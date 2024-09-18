import streamlit as st
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS dataform (Name TEXT, Age TEXT)''')
conn.commit()

def create_dataform_table():
        
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    name=st.text_input('Name')
    age=st.text_input('Age')
    c.execute("INSERT INTO dataform VALUES (?, ?)", (name,age))
    
    if st.button('submite'):
            
        conn.commit()
    
create_dataform_table()
