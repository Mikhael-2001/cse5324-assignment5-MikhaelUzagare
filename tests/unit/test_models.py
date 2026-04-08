import unittest
from app.models import User, Task, Category, db
from app import create_app

class TestModels(unittest.TestCase):
    def setUp(self):
        """Initialize the app and a clean in-memory database"""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Cleanup database after each test"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # --- User Model Tests ---
    def test_password_hashing(self):
        """Verify passwords are properly hashed and checked"""
        user = User(username='testuser', email='test@uta.edu')
        user.set_password('SecurePass123!')
        self.assertNotEqual(user.password_hash, 'SecurePass123!')
        self.assertTrue(user.check_password('SecurePass123!'))
        self.assertFalse(user.check_password('wrongpass'))

    # --- Task Model Tests ---
    def test_task_creation(self):
        """Verify task properties are correctly stored"""
        task = Task(title='Unit Test Task', priority='high', status='todo')
        db.session.add(task)
        db.session.commit()
        self.assertIsNotNone(task.id)
        self.assertEqual(task.priority, 'high')

    def test_task_status_transitions(self):
        """Verify valid status progression"""
        task = Task(title='Transition Task', status='todo')
        task.update_status('in_progress')
        self.assertEqual(task.status, 'in_progress')
        task.update_status('completed')
        self.assertEqual(task.status, 'completed')

    def test_invalid_status_transition(self):
        """Verify that illegal transitions raise a ValueError"""
        task = Task(title='Illegal Task', status='completed')
        with self.assertRaises(ValueError):
            task.update_status('todo')

    # --- Category & Relationship Tests ---
    def test_category_creation(self):
        """Verify Category model creation"""
        cat = Category(name='Academic')
        db.session.add(cat)
        db.session.commit()
        self.assertEqual(cat.name, 'Academic')

    def test_category_task_relationship(self):
        """Verify 1-to-Many relationship between Category and Task"""
        cat = Category(name='Work')
        db.session.add(cat)
        task = Task(title='Finish Assignment', category=cat)
        db.session.add(task)
        db.session.commit()
        
        # Check bidirectional relationship
        self.assertEqual(cat.tasks.first().title, 'Finish Assignment')
        self.assertEqual(task.category.name, 'Work')