import streamlit as st
import sqlite3

# Create a connection to the SQLite database
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

def login(username, password):
    # Query the database to check if the username and password combination exists
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone():
        return True
    else:
        return False

# Create some sample users
create_user_table()

# Streamlit UI
st.title('Mini Login Page')


username = st.text_input('Username')
password = st.text_input('Password', type='password')

if st.button('Login'):
    if login(username, password):
        st.success('Logged in successfully!')
    else:
        st.error('Incorrect username or password')
