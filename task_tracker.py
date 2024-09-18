import json
import datetime
import argparse
import os.path

TASK_FILE = "tasks.json"

def check_for_file():
    if not os.path.isfile(TASK_FILE):
        with open(TASK_FILE, "w") as file:
            json.dump([], file)

def load_file():
    with open(TASK_FILE, 'r') as file:
        if os.path.getsize(TASK_FILE) > 0:
            return json.load(file)
        return []

def save_file(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def generate_task_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(description):
    tasks = load_file()

    id = generate_task_id(tasks)
    status = 'todo'
    createdAt = datetime.datetime.now().isoformat()  # Convert datetime to string
    updatedAt = createdAt  # Use the same time for creation and update initially

    new_task = {
        "id": id,
        "description": description,
        "status": status,
        "createdAt": createdAt,
        "updatedAt": updatedAt
    }

    tasks.append(new_task)
    save_file(tasks)
    print(f"Task added successfully (ID: {id})")

def update_task(id, new_description):
    tasks = load_file()
    
    updatedAt = datetime.datetime.now().isoformat()

    for task in tasks:
        if task['id'] == id:
            task['description'] = new_description
            task['updatedAt'] = updatedAt
            save_file(tasks)
            print(f"Task ID {id} updated successfully.")
            return
        
    print(f"Error: Task with ID {id} not found.")

def delete_task(id):
    tasks = load_file()
    new_tasks = [task for task in tasks if task['id'] != id]
    
    if len(new_tasks) == len(tasks):
        print(f"Error: Task with ID {id} not found.")
    else:
        save_file(new_tasks)
        print(f"Task ID {id} deleted successfully.")

def mark_in_progress(id):
    tasks = load_file()

    updatedAt = datetime.datetime.now().isoformat()

    for task in tasks:
        if task['id'] == id:
            if task['status'] != 'in-progress':
                task['status'] = 'in-progress'
                task['updatedAt'] = updatedAt
                save_file(tasks)
                print(f"Task ID {id} marked as in-progress.")
            else:
                print(f"Task ID {id} is already in-progress.")
            return
    
    print(f"Error: Task with ID {id} not found.")

def mark_done(id):
    tasks = load_file()

    updatedAt = datetime.datetime.now().isoformat()

    for task in tasks:
        if task['id'] == id:
            if task['status'] != 'done':
                task['status'] = 'done'
                task['updatedAt'] = updatedAt
                save_file(tasks)
                print(f"Task ID {id} marked as done.")
            else:
                print(f"Task ID {id} is already done.")
            return
    
    print(f"Error: Task with ID {id} not found.")

def list_tasks(status=None):
    tasks = load_file()

    if status:
        filtered_tasks = [task for task in tasks if task['status'] == status]
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        print(f"No tasks found{' with status ' + status if status else ''}.")
        return
    
    for task in filtered_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, "
              f"Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")


def main():
    check_for_file()

    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    subparsers = parser.add_subparsers(dest='action')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('description', type=str, help='New description of the task')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')

    # Mark-in-progress command
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark a task as in-progress')
    mark_in_progress_parser.add_argument('id', type=int, help='Task ID')

    # Mark-done command
    mark_done_parser = subparsers.add_parser('mark-done', help='Mark a task as done')
    mark_done_parser.add_argument('id', type=int, help='Task ID')

    # List command
    list_parser = subparsers.add_parser('list', help='List all tasks or tasks with specific status')
    list_parser.add_argument('status', nargs='?', choices=['todo', 'in-progress', 'done'], help='Task status')


    args = parser.parse_args()

    if args.action == 'add':
        if args.description:
            add_task(args.description)
        else:
            print("Error: Task description is required.")

    elif args.action == 'update':
        if args.id and args.description:
            update_task(args.id, args.description)
        else: 
            print("Error: Task ID and description are required for updating a task.")

    elif args.action == 'delete':
        if args.id:
            delete_task(args.id)
        else: 
            print("Error: Task ID is required for deleting a task.")

    elif args.action == 'mark-in-progress':
        if args.id:
            mark_in_progress(args.id)
        else: 
            print("Error: Task ID is required for marking a task.")

    elif args.action == 'mark-done':
        if args.id:
            mark_done(args.id)
        else: 
            print("Error: Task ID is required for marking a task.")

    elif args.action == 'list':
        list_tasks(args.status)
       
       
if __name__ == "__main__":
    main()
