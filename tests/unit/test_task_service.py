import unittest
from unittest.mock import MagicMock, patch
from app.services.task_service import TaskService
from app.models import Task

class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.service = TaskService()

    @patch('app.models.db.session')
    def test_create_task_success(self, mock_session):
        """Verify task creation calls the DB correctly [cite: 353, 363-364]"""
        task_data = {'title': 'New Task', 'priority': 'high'}
        result = self.service.create_task(user_id=1, data=task_data)
        
        self.assertEqual(result.title, 'New Task')
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()