'''
You are given an API endpoint that shows data about purchases in the market. The prices for products are given in international currency, and you'll need to convert the price of the purchase to internal currency. But the market is changing very fast, so you need to find out the currency exchange rate in the market at the time of the purchase.

So your task is divided into 2 parts:

Using the provided REST API, get information about the purchase.
Using the market currency exchange, find the exchange rate for the purchase and convert the purchase price into internal currency.
For the first subtask, perform a GET request to receive a JSON-formatted response containing the product name, product price in the international currency, and timestamp when the purchase was made in the market, in the following format:

{
  "productName": "product1",
  "productPrice": 100,
  "timestamp" : 1552122500
}
For the second subtask you are given a table currency in a MySQL database that contains information about each market exchange rate change. The table contains the following columns:

timestamp, an integer column containing the timestamp of the change;
exchangeRate, an integer column containing the rate for converting international currency into internal.
For example, a row with timestamp = 1552122000 and exchangeRate = 20 means that starting from time 1552122000 (inclusively), each international currency unit can be converted to 20 internal currency units. So, if the purchase was made for 100 international units, you will need to pay 2000 internal currency units for the purchase.

Your task is to find the sum you need to pay, in internal currency units.

API credentials

API endpoint for the GET request: http://localhost/marketPurchase.
Database credentials

Host: db;
Username: test;
Password: empty (no password);
Database name: ri_db.
Note: if you are solving this task in JavaScript use the request module for HTTP calls.
Note: if you are solving this task in C# use the WebClient module for HTTP calls.

Example

For the following table currency

timestamp	exchangeRate
1552122000	10
1552125600	20
1552129200	30
And the following response from the API

{
  "productName": "product1",
  "productPrice": 100,
  "timestamp" : 1552122600
}
1000 should be printed to the standart output.

The purchase was made at timestamp = 1552122600. According to the market currency table, the exchange rate had changed to 10 at timestamp = 1552122000. The next change happens at timestamp = 1552125600, but the purchase happened before this, so it was made with purchaseRate = 10, so the answer is 100 * 10 = 1000.

[execution time limit] 12 seconds (py3)

'''



from multiprocessing import connection
import requests
import pymysql
import json

import pandas as pd

url = 'http://localhost/marketPurchase'

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
            sql = "SELECT * FROM currency WHERE timestamp <= %s ORDER BY timestamp DESC LIMIT 1"
            cursor.execute(sql, (str(res['timestamp'])))
            result = cursor.fetchall()
            connection.close()

            print(res['productPrice'] * result[0].get('exchangeRate'))

    else:
        return None
        
makeAPIRequest(url)