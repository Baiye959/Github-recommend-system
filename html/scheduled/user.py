from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALSModel
import pandas as pd



# 创建 Spark 会话
spark = SparkSession.builder.appName("ALS_user").getOrCreate()
# 从保存的路径中加载ALS推荐系统模型
model_path = "/root/html/scheduled/als_model"
model = ALSModel.load(model_path)

# # 对特定用户进行推荐
# # 为特定用户（用户ID为1）生成推荐结果
# user_id = 1
# userRecs = model.recommendForUserSubset(spark.createDataFrame([(user_id,)]).toDF("userId"), 10)
# # 显示结果
# userRecs.show(truncate = False)
# for item in userRecs:
#     print(item)


# user_recommend = model.recommendForAllItems(10)
# test.show(truncate = False)
# for item in user_recommend
#     print(item)


df_item = model.itemFactors.toPandas()
df_item.to_csv('item_embedding.csv',index=False,encoding="utf-8")

df_user = model.userFactors.toPandas()
df_user.to_csv('user_embedding.csv',index=False,encoding="utf-8")

spark.stop()