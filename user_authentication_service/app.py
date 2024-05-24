#!/usr/bin/env python3
""" a Flask app """
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """ a Flask app that has a single GET route ("/") and use flask.jsonify
    to return a JSON payload of the form
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """ implement the end-point to register a user
    The end-point should expect two form data fields: "email" and "password".
    If the user does not exist, the end-point should register it and respond
    with the following JSON payload
    If the user is already registered, catch the exception and return a JSON
    payload of the form and return a 400 status code"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({'email': email, 'message': 'user created'})
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
