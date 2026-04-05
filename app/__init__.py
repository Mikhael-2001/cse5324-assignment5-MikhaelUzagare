from flask import Flask
from app.models import db

def create_app(config_name='default'):
    """
    Application factory to create and configure the Flask app.
    Registers blueprints for Auth and Tasks [cite: 171-176].
    """
    app = Flask(__name__)
    
    if config_name == 'testing':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    # Register Blueprints [cite: 174-176]
    from app.routes.tasks import tasks_bp
    from app.routes.auth import auth_bp
    
    app.register_blueprint(tasks_bp)
    app.register_blueprint(auth_bp)
    
    return app