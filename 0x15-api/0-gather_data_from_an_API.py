#!/usr/bin/python3
""" Module for gathering employee information """
import requests
import sys


if __name__ == "__main__":
    eid = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    # Getting employee name
    employees = requests.get(url + 'users/' + eid)
    e_json = employees.json()
    name = e_json['name']

    # Getting list of employee's completed tasks
    todos = requests.get(url + 'todos/')
    todos_dicts = todos.json()
    e_todos = [i for i in todos_dicts if i['userId'] == int(eid)]
    total = len(e_todos)
    done = [i for i in e_todos if i['completed'] is True]

    # Printing message
    print('Employee {} is done with tasks({}/{}):'.format(
          name, len(done), total))
    for task in done:
        print('\t ' + task['title'])
