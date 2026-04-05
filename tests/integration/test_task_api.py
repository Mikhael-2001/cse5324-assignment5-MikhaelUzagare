import unittest
import json
from app import create_app, db

class TestTaskAPI(unittest.TestCase):
    def setUp(self):
        """Initialize the app and a clean database [cite: 276-279]"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Cleanup database [cite: 280-283]"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_task_integration(self):
        """Verify the POST /api/tasks endpoint works with the DB [cite: 257]"""
        payload = {'title': 'Integration Test Task', 'priority': 'high'}
        response = self.client.post(
            '/api/tasks',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Integration Test Task')

    def test_get_tasks_integration(self):
        """Verify the GET /api/tasks endpoint retrieves data [cite: 209]"""
        # Create a task first
        self.client.post('/api/tasks', data=json.dumps({'title': 'Task 1'}), content_type='application/json')
        
        response = self.client.get('/api/tasks')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)