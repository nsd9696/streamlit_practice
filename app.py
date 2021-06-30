import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import gspread
from oauth2client.client import GoogleCredentials
from oauth2client.service_account import ServiceAccountCredentials
def load_works(name):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    json_file_name = 'streamlit-practice-588d79fd6ab5.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
    gc = gspread.authorize(credentials)
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/1fJESPUhqvoMJH916zbY-5nkxO9GPwMJyIztDZe14yL0/edit#gid=0"
    # 스프레스시트 문서 가져오기
    doc = gc.open_by_url(spreadsheet_url)
    # 시트 선택하기
    ws = doc.worksheet('work')

    # get_all_values gives a list of rows.
    rows = ws.get_all_values()

    # Convert to a DataFrame and render.
    df = pd.DataFrame.from_records(rows)
    header = df.iloc[0]
    df = df[1:]

    df = df.rename(columns=header)
    return list(df[name].values)

def load_name():
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    json_file_name = 'streamlit-practice-588d79fd6ab5.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
    gc = gspread.authorize(credentials)
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/1fJESPUhqvoMJH916zbY-5nkxO9GPwMJyIztDZe14yL0/edit#gid=0"
    # 스프레스시트 문서 가져오기
    doc = gc.open_by_url(spreadsheet_url)
    # 시트 선택하기
    ws = doc.worksheet('workers')

    # get_all_values gives a list of rows.
    rows = ws.get_all_values()
    return [i[0] for i in rows]
# @st.cache
def load_work_frame(name):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    json_file_name = 'streamlit-practice-588d79fd6ab5.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
    gc = gspread.authorize(credentials)
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/1fJESPUhqvoMJH916zbY-5nkxO9GPwMJyIztDZe14yL0/edit#gid=0"
    # 스프레스시트 문서 가져오기
    doc = gc.open_by_url(spreadsheet_url)
    # 시트 선택하기
    ws = doc.worksheet(name)
    # get_all_values gives a list of rows.
    rows = ws.get_all_values()

    # Convert to a DataFrame and render.
    df = pd.DataFrame.from_records(rows)
    header = df.iloc[0]
    df = df[1:]

    df = df.rename(columns=header)
    return df

name_list = load_name()
st.title("Smartmind KPI")
st.header("일일업무 보고")
name= st.selectbox(label="이름", options=tuple(name_list))
work_frame = load_work_frame(name)
work_frame = work_frame.set_index('날짜')
st.line_chart(work_frame)
date = st.date_input("Date input")

work_list = load_works("남상대")
work_num = int(len(work_list))
cols = st.beta_columns(work_num)

with st.form(key="work_report"):
    work_name_list = []
    work_time_list = []
    for i in range(work_num):
        with cols[i]:
            work_name=st.header(work_list[i])
            work_name_list.append(str(work_name))
            work_time = st.time_input(label="업무시간",key=i)
            work_content = st.text_input(label="업무내용",key=i)
            work_status = st.radio(label="업무진행상황",options=("시작전","진행중","완료"),key=i)
            work_percent = st.number_input(label="진행율",key=i)
            work_contrib = st.number_input(label="기여율",key=i)
    submitted = st.form_submit_button("submit")





# def show_checkboxes(containers, q_no):
#     containers[0].checkbox("Answer 1", value=False, key=f"q{q_no}_1")
#     containers[1].checkbox("Answer 2", value=False, key=f"q{q_no}_2")
#     containers[2].checkbox("Answer 3", value=False, key=f"q{q_no}_3")
#     containers[3].checkbox("Answer 4", value=False, key=f"q{q_no}_4")
#     containers[4].checkbox("Answer 5", value=False, key=f"q{q_no}_5")
#
#
# question_number = 1
# containers = [st.empty(), st.empty(), st.empty(), st.empty(), st.empty()]
#
# show_checkboxes(containers, question_number)
#
# if st.button("Submit"):
#     question_number += 1
#     show_checkboxes(containers, question_number)
