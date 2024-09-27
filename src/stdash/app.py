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

df['request_time'] = pd.to_datetime(df['request_time']).dt.floor('30min')
df['prediction_time'] = pd.to_datetime(df['prediction_time']).dt.floor('30min')

r_hourly_counts = df.groupby('request_time').size()
p_hourly_counts = df.groupby('prediction_time').size()


plt.bar(r_hourly_counts.index, r_hourly_counts.values, label='request', width=0.015)
plt.plot(p_hourly_counts.index, p_hourly_counts.values, color='red', marker='o', label='prediction')

plt.title('request & prediction per hour')

plt.ylabel('count')
plt.xticks(rotation=45)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H'))

# 화면에 그리기
st.pyplot(plt)
