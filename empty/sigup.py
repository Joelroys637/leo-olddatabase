import streamlit as st
import sqlite3

conn = sqlite3.connect('login.db')
c = conn.cursor()

# Create a table for storing user credentials if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
conn.commit()

def create_user_table():
    # Insert some dummy users for testing
   
    user=st.text_input('username')
    password1=st.text_input('password')

   

    
    c.execute("INSERT INTO users VALUES (?, ?)", (user,password1))
        

    conn.commit()


