import streamlit as st

# HTML 파일을 읽어오기
with open("./jeseul.html", "r",  encoding="utf-8") as f:
    html_code = f.read()

# Stremlit 앱에 HTML 표시
st.components.v1.html(html_code, height=2000,width = 3000, scrolling=False)
