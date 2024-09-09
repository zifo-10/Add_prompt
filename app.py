import streamlit as st
from controller import insert


st.title("Add Prompt APP")

# MongoDB connection setup
st.sidebar.header("MongoDB Connection")
mongo_uri = st.sidebar.text_input("Enter MongoDB URI", placeholder="mongodb://localhost:27017/")
db_name = st.sidebar.text_input("Enter Database Name", placeholder="prompt database")
collection_name = "prompt"

# Establish MongoDB connection
if mongo_uri and db_name:
    user = st.text_area("Enter User Prompt", height=100)
    system = st.text_area("Enter System Prompt", height=150)
    name = st.text_input("Enter Prompt Name")
    if st.button("Add Prompt"):
        if user == "":
            st.error("User Field Required")
        elif system == "":
            st.error("System Field Required")
        else:
            insert_prompt = insert(mongo_uri, db_name, user, system, name)
            if insert_prompt:
                st.success("Prompt added to the collection!")
            else:
                st.error("Failed to add prompt please check the connection")
else:
    st.sidebar.warning("Please enter MongoDB URI and Database Name to continue")
