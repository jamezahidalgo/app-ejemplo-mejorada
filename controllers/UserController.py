from flask import request, jsonify
from services.UserService import create_user

def create_user_controller():
    data = request.get_json()
    username = data.get('username')
    create_user(username)
    return jsonify({"mensaje": "Usuario creado"}), 201