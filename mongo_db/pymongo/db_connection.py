from pymongo import MongoClient

url = "mongodb://localhost:27017"
db_name = "mongodb_test_pymongo"

client = MongoClient(url)
db = client[db_name]