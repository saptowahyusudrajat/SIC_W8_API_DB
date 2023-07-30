import pymongo # meng-import library pymongo yang sudah kita install

from pymongo.mongo_client import MongoClient

#uri = "mongodb+srv://saptowahyusudrajat:<password>@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb+srv://saptowahyusudrajat:1331@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)
db = client['test_SIC'] # ganti sesuai dengan nama database kalian
my_collections = db['col1'] # ganti sesuai dengan nama collections kalian

# Data yang ingin dimasukkan
murid_1 = {'nama':'John Doe','Jurusan':'IPS','Nilai':90}
murid_2 = {'nama':'This is name', 'Jurusan':'IPA','Nilai':100}

results = my_collections.insert_many([murid_1,murid_2])
print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan
