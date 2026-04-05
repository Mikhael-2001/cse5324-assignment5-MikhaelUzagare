import unittest
import json
from app import create_app, db

class TestUserFlow(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_complete_user_lifecycle(self):
        """System Test: Register -> Login -> Create Task [cite: 236, 258-260]"""
        # 1. Register [cite: 247]
        reg_payload = {
            'username': 'mikhael',
            'email': 'mikhael@uta.edu',
            'password': 'SecurePass123!'
        }
        reg_res = self.client.post('/api/auth/register', 
                                   data=json.dumps(reg_payload), 
                                   content_type='application/json')
        self.assertEqual(reg_res.status_code, 201)

        # 2. Login [cite: 259]
        login_payload = {'username': 'mikhael', 'password': 'SecurePass123!'}
        login_res = self.client.post('/api/auth/login', 
                                     data=json.dumps(login_payload), 
                                     content_type='application/json')
        self.assertEqual(login_res.status_code, 200)
        token = json.loads(login_res.data)['token']
        self.assertTrue(token)

        # 3. Create Task [cite: 260]
        task_payload = {'title': 'System Test Task'}
        task_res = self.client.post('/api/tasks', 
                                    data=json.dumps(task_payload), 
                                    content_type='application/json')
        self.assertEqual(task_res.status_code, 201)