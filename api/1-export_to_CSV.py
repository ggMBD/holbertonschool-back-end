#!/usr/bin/python3
"""
api : first use
"""
import csv
import requests
import sys


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    api_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{api_url}/users/{employee_id}")
    user_data = user_response.json()

    todos_response = requests.get(f"{api_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    employee_name = user_data.get('name')

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for task in todos_data:
            csv_writer.writerow(
                [employee_id, employee_name, task['completed'], task['title']])
