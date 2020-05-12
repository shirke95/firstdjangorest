import pymongo

#client = pymongo.MongoClient("mongodb://admin:pass123@cluster01-doswy.mongodb.net/test?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://admin:pass123@cluster01-doswy.mongodb.net/test?retryWrites=true&w=majority")
#db = client.sample_airbnb
db = client.dataecom

#print(db)
print(db.list_collection_names())

#coll = db.get_collection('listingsAndReviews')
coll = db.get_collection('collecom')

print(coll)

ab = coll.find()
bc = coll.find_one()
#thast the final
for i in ab:
	print(i['_id'])
	#print(bc)
#that the final oh yeh