import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from home import load_data


st.set_page_config(
    page_title="CNN JOB MON",
    layout="centered",
    page_icon=":smiley_cat:",
    initial_sidebar_state="expanded")

st.markdown("# STEP 2 ❄️")
st.sidebar.markdown("# STEP 2 ❄️")

st.title('요청자, 처리자 통계')
st.write("streamlit chart 사용")
        
data = load_data()
df = pd.DataFrame(data)


# A(request time) 열에 대해서 count
a_counts = df.groupby('request_time').size().reset_index(name='count')
a_counts['type'] = 'request_time'
a_counts.rename(columns={'request_time': 'date'}, inplace=True)

# B(prediction time) 열에 대해서 count
b_counts = df.groupby('prediction_time').size().reset_index(name='count')
b_counts['type'] = 'prediction_time'
b_counts.rename(columns={'prediction_time': 'date'}, inplace=True)

# A와 B count 데이터 합치기
result = pd.concat([a_counts, b_counts]).sort_values(by='date').reset_index(drop=True)
st.bar_chart(result, x="date", y="count", color="type")
st.line_chart(result, x="date", y="count", color="type")


# char2
result_df = df.groupby(['request_time', 'request_user']).size().reset_index(name='count')
st.bar_chart(result_df, x="request_time", y="count", color="request_user", horizontal=False, stack=False)
