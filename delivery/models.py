from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient("mongodb+srv://Aditi_Sri:Aditi1311@cluster0.oqnfp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mydatabase"]
collection = db["items"]  # Collection name

class ItemModel:
    @staticmethod
    def create_item(data):
        """Insert a new item into MongoDB"""
        return collection.insert_one(data).inserted_id

    @staticmethod
    def get_item(item_id):
        """Retrieve an item by ID"""
        return collection.find_one({"_id": ObjectId(item_id)})

    @staticmethod
    def get_all_items():
        """Retrieve all items"""
        return list(collection.find())

    @staticmethod
    def update_item(item_id, data):
        """Update an item by ID"""
        return collection.update_one({"_id": ObjectId(item_id)}, {"$set": data})

    @staticmethod
    def delete_item(item_id):
        """Delete an item by ID"""
        return collection.delete_one({"_id": ObjectId(item_id)})
