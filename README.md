# Task Tracker

A command-line interface (CLI) application for managing tasks. This project allows you to add, update, delete, and track the status of tasks using a JSON file for storage.

## Features

- **Add a Task:** Create a new task with a description.
- **Update a Task:** Modify the description of an existing task.
- **Delete a Task:** Remove a task by its ID.
- **Mark a Task as In-Progress:** Change the status of a task to "in-progress".
- **Mark a Task as Done:** Change the status of a task to "done".
- **List Tasks:** View tasks with optional filtering by status (todo, in-progress, done).

## Requirements

- Python 3
- `argparse` (standard library)
- `json` (standard library)
- `datetime` (standard library)
- `os` (standard library)

## Setup

1. Clone this repository:
   ```sh
   git clone https://github.com/julieboysen/task_tracker.git
2. Naviagte to project directory
    ```sh
     cd task_tracker
## Usage
### Adding a task
    python3 task_tracker.py add "Task description"
### Updating a task
    python3 task_tracker.py update <task_id> "New task description"
### Deleting a task
    python3 task_tracker.py delete <task_id>
### Marking a task as in-progress
    python3 task_tracker.py mark-in-progress <task_id>
### Marking a task as done
    python3 task_tracker.py mark-done <task_id>
### Listing all tasks
    python3 task_tracker.py list
### Listing tasks by staus
```sh
python3 task_tracker.py list
```
#### Done tasks:
```sh
python3 task_tracker.py list done
```
#### To-do tasks:
```sh
python3 task_tracker.py list todo
```
#### In-progress tasks:
```sh
python3 task_tracker.py list in-progress
```

## Testning
Unit test are also included and can be run by:
```sh
python3 test_task_tracker.py
```

## Project Link
For more details about this project, visit the [Task Tracker Project](https://roadmap.sh/projects/task-tracker).
