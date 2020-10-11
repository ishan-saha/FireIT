#!/usr/bin/env python3
import sqlite3,os

database =os.path.join(os.path.dirname(os.path.abspath(__file__)),"Stats.db")
connection = sqlite3.connect(database)
query="""CREATE TABLE IF NOT EXISTS owner (number TEXT PRIMARY KEY,name TEXT, address TEXT, location TEXT)"""
cur=connection.cursor()
cur.execute(query)
query="""CREATE TABLE IF NOT EXISTS Logs (DateTime TEXT PRIMARY KEY, Temperature TEXT, Humidity TEXT)"""
cur.execute(query)
query="""CREATE TABLE IF NOT EXISTS Extension (module TEXT PRIMARY KEY)"""
cur.execute(query)
connection.commit()