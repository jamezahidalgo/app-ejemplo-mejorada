from flask import Blueprint
from controllers.TaskController import create_task_controller, mark_task_done_controller

main = Blueprint('main', __name__)

@main.route('/tasks', methods=['POST'])
def create_task():
    return create_task_controller()

@main.route('/tasks/<int:task_id>/done', methods=['PATCH'])
def mark_task_done(task_id):
    return mark_task_done_controller(task_id)