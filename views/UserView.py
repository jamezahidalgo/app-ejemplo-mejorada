from flask import Blueprint
from controllers.UserController import create_user_controller

main = Blueprint('main', __name__)

@main.route('/users', methods=['POST'])
def create_user():
    return create_user_controller()