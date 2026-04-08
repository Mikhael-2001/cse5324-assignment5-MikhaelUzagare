from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import User, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data.get('username')).first():
        return jsonify({"msg": "User already exists"}), 400
    
    user = User(username=data.get('username'), email=data.get('email'))
    user.set_password(data.get('password'))
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    
    if user and user.check_password(data.get('password')):
        # This token MUST be signed with the key defined in __init__.py
        access_token = create_access_token(identity=str(user.id))
        return jsonify(token=access_token), 200
    
    return jsonify({"msg": "Invalid credentials"}), 401