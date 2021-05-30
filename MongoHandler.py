# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:12:53 2021

@author: tomcs
"""
from pymongo import MongoClient
import pandas as pd

class Mongo():
    def __init__(self,collectionName="invoices"):
        self.db = self.connect(collectionName)

    def connect(self,collectionName):
        return MongoClient('127.0.0.1', 27017).gym[collectionName]
    def getAll(self):
        """    
    
        Returns The whole DB
        -------
        pd.DataFrame
    
        """
        df = list(self.db.find())
        df = pd.DataFrame(df)
        df._id = df._id.astype(str)
        # df = df.set_index("_id")
        return df
    def getById(self,_id):
        return self.db.find_one({"_id":_id})
    def searchByField(self,fieldName,Value):
        return self.db.find({fieldName:Value})
    def insert(self,data):
        """
        Inserts one or multiple lines to the database.
    
        Parameters
        ----------
        data : DataFrame
            DESCRIPTION.
    
        """  
        # result = self.db.insert_many(data.to_dict("records"))
        result = self.db.insert_many(data)
        print('Multiple posts: {0}'.format(result.inserted_ids))
        return result
    def getEstimatedCount(self):
        # Fast counting method  using collection metadata
        return self.db.estimated_document_count()
    def getRealCount(self):
        # Real count of the documents
        return self.db.count_documents()
    
    
    
    def replaceById(self,_id,data):
        return self.db.replace_one({"_id":_id},data.to_dict(),upsert=True)