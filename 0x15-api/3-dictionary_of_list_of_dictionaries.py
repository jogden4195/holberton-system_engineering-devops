#!/usr/bin/python3
"""
Module for gathering all employee information and exporting
data into JSON format
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    # Getting all todos
    todos = requests.get(url + 'todos/')
    todos_dicts = todos.json()

    # Getting all employees
    employees = requests.get(url + 'users/')
    e_json = employees.json()

    # Getting list of employee's tasks and formatting dicts
    json_dict = {}
    for emp in e_json:
        eid = emp['id']
        name = emp['username']
        todos = requests.get(url + 'todos/')
        todos_dicts = todos.json()
        e_todos = [i for i in todos_dicts if i['userId'] == eid]
        json_todos = []
        for task in e_todos:
            new_dict = {}
            new_dict['username'] = name
            new_dict['completed'] = task['completed']
            new_dict['task'] = task['title']
            json_todos.append(new_dict)
            json_dict[str(eid)] = json_todos

    # Exporting to JSON
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as fp:
        json.dump(json_dict, fp)
