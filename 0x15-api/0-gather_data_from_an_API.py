#!/usr/bin/python3
"""
    for a given employee ID, script returns information about
    his/her todo list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{url}/{path}/{id}".format(url=base_url, path='users',
                                           id=int(argv[1]))
    user_res = requests.get(users_url).json()
    todos_res = requests.get("{users}/todos".format(users=users_url)).json()

    def get_tasks_done():
        count = 0
        for item in todos_res:
            if item['completed']:
                count = count + 1
        return count

    print("Employee {name} is done with tasks({done}/{total}:"
          .format(name=user_res['name'],
                  done=get_tasks_done(),
                  total=len(todos_res)))

    for item in todos_res:
        if item['completed']:
            print('\t {TASK_TITLE}'.format(TASK_TITLE=item['title']))
