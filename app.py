from dotenv import load_dotenv
load_dotenv()#load all env veriables
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load GOOGLE gemini model and provid sql query
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

#function to retrive query from sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows

#Prompt for gem-pro model

prompt=["""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """]

#streamlit app

st.set_page_config(page_title='Retrive any sql query')
st.header("gemini app to retrive sql data")
question=st.text_input("input: ",key="input")
submit=st.button("ASK THE QUERY")

#if submit clicked

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader('response is')
    for row in data:
        print(row)
    st.header(row)