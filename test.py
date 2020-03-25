import pymongo

client = pymongo.MongoClient("mongodb+srv://website:123@websitebackend-g3osg.mongodb.net/test?retryWrites=true&w=majority")
db = client.test