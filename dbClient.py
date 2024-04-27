from pymongo import MongoClient

connecttionString = 'mongodb://127.0.0.1:27017'

try:
    client = MongoClient(connecttionString)
    db = client['urlShortener']
    urlMappingCollection = db['url_mapping_collection']

#     testing by printing all values
#     allRecords = urlMappingCollection.find()
#     for record in allRecords:
#         print(record)
except:
    print("Error while connecting to client/db/collection")