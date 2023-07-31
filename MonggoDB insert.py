import pymongo

database_password = "1331"
database_name = "test_SIC"
database_collection = "col1"
database_url = f"mongodb+srv://saptowahyusudrajat:{database_password}@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(database_url)
db = client[database_name]
my_collections = db[database_collection]

# Data yang ingin dimasukkan
murid_1 = {'nama':'John Doe','Jurusan':'IPS','Nilai':90}
murid_2 = {'nama':'Alex', 'Jurusan':'IPA','Nilai':100}

results = my_collections.insert_many([murid_1,murid_2])
print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan