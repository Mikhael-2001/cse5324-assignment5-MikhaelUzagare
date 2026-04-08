from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.task_service import TaskService
from app import db

tasks_bp = Blueprint('tasks', __name__)
service = TaskService()

@tasks_bp.route('/api/tasks', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"msg": "Missing title"}), 400
    task = service.create_task(user_id, data)
    return jsonify({"id": task.id, "title": task.title}), 201

@tasks_bp.route('/api/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = service.get_user_tasks(user_id)
    return jsonify([{"id": t.id, "title": t.title} for t in tasks]), 200