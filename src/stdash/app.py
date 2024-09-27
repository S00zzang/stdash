import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

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
# 즉 시간별  GROUP BY COUNT 하여 plt 차트 그려보기
df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time'] = df['request_time'].dt.strftime('%Y-%m-%d %H')
time = df.groupby('request_time').size()

plt.bar(time.index, time.values)
plt.plot(time.index, time.values, marker='o', color='r')
plt.title("Requests by Date and Time")
plt.xlabel('Date and Time') # X축 레이블
plt.ylabel('Number of Requests') # Y축 레이블
plt.xticks(rotation = 45)

st.pyplot(plt)
