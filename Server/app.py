from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


items= ["Мстители", "ЛЮДИ Х", "ЛЮДИ В ЧЕРНОМ"]

@app.route("/")
@cross_origin()
def hello():
    return jsonify({'result': items})