# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:14:30 2020

@author: shyam

create database
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shy@m1l1"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE hopeDB")