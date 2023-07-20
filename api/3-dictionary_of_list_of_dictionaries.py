#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests
import sys


def record_all_tasks():
    """gather and print api data"""

    user_data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    counter = 0
    task_list = []
    complete_status_list = []
    username_list = []

    for item in user_data:
        username_list.append(item.get("username"))

    for item in todo_data:
        if item.get("userId") > counter:
            counter += 1
        task_list.append(item.get("title"))
        complete_status_list.append(item.get("completed"))

    
    todo_list = []
    for i in range(1, counter + 1):
        todo_list.append(requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={"userId": i}).json())

    json_dict = {}
    counter = 0
    for each in todo_list:
        json_list = []
        for i in range(len(todo_list)):
            new_dict = {
                    "username": username_list[counter],
                    "task": task_list[i],
                    "completed": complete_status_list[i],
            }
            json_list.append(new_dict)
        json_dict[f'{counter}'] = json_list
        counter += 1

    json_object = json.dumps(json_dict)

    with open('todo_all_employees.json', 'w') as f:
        f.write(json_object)


if __name__ == "__main__":
    record_all_tasks()
