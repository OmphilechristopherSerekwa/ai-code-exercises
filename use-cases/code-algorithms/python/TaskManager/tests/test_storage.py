import csv
import os
import tempfile
import unittest

from models import Task, TaskPriority
from storage import TaskStorage


class TaskStorageExportTest(unittest.TestCase):
    def test_export_tasks_to_csv_creates_file_with_expected_headers(self):
        task = Task("Test Task", "Description", TaskPriority.HIGH)
        task.due_date = None
        task.tags = ["work", "urgent"]

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = os.path.join(tmpdir, "tasks.csv")
            storage = TaskStorage(storage_path=os.path.join(tmpdir, "tasks.json"))
            storage.tasks = {task.id: task}

            result = storage.export_tasks_to_csv(output_path)

            self.assertTrue(result)
            self.assertTrue(os.path.exists(output_path))

            with open(output_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.assertEqual(reader.fieldnames, [
                    'id', 'title', 'description', 'status', 'priority',
                    'due_date', 'created_at', 'updated_at', 'completed_at', 'tags'
                ])
                rows = list(reader)
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0]['title'], 'Test Task')
                self.assertEqual(rows[0]['status'], task.status.value)
                self.assertEqual(rows[0]['priority'], task.priority.name)
                self.assertEqual(rows[0]['tags'], 'work,urgent')


if __name__ == '__main__':
    unittest.main()
