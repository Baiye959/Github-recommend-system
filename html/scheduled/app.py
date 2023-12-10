from flask import Flask
from flask_apscheduler import APScheduler
from gevent import pywsgi # pywsgi: flask开发环境转生产环境
import datetime
import pymysql
from config import conn
import csv
from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.sql.functions import col



class Config(object):
    SCHEDULER_API_ENABLED = True


scheduler = APScheduler()

@scheduler.task('cron', id='do_job', day='*', hour='00', minute='00', second='00')
def job():
    cursor = conn.cursor()
    sql = 'select * from ratings'
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()

    csv_file = 'lastest_ratings.csv'
    f = open(csv_file,'w',encoding='utf-8',newline="")
    csv_writer = csv.writer(f)
    csv_writer.writerow(["userId","githubId","rating","timestamp"])

    for line in data:
        csv_writer.writerow([line['userId'],line['githubId'],line['rating'],line['timestamp']])

    f.close()
    print("数据导出成功")


    # 创建 Spark 会话
    spark = SparkSession.builder.appName("ALS").getOrCreate()
    # 读取数据
    data = spark.read.csv("file:///root/html/scheduled/lastest_ratings.csv", header=True, inferSchema=True)
    # 数据预处理
    # 去除空值
    data = data.dropna()
    # # 处理异常值
    # data = data.filter((col("rating") >= 1) & (col("rating") <= 5))
    # 将字符串类型的列转换为数值类型
    data = data.withColumn("userId", col("userId").cast("integer"))
    data = data.withColumn("githubId", col("githubId").cast("integer"))
    data = data.withColumn("rating", col("rating").cast("float"))
    # 划分训练集和测试集
    (training, test) = data.randomSplit([0.8, 0.2])
    # 创建 ALS 模型
    als = ALS(userCol="userId", itemCol="githubId", ratingCol="rating", coldStartStrategy="drop")
    # 定义参数网格
    paramGrid = ParamGridBuilder() \
        .addGrid(als.rank, [10, 20, 30]) \
        .addGrid(als.regParam, [0.01, 0.05, 0.1]) \
        .build()
    # 创建交叉验证器
    crossval = CrossValidator(estimator=als,
                            estimatorParamMaps=paramGrid,
                            evaluator=RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction"),
                            numFolds=5)
    # 训练 ALS 模型
    model = crossval.fit(training)
    bestModel = model.bestModel
    # 在测试数据上进行预测
    predictions = bestModel.transform(test)
    # 计算均方根误差
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
    rmse = evaluator.evaluate(predictions)
    print("Root-mean-square error = " + str(rmse))
    # 导出embedding
    df_item = bestModel.itemFactors.toPandas()
    df_item.to_csv('item_embedding.csv',index=False,encoding="utf-8")

    df_user = bestModel.userFactors.toPandas()
    df_user.to_csv('user_embedding.csv',index=False,encoding="utf-8")

    spark.stop()
    print("embedding导出成功")



if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())

    # it is also possible to enable the API directly
    # scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()

    # app.run(port=5002)
    server = pywsgi.WSGIServer(('0.0.0.0', 5002), app)
    server.serve_forever()