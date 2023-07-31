import pymongo

database_password = "1331"
database_name = "test_SIC"
database_collection = "col1"
database_url = f"mongodb+srv://saptowahyusudrajat:{database_password}@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(database_url)
db = client[database_name]
my_collections = db[database_collection]

# Data yang ingin diperbaharui
nama_murid = {'nama':'sapto'}
nilai_baru = {'$set':{'Nilai':1332}}
my_collections.update_one(nama_murid,nilai_baru) #gunakan update_many untuk mengubah lebih dari satu nama yang sama