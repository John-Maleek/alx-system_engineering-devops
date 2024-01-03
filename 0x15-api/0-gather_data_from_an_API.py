#!/usr/bin/python3
"""
    for a given employee ID, script returns information about 
    his/her todo list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{url}/{path}/{id}".format(url=base_url, path='users', id=int(argv[1]))
    user_res = requests.get(users_url).json()
    todos_res = requests.get("{users}/todos".format(users=users_url)).json()
    
    def get_tasks_done():
        count = 0
        for item in todos_res:
            if item['completed'] == True:
                count = count + 1
        return count
    
    print("Employee {EMPLOYEE_NAME} is done with \
          tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})\
          :".format(EMPLOYEE_NAME= user_res['name'],
                    NUMBER_OF_DONE_TASKS=get_tasks_done(),
                    TOTAL_NUMBER_OF_TASKS=len(todos_res) ))
    
    for item in todos_res:
        if item['completed'] == True:
            print('\t {TASK_TITLE}'.format(TASK_TITLE=item['title']))
