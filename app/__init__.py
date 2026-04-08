from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# 1. Initialize extensions at the top to avoid circular imports
db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'cse5324-ultra-secure-key-123'
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    
    # 2. Bind extensions to the app instance
    db.init_app(app)
    jwt.init_app(app)
    
    # 3. Import Blueprints INSIDE the function to prevent circularity
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    
    return app