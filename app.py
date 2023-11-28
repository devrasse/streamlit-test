import streamlit as st

st.set_page_config(layout='wide')
# HTML 파일을 읽어오기
with open("jeseol.html", "r",  encoding="utf-8") as f:
    html_code = f.read()

# Stremlit 앱에 HTML 표시
st.components.v1.html(html_code, height=800, width = 1000, scrolling=False)
