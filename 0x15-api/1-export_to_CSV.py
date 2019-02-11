#!/usr/bin/python3
"""
Module for gathering employee information and exporting
data into CSV format
"""
import csv
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
    csv_todos = []
    for task in e_todos:
        new_dict = {}
        new_dict['username'] = name
        new_dict['user_id'] = int(eid)
        new_dict['task_completed_status'] = task['completed']
        new_dict['task_title'] = task['title']
        csv_todos.append(new_dict)

    # Exporting into CSV
    csv_columns = ['user_id',
                   'username',
                   'task_completed_status',
                   'task_title']
    csv_file = eid + '.csv'
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, csv_columns,
                                    quoting=csv.QUOTE_ALL)
            for data in csv_todos:
                writer.writerow(data)
    except IOError:
        print("I/O error")
