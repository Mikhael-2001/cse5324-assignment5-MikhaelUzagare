from app.models import Task, db

class TaskService:
    def create_task(self, user_id, data):
        task = Task(
            title=data.get('title'),
            description=data.get('description', ''),
            priority=data.get('priority', 'medium'),
            user_id=user_id,
            category_id=data.get('category_id')
        )
        db.session.add(task)
        db.session.commit()
        return task

    def get_user_tasks(self, user_id):
        return Task.query.filter_by(user_id=user_id).all()