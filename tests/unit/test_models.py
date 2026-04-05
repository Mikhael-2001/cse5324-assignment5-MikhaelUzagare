import unittest
from app import create_app, db
from app.models import User, Task

class TestModels(unittest.TestCase):
    def setUp(self):
        """Set up a temporary database for each test"""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Clean up the database after each test"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        """Test that passwords are properly hashed and verified"""
        user = User(username='mikhael', email='test@uta.edu')
        user.set_password('SecurePass123!')
        self.assertNotEqual(user.password_hash, 'SecurePass123!') # [cite: 288]
        self.assertTrue(user.check_password('SecurePass123!')) # [cite: 289]

    def test_task_status_transitions(self):
        """Test valid and invalid status transitions"""
        task = Task(title='Finish Assignment', status='todo')
        # Valid transition [cite: 322-324]
        task.update_status('in_progress')
        self.assertEqual(task.status, 'in_progress')
        # Invalid transition: Reverting completed to todo [cite: 330-331]
        task.status = 'completed'
        with self.assertRaises(ValueError):
            task.update_status('todo')