import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests




st.set_page_config(
     page_title="CNN JOB MON",
     layout="centered",
     page_icon=":smiley_cat:",
    initial_sidebar_state="expanded")

st.markdown("# STEP 1 🎈")
st.sidebar.markdown("# STEP 1 🎈")

st.title('요청/처리 건수(h)')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

# TODO
# request_time, prediction_time 이용해 '%Y-%m-%d %H' 형식
# 즉 시간별 GROUPBY COUNT 하여 plt 차트 그려보기

df['request_time'] = pd.to_datetime(df['request_time']).dt.strftime('%Y-%m-%d %H')
time = df.groupby('request_time').size()

plt.title('Requests by Date and Time')
plt.bar(time.index, time.values)
plt.plot(time.index, time.values, marker='o', color='r')
plt.xlabel('Date and Time')  # x축 레이블
plt.ylabel('Count')  # y축 레이블
plt.xticks(rotation = 45)

# 화면에 그리기
st.pyplot(plt)