from pymongo import MongoClient

client = MongoClient("mongodb+srv://mukilan:1234@cluster0.cp4l5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db_account = client.Account
