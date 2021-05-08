# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:11:59 2020

@author: shyam

connect database
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shy@m1l1",
  database="vintage"
)