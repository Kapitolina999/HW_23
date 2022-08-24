import os

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

from utils import get_result, get_cmd

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    query = request.json

    try:
        file_name = query["file_name"]
        cmd1 = query["cmd1"]
        value1 = query["value1"]
        cmd2 = query["cmd2"]
        value2 = query["value2"]
    except KeyError:
        return '', 400

    if not os.path.exists(os.path.join(DATA_DIR, file_name)):
        raise BadRequest

    chunk = get_cmd(query)

    result = get_result(DATA_DIR, file_name, chunk)
    return jsonify(list(result))


if __name__ == '__main__':
    app.run()

