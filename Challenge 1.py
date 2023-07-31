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

def kirim_data(temperature, kelembapan, timestamp):
    sensor = {
        'temperature':temperature,
        'kelembapan':kelembapan,
        'timestamp':timestamp
    }
    
    inserted_data = my_collections.insert_one(sensor)

    #print id data yang diinsert ke mongoDB di terminal
    print('Inserted document ID:', inserted_data.inserted_id)

app = Flask(__name__)

@app.route('/sensor1',methods=['POST'])
def sensor1():

    #input parameter yang harus diketikkan di postman. Misal: parameter = temperature | value=30
    temperature_input = request.args.get('temperature')
    kelembapan_input  = request.args.get('kelembapan')
    timestamp_input  = request.args.get('timestamp')
    
    kirim_data(temperature_input, kelembapan_input, timestamp_input)

    #print respon dari POST method pada postman/browser
    return f'INPUT TEMPERATURE= {temperature_input}, INPUT KELEMBAPAN= {kelembapan_input}, INPUT TIMESTAMP= {timestamp_input}' 

if __name__ == '__main__':
    app.run(host='0.0.0.0')