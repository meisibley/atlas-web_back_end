#!/usr/bin/env python3
""" a Flask app """
from flask import Flask, jsonify
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """ a Flask app that has a single GET route ("/") and use flask.jsonify
    to return a JSON payload of the form
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
