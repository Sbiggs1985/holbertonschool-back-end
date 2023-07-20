#!/usr/bin/python3

import requests


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = f'{base_url}/{employee_id}/todos'

    response = requests.get(todo_url)

    if response.status_code != 200:
        print(f"Error: Could not fetch data for employee ID {employee_id}")
        return

    todos = response.json()
    employee_name = todos[0]['username']
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])

    print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")

    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
