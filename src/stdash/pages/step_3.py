import streamlit as st
import requests


st.markdown("# STEP 3 ☘︎")
st.sidebar.markdown("# STEP 3 ☘︎")

st.title('숫자 이미지 파일 업로드')
        
def upload_file():
    file = st.file_uploader('숫자 이미지 업로드', type=['png', 'jpg', 'jpeg'])

    if file is not None:
        label = file.name.split('_')[0]
        url = f'http://localhost:8000/uploadfile?label={label}'
        files = {"file": (file.name, file.getvalue(), file.type)}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            st.success("이미지 업로드 성공")
            st.write(response.json())

        else:
            st.error(f"이미지 업로드 실패: {response.status_code}")
            st.write(response.text)
    else:
        st.warning("파일을 업로드 해주세요.")

upload_file()

