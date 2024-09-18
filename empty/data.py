import streamlit as st
import pymysql

# Connect to MySQL database
conn = pymysql.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_database',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Function to check if username exists and password matches
def login(username, password):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(sql, (username, password))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False

# Function to add user to database
def add_user(username, password):
    with conn.cursor() as cursor:
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(sql, (username, password))
        conn.commit()

# Page title
st.title("Mini Login Page")

# Input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Check if user exists in database and password matches
if st.button("Login"):
    if login(username, password):
        st.success("Login successful!")
    else:
        st.error("Invalid username or password. Please try again.")

# Option to register a new user
if st.button("Register"):
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if new_username and new_password:
        add_user(new_username, new_password)
        st.success("User registered successfully!")
