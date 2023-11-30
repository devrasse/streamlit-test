import streamlit as st

st.set_page_config(layout='wide')
# HTML 파일을 읽어오기
with open("jeseolham.html", "r",  encoding="utf-8") as f:
    html_code = f.read()

# Stremlit 앱에 HTML 표시
st.components.v1.html(html_code, height=800, width = 1500, scrolling=False)
