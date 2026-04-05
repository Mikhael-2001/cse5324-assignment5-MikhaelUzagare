from flask import Blueprint, request, jsonify
from app.services.task_service import TaskService
from app.utils.validators import sanitize_input

tasks_bp = Blueprint('tasks', __name__)
task_service = TaskService()

@tasks_bp.route('/api/tasks', methods=['POST'])
def create_task():
    """Endpoint to create a new task [cite: 158, 209]"""
    data = request.get_json()
    
    # Basic Validation
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    # Sanitize the input [cite: 394, 428]
    data['title'] = sanitize_input(data['title'])
    
    # Use the service to save to DB [cite: 360]
    task = task_service.create_task(user_id=1, data=data) # Defaulting to user 1 for now
    
    return jsonify({
        'id': task.id,
        'title': task.title,
        'status': task.status
    }), 201

@tasks_bp.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Endpoint to list all tasks for a user [cite: 158, 209]"""
    tasks = task_service.get_user_tasks(user_id=1)
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'status': t.status
    } for t in tasks]), 200