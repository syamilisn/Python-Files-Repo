# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:01:20 2020

@author: shyam

To check if DB exists
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shy@m1l1"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)