#!/usr/bin/env python3
""" Create a new Flask view that handles all routes for the Session
authentication. """
from flask import jsonify, request, abort
from models.user import User
from api.v1.views import app_views
from os import getenv


SESSION_NAME = getenv("SESSION_NAME")


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def sess_auth() -> str:
    """ POST /api/v1/auth_session/login
    returns the status of the API """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': email})
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    for each_user in users:
        if not each_user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(users[0].id)
    user_id = auth.user_id_for_session_id(session_id)
    user = User.get(user_id)
    user_dict = jsonify(user.to_json())
    user_dict.set_cookie(SESSION_NAME, session_id)

    return user_dict


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def sess_auth_del() -> str:
    """ deleting the Session ID contains in the request as cookie """
    from api.v1.app import auth
    session_id = request.cookies.get(SESSION_NAME)
    if session_id is None:
        abort(404)
    auth.destroy_session(request)
    return jsonify({}), 200
