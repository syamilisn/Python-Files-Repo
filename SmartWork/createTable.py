# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:17:32 2020

@author: shyam

create table, insert values
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shy@m1l1",
  database="hopeDB"
)

mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE konosuba2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
#mycursor.execute("DROP TABLE konosuba")
sql = "INSERT INTO konosuba (name) VALUES (%s)"
#sql="insert into konosuba (name) values (Darkness)"
val = ["Megumin","Aqua","Darkness","Kazuma"]
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")