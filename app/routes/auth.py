from flask import Blueprint, request, jsonify
from app.models import db, User
from app.utils.validators import validate_email, validate_password_strength

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    """Register a new user with validation [cite: 157, 247]"""
    data = request.get_json()
    
    if not validate_email(data.get('email')):
        return jsonify({'error': 'Invalid email'}), 400
    
    if not validate_password_strength(data.get('password')):
        return jsonify({'error': 'Password too weak'}), 400
        
    if User.query.filter_by(username=data.get('username')).first():
        return jsonify({'error': 'User already exists'}), 400

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered', 'user_id': user.id}), 201

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    """Login and return a dummy JWT token for this assignment """
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    
    if user and user.check_password(data.get('password')):
        # In a real app, we'd use flask-jwt-extended here
        return jsonify({'token': 'dummy-jwt-token', 'user_id': user.id}), 200
        
    return jsonify({'error': 'Invalid credentials'}), 401