#!/usr/bin/python3
"""
    for a given employee ID, script returns information about
    his/her todo list progress and exports it to a csv file
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{url}/{path}/{id}".format(url=base_url, path='users',
                                           id=user_id)
    user_res = requests.get(users_url).json()
    todos_res = requests.get("{users}/todos".format(users=users_url)).json()

    data = []
    for item in todos_res:
        data.append(["{}".format(user_id),
                     "{}".format(user_res['name']),
                     "{}".format(item['completed']),
                     "{}".format(item['title'])])

    with open("{USER_ID}.csv".format(USER_ID=user_id), 'w',
              encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)
