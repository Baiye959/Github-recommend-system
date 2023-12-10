from exts import db
import pandas as pd
import json
import numpy as np
import faiss


class UserModel(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar,null=0
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(100),nullable=False)

class GithubModel(db.Model):
    __tablename__="github_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar,null=0
    name = db.Column(db.String(1000),nullable=False)
    link = db.Column(db.String(1000),nullable=False)
    introduction = db.Column(db.String(5000),nullable=False)
    language = db.Column(db.String(64),nullable=False)
    stars = db.Column(db.Integer,nullable=False)
    forks = db.Column(db.Integer,nullable=False)

class RatingModel(db.Model):
    __tablename__="ratings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar,null=0
    userId = db.Column(db.Integer,nullable=False)
    githubId = db.Column(db.Integer,nullable=False)
    rating = db.Column(db.Float,nullable=False)
    timestamp = db.Column(db.Integer,nullable=False)

class CollectModel(db.Model):
    __tablename__="collect"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # varchar,null=0
    githubId = db.Column(db.Integer,nullable=False)
    userId = db.Column(db.Integer,nullable=False)

class EmbeddingManager(object):

    def __init__(self, fpath, key_name, value_name):
        # pandas.dataframe
        self.df = pd.read_csv(fpath)
        # 将文件中的embedding加载到内存
        self.dict_embedding = self.load_embedding_to_dict(key_name, value_name)
        # 在faiss建立索引
        self.faiss_index = self.load_embedding_to_faiss(key_name, value_name)
    
    def get_embedding(self,key):
        return self.dict_embedding[str(key)]

    def load_embedding_to_dict(self, key_name, value_name):
        return {
            str(row[key_name]): row[value_name]
            for index,row in self.df.iterrows()
        }

    def load_embedding_to_faiss(self,key_name, value_name):
        # id列表
        ids = self.df[key_name].values.astype(np.int64)
        # 二维embedding
        datas = [json.loads(x)for x in self.df[value_name]]
        datas = np.array(datas).astype(np.float32)
        # 维度
        dimension = datas.shape[1]
        # 创建faiss索引
        index = faiss.IndexFlatL2(dimension)
        index2 = faiss.IndexIDMap(index)
        index2.add_with_ids(datas, ids)
        return index2

    def search_ids_by_embedding(self, embedding_str, topk):
        """实现近邻搜索"""
        input = np.array(json.loads(embedding_str))
        input = np.expand_dims(input, axis=0).astype(np.float32)
        D,I = self.faiss_index.search(input,topk)
        return list(I[0])