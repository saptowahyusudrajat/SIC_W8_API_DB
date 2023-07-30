from flask import Flask
app = Flask(__name__)

@app.route('/',methods=[ 'GET'])
def hello_world():
    return 'GET METHOD'

@app.route('/data',methods=['POST'])
def data():
    return 'POST METHOD'

if __name__ == '__main__':
    app.run(host='0.0.0.0')