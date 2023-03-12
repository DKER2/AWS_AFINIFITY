import os
import logging
from typing import List, Dict, Tuple, Set, Optional

from flask import Flask, flash, request, request, jsonify, abort
from flask_cors import CORS, cross_origin
from infer import infer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('HELLO WORLD')

app = Flask(__name__)

@app.route("/get_suggestion", methods=['GET','POST'])
def get_suggestion() -> dict:
    print(request)
    message = request.json
    print(message)
    print("I am waiting for open api to return the reuslt")
    response = infer(message['seeker'], message['supporter'])
    print(response)
    return jsonify({"operations": response})

if __name__ == "__main__":
    cors = CORS(app, expose_headers='Authorization')
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run(debug=True, host="0.0.0.0", use_reloader=False, port=8080)
