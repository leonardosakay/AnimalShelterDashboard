'''
Author: Caio De Morais
Date: 10/03/2021
Description: Script creates, reads, deletes, and updates documents from AAC database.
'''

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:53802/AAC' % (username, password))
        self.database = self.client['AAC']
        self.collection = self.database['animals']
                                       

# Complete this create method to implement the C in CRUD.
    def create(self, data):
      
        if data is not None:
            if data:
                self.database.animals.insert_one(data)
                return True
        else:
            Exception("Error, please try again!") 
            
# Create method to implement the R in CRUD.
    def read (self,findKeyValue):

         # Return values if found     
        data = self.database.animals.find(findKeyValue, {'_id':False})
        return data
                 
    
# Create method to update documents 
    def updateDocument(self, myQuery, newValue):
        col = self.collection
        if myQuery:
            col.update_many(myQuery, { "$set": newValue })
            print("Data successfully updated!")
        else:
            raise Exception("Key/value not found!") 
            
# Create method to delete documents 
    def deleteDocument(self, deleteKeyValue):
        col = self.collection
        if deleteKeyValue:
            col.delete_one(deleteKeyValue)
            print("Data successfully deleted!")
        else:
            raise Exception("Key/value not found!") 

      
