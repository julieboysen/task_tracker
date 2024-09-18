import unittest
import json
import os
import task_tracker

TASK_FILE = 'test_tasks.json' 

class TestTaskTracker(unittest.TestCase):

    def setUp(self):
        """Create a fresh tasks.json file before each test"""
        task_tracker.TASK_FILE = TASK_FILE
        with open(TASK_FILE, 'w') as f:
            json.dump([], f)


    def test_add_task(self):
        """Test adding a new task"""
        task_tracker.add_task("Test task")
        tasks = task_tracker.load_file()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "Test task")
        self.assertEqual(tasks[0]['status'], "todo")

    def test_update_task(self):
        """Test updating a task's description"""
        task_tracker.add_task("Original task")
        task_tracker.update_task(1, "Updated task")
        tasks = task_tracker.load_file()
        self.assertEqual(tasks[0]['description'], "Updated task")

    def test_delete_task(self):
        """Test deleting a task"""
        task_tracker.add_task("Task to delete")
        task_tracker.delete_task(1)
        tasks = task_tracker.load_file()
        self.assertEqual(len(tasks), 0)

    def test_mark_in_progress(self):
        """Test marking a task as in-progress"""
        task_tracker.add_task("Task to mark in-progress")
        task_tracker.mark_in_progress(1)
        tasks = task_tracker.load_file()
        self.assertEqual(tasks[0]['status'], "in-progress")

    def test_mark_done(self):
        """Test marking a task as done"""
        task_tracker.add_task("Task to mark done")
        task_tracker.mark_done(1)
        tasks = task_tracker.load_file()
        self.assertEqual(tasks[0]['status'], "done")

    def test_list_tasks(self):
        """Test listing tasks"""
        task_tracker.add_task("First task")
        task_tracker.add_task("Second task")
        tasks = task_tracker.load_file()
        self.assertEqual(len(tasks), 2)
    
    def test_list_todo_tasks(self):
        """Test listing tasks with status 'todo'"""
        task_tracker.add_task("First task")
        task_tracker.add_task("Second task")
        task_tracker.mark_done(1)
        todo_tasks = [task for task in task_tracker.load_file() if task['status'] == 'todo']
        self.assertEqual(len(todo_tasks), 1)
        self.assertEqual(todo_tasks[0]['description'], "Second task")

if __name__ == '__main__':
    unittest.main()