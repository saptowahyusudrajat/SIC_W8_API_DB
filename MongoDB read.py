import pymongo

database_password = "1331"
database_name = "test_SIC"
database_collection = "col1"
database_url = f"mongodb+srv://saptowahyusudrajat:{database_password}@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(database_url)
db = client[database_name] # ganti sesuai dengan nama database kalian
my_collections = db[database_collection] # ganti sesuai dengan nama collections kalian

for x in my_collections.find():
  print(x)
