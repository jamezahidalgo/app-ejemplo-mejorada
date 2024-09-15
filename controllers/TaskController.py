from flask import request, jsonify
from services.TaskService import create_task, mark_task_as_done

def create_task_controller():
    data = request.get_json()
    user_id = data.get('user_id')
    description = data.get('descripcion')
    create_task(user_id, description)
    return jsonify({"mensaje": "Tarea creada"}), 201

def mark_task_done_controller(task_id):
    mark_task_as_done(task_id)
    return jsonify({"mensaje": "Tarea marcada como terminada"}), 200