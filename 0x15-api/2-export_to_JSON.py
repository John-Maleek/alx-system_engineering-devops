#!/usr/bin/python3
"""
    for a given employee ID, script returns information about 
    his/her todo list progress and exports it to a json file
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{url}/{path}/{id}".format(url=base_url, path='users', id=user_id)
    user_res = requests.get(users_url).json()
    todos_res = requests.get("{users}/todos".format(users=users_url)).json()

    data = []
    for item in todos_res:
        data.append({"task": "{}".format(item['title']),
                     "completed": "{}".format(item['completed']),
                     "username": "{}".format(user_res['name']),
                     })

    file_name = "{USER_ID}.json".format(USER_ID=user_id)
    file_data = {}
    file_data["{USER_ID}".format(USER_ID=user_id)] = data
    with open(file_name, 'w') as json_file:
        json.dump(file_data, json_file)