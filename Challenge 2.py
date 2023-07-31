import pymongo
from flask import Flask
from flask import request

database_password = "1331"
database_name = "test_SIC"
database_collection = "sensor"
database_url = f"mongodb+srv://saptowahyusudrajat:{database_password}@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(database_url)
db = client[database_name]
my_collections = db[database_collection]

def baca_data():
    query = {}
    cursor = my_collections.find(query)

    temperature_list = []
    kelembapan_list = []
    for document in cursor:
        temperature = int(document['temperature'])
        kelembapan = int(document['kelembapan'])
        temperature_list.append(temperature)
        kelembapan_list.append(kelembapan)
    
    # rata rata = penjumlahan seluruh data / jumlah data
    temperature_rata_rata = sum(temperature_list) / len(temperature_list)
    kelembapan_rata_rata = sum(kelembapan_list) / len(kelembapan_list)

    return temperature_rata_rata, kelembapan_rata_rata


average_temperature, average_kelembapan = baca_data()

#Flask API
app = Flask(__name__)

@app.route('/sensor1/temperature/avg',methods=[ 'GET'])
def get_temperature_rata_rata():
    return f'TEMPERATURE RATA-RATA= {average_temperature}'

@app.route('/sensor1/kelembapan/avg',methods=[ 'GET'])
def get_gelembapan_rata_rata():
    return f'KELEMBAPAN RATA-RATA= {average_kelembapan}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')