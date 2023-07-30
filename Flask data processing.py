from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/',methods=[ 'GET'])
def hello_world():
    return 'GET METHOD'

@app.route('/data',methods=['POST'])
def data():
    params = request.args.get('params')
    return f'Hello {params}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

#URL http://127.0.0.1:5000/data?params=1 maka akan mengembalikan Hello 1.