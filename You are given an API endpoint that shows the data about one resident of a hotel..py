'''
You are given an API endpoint that shows the data about one resident of a hotel. Part of your task will be to make a GET request to receive a JSON-formatted response containing the first name and last name of the resident in the following format:

{
  "residentFirstName": "Lisa",
  "residentLastName": "Carter"
}
You are also given a table residents in a MySQL database that contains data about each resident of the hotel, where each row contains residentFirstName, residentLastName, and room fields. The value of room is a string representing the hotel room where the person is registered.

Your task is to fetch from the database and print to the standard output the room of the resident whose name was received from the API call. Print "Many rooms." if there are multiple rows found for the same first name and last name, and "No rooms." if there are no rooms found under this name.

API credentials

API endpoint for the GET request http://localhost/residentInfo.
Database credentials

Host: db;
Username: test;
Password: empty (no password);
Database name: ri_db.
Note: if using Java to solve, the following libraries are available to be imported in addition to the JDK standard library:

libjackson2-core-java;
libjackson2-databind-java;
libmysql-java.
Example

For the following table residents

id	residentFirstName	residentLastName	room
1	Lisa	Carter	Room No. 015
2	Michael	Butler	Room No. 022
3	Michael	Rogers	Room No. 103
And the following response from the API

{
  "residentFirstName": "Michael",
  "residentLastName": "Rogers"
}
Room No. 103 should be printed to the standard output stream.

[execution time limit] 10 seconds (py3)
'''

from multiprocessing import connection
import requests
import pymysql
import json

import pandas as pd

#make api request
url = 'http://localhost/residentInfo'

def makeConnectionforDB():
    connection = pymysql.connect(host='db',
                                 user='test',
                                 password='',
                                 db='ri_db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def makeAPIRequest(url):
    response = requests.get(url)
    if response.status_code == 200:
        res = response.json()
        # print(res)
        
        connection = makeConnectionforDB()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM residents WHERE residentFirstName = %s AND residentLastName = %s"
            cursor.execute(sql, (str(res['residentFirstName']), str(res['residentLastName'])))
            result = cursor.fetchall()
            connection.close()
            if len(result) >1:
                print("Many rooms.")
            if len(result) ==1:
                print(result[0].get('room'))
            else:
                print("No rooms.")
    else:
        return None
        
makeAPIRequest(url)

