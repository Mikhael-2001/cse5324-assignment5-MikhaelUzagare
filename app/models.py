from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    tasks = db.relationship('Task', backref='owner', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def validate_email(self):
        if "@" not in self.email:
            raise ValueError("Invalid email format")

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='todo') # todo, in_progress, completed
    priority = db.Column(db.String(20), default='medium') # low, medium, high
    due_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def update_status(self, new_status):
        valid_statuses = ['todo', 'in_progress', 'completed']
        if new_status not in valid_statuses:
            raise ValueError("Invalid status")
        # Logic check: Cannot go back to todo if completed (as per assignment example)
        if self.status == 'completed' and new_status == 'todo':
            raise ValueError("Cannot revert completed task to todo")
        self.status = new_status