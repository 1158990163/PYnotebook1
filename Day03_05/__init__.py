from pymongo import MongoClient
client = MongoClient()
database = client['Chapter8']
collection = database['spider']
data={'id':123,'name':'kingname','age':23,'salary':999909}
collection.insert_one(data)

