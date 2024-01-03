#!/usr/bin/python3
"""
    for a given employee ID, script returns information about
    his/her todo list progress and exports it to a json file
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{url}/{path}".format(url=base_url, path='users')
    user_res = requests.get(users_url).json()

    employee_data = {}
    for user in user_res:
        todos_res = requests.get("{users}/{id}/todos".format(
                                 users=users_url, id=user['id'])).json()
        data = []
        for item in todos_res:
            data.append({"username": "{}".format(user['name']),
                         "task": "{}".format(item['title']),
                         "completed": "{}".format(item['completed']),
                         })
        employee_data["{USER_ID}".format(USER_ID=user['id'])] = data

    file_name = 'todo_all_employees.json'
    file_data = {}
    with open(file_name, 'w') as json_file:
        json.dump(employee_data, json_file)
