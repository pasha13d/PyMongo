from pprint import pprint
import pymongo
from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId
#from pymongo.objectid import ObjectId
from pymongo.collection import ReturnDocument

class MongoDBManagement:
    def __init__(self):
        mongo_host = 'localhost'
        mongo_port = '27017'
        self.client = MongoClient(mongo_host + ':' + mongo_port)
        self.db = self.client['mongoDatabaseDemo']
        self.collection_employee = self.db['employee']

    def insert_one_employee(self):
        self.collection_employee.insert_one({
            "name": "Piper Pasha",
            "age": 24,
            "email": "mahabub13d1995@gmail.com"
        })

    def insert_many_employee(self):
        new_employee = self.collection_employee.insert_many(
            [
                {
                    "name": "shajir",
                    "age": 26,
                    "email": "shajir@gmail.com"
                },
                {
                    "name": "Deepika",
                    "age": 24,
                    "email": "sabrina@gmail.com"
                }
            ]
        )

    def update_a_student(self):
        self.collection_employee.find_one_and_update(
            {
                '_id': ObjectId('5c94ecb1e390dc0acb385793')
            },
            {
                '$set': {
                    'name': "Shajir Uddin Haider Alve"
                }
            },
            projection={'seq': True, '_id': False},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )

    def find_all_employee(self):
        all_employee = self.collection_employee.find({})
        print("Number of records = " + str(all_employee.count()))
        for each_student in all_employee:
            pprint(each_student)

    def delete_an_employee(self):
        self.collection_employee.delete_one({"name": "Deepika"})

if __name__ == "__main__":
    mongoDB = MongoDBManagement()
    #mongoDB.insert_one_employee()
    # mongoDB.insert_many_employee()
    # mongoDB.update_a_student()
    # mongoDB.find_all_employee()
    mongoDB.delete_an_employee()