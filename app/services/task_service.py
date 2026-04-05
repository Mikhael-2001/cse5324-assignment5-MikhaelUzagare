from app.models import db, Task

class TaskService:
    def create_task(self, user_id, data):
        """Creates a task and saves it to the DB [cite: 353-354]"""
        task = Task(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'medium'),
            user_id=user_id
        )
        db.session.add(task)
        db.session.commit()
        return task

    def get_user_tasks(self, user_id, filters=None):
        """Retrieves tasks with optional filtering [cite: 370-372]"""
        query = Task.query.filter_by(user_id=user_id)
        if filters:
            if 'status' in filters:
                query = query.filter_by(status=filters['status'])
        return query.all()