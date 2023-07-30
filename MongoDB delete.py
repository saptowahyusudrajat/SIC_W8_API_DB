import pymongo

#uri = "mongodb+srv://saptowahyusudrajat:<password>@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb+srv://saptowahyusudrajat:1331@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)
db = client['test_SIC'] # ganti sesuai dengan nama database kalian
my_collections = db['col1'] # ganti sesuai dengan nama collections kalian

## *identifier* data yang ingin dihapus
nama_data = {'nama':'This is name'}
my_collections.delete_one(nama_data)