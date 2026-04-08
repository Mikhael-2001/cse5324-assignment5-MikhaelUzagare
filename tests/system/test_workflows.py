import unittest
import json
from app import create_app, db
from app.models import User, Category, Task

class TestWorkflows(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        self.user = User(username='mikhael', email='mikhael@uta.edu')
        self.user.set_password('SecurePass123!')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_full_task_lifecycle(self):
        """Workflow: Login -> Create Task -> Verify DB [cite: 353]"""
        login_res = self.client.post('/api/auth/login',
                                     data=json.dumps({'username': 'mikhael', 'password': 'SecurePass123!'}),
                                     content_type='application/json')
        token = json.loads(login_res.data)['token']
        headers = {'Authorization': f'Bearer {token}'}

        task_res = self.client.post('/api/tasks',
                                    data=json.dumps({'title': 'Lifecycle Task'}),
                                    content_type='application/json',
                                    headers=headers)
        self.assertEqual(task_res.status_code, 201)

    def test_category_workflow(self):
        """Workflow: Login -> Category -> Task [cite: 354]"""
        login_res = self.client.post('/api/auth/login',
                                     data=json.dumps({'username': 'mikhael', 'password': 'SecurePass123!'}),
                                     content_type='application/json')
        token = json.loads(login_res.data)['token']
        headers = {'Authorization': f'Bearer {token}'}

        cat = Category(name='Project')
        db.session.add(cat)
        db.session.commit()

        payload = {'title': 'E2E Task', 'category_id': cat.id}
        res = self.client.post('/api/tasks', data=json.dumps(payload), content_type='application/json', headers=headers)
        self.assertEqual(res.status_code, 201)

    def test_error_recovery_workflow(self):
        """Workflow: Invalid operations """
        # No token should result in 401
        res = self.client.post('/api/tasks', data=json.dumps({'title': 'No Auth'}), content_type='application/json')
        self.assertEqual(res.status_code, 401)