from flask import Blueprint
from flask import Flask, render_template ,jsonify, make_response, redirect, request, url_for, session
from exts import db
from models import UserModel, GithubModel, RatingModel
import pymysql
import csv
from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.sql.functions import col




bp = Blueprint("index", __name__, url_prefix="/")

@bp.route("/")
def index():
    items_github = GithubModel.query.order_by(GithubModel.id.desc()).limit(9).all()
    
    if session:
        userId = session['user_id']
    else:
        return render_template("index.html",items_github=items_github)
    recommends = []
    ratings = RatingModel.query.filter_by(userId=userId).first()
    if ratings:
        # 建立 MySQL 连接
        conn1 = pymysql.connect(
            host='localhost',
            user='debian-sys-maint',
            password='ET8f5F3qMOvqPnbM',
            db='recommend',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor1 = conn1.cursor()
        sql = 'select * from ratings'
        cursor1.execute(sql)
        data = cursor1.fetchall()
        conn1.close()

        csv_file = '/root/html/scheduled/lastest_ratings.csv'
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
        # 将字符串类型的列转换为数值类型
        data = data.withColumn("userId", col("userId").cast("integer"))
        data = data.withColumn("githubId", col("githubId").cast("integer"))
        data = data.withColumn("rating", col("rating").cast("float"))
        # 创建 ALS 模型
        als = ALS(userCol="userId", itemCol="githubId", ratingCol="rating", rank=10, regParam=0.01)
        # 训练 ALS 模型
        model = als.fit(data)

        # 对特定用户进行推荐
        userRecs = model.recommendForUserSubset(spark.createDataFrame([(userId,)]).toDF("userId"), 9).first()
        row_recommends = userRecs["recommendations"]
        for recommend in row_recommends:
            recommends.append(GithubModel.query.filter_by(id=recommend['githubId']).first())
        items_github = recommends        
        spark.stop()
    return render_template("index.html",items_github=items_github)
