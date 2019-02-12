#!/usr/bin/python3
"""
Module for gathering employee information and exporting
data into JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    eid = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    # Getting employee's username
    employees = requests.get(url + 'users/' + eid)
    e_json = employees.json()
    name = e_json['username']

    # Getting list of employee's tasks and formatting dicts into list
    todos = requests.get(url + 'todos/')
    todos_dicts = todos.json()
    e_todos = [i for i in todos_dicts if i['userId'] == int(eid)]
    json_todos = []
    for task in e_todos:
        new_dict = {}
        new_dict['username'] = name
        new_dict['completed'] = task['completed']
        new_dict['task'] = task['title']
        json_todos.append(new_dict)
    json_dict = {}
    json_dict[eid] = json_todos
    # Exporting to JSON
    filename = eid + '.json'
    with open(filename, 'w') as fp:
        json.dump(json_dict, fp)
