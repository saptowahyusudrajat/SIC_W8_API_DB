import pymongo

database_password = "1331"
database_url = f"mongodb+srv://saptowahyusudrajat:{database_password}@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(database_url)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)