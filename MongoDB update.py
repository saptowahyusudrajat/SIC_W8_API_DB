import pymongo

#uri = "mongodb+srv://saptowahyusudrajat:<password>@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb+srv://saptowahyusudrajat:1331@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)
db = client['test_SIC'] # ganti sesuai dengan nama database kalian
my_collections = db['col1'] # ganti sesuai dengan nama collections kalian

# Data yang ingin diperbaharui
nama_murid = {'nama':'sapto'}
nilai_baru = {'$set':{'Nilai':1331}}
my_collections.update_one(nama_murid,nilai_baru)