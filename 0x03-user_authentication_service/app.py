#!/usr/bin/env python3
""" flask app """
from flask import request, jsonify, Flask


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """ return json payload """
    return jsonify({"message": "Bienvenue"})
