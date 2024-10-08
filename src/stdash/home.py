import streamlit as st
import pandas as pd
import requests
from PIL import Image

st.set_page_config(
     page_title="CNN JOB MON",
     layout="centered",
     page_icon=":smiley_cat:",
    initial_sidebar_state="expanded")

st.markdown("# 🖼️ 이미지 처리 프로그램")
st.sidebar.markdown("# Home")

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

st.header("")
img = Image.open('img/home.jpeg')

st.image(img, width = 700)
