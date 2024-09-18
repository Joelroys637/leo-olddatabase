import streamlit as st

import json

user={'leo':'123','joel':'1234'}
st.title("login page")
def load_dict(filename):
    try:
        with open(filename,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return{}



def save_dict(data,filename):
    with open(filename,'w') as file:
        json.dump(data,file)

filename='data.json'
my_dict=load_dict(filename)

k=st.text_input("Enter a email :")
v=st.text_input("Enter a value :")
my_dict['k']='v'
save_dict(my_dict,filename)

email=st.text_input("User ID")
password=st.text_input("password")


button=st.button("login")
for user_email,user_password in user.items():
    if button and email==user_email and password==user_password:
        
        st.success("login successful")
if button:
    st.error("fail")
       
  
