import unittest
import json
from app import create_app, db
from app.models import User

class TestTaskAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Create a user and get a token for all requests
        self.user = User(username='testuser', email='test@uta.edu')
        self.user.set_password('SecurePass123!')
        db.session.add(self.user)
        db.session.commit()

        # Login to get the token
        login_res = self.client.post('/api/auth/login',
                                     data=json.dumps({'username': 'testuser', 'password': 'SecurePass123!'}),
                                     content_type='application/json')
        self.token = json.loads(login_res.data)['token']
        self.headers = {'Authorization': f'Bearer {self.token}'}

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_task_integration(self):
        """Verify the POST /api/tasks works with valid auth [cite: 342]"""
        payload = {'title': 'Integration Test Task', 'priority': 'high'}
        response = self.client.post('/api/tasks',
                                    data=json.dumps(payload),
                                    content_type='application/json',
                                    headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_get_tasks_integration(self):
        """Verify retrieval works with auth [cite: 342]"""
        self.client.post('/api/tasks', 
                         data=json.dumps({'title': 'Task 1'}), 
                         content_type='application/json',
                         headers=self.headers)
        
        response = self.client.get('/api/tasks', headers=self.headers)
        self.assertEqual(response.status_code, 200)