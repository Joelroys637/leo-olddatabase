import streamlit as st
import sqlite3
import sigup as si

conn = sqlite3.connect('login.db')
c = conn.cursor()

# Create a table for storing user credentials if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
conn.commit()



def login(username, password):
    # Query the database to check if the username and password combination exists
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone():
        return True
    else:
        return False

si.create_user_table()
