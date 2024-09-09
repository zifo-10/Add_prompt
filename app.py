import streamlit as st
from controller import insert

# Streamlit app
st.title("MongoDB Streamlit App")

# MongoDB connection setup
st.sidebar.header("MongoDB Connection")
mongo_uri = st.sidebar.text_input("Enter MongoDB URI", placeholder="mongodb://localhost:27017/")
db_name = st.sidebar.text_input("Enter Database Name", value="testdb")
collection_name = "prompt"

# Establish MongoDB connection
if mongo_uri and db_name:
    user = st.text_input("Enter your name", "prompt user")
    system = st.text_input("Enter system name", "prompt system")
    name = st.text_input("Enter name", "prompt name")
    if st.button("Add Prompt"):
        insert_prompt = insert(mongo_uri, db_name, user, system, name)
        if insert_prompt:
            st.success("Prompt added to the collection!")
        else:
            st.error("Failed to add prompt please check the connection")
else:
    st.sidebar.warning("Please enter MongoDB URI and Database Name")
