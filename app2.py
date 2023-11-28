import streamlit as st
import json
from streamlit_lottie import st_lottie
import requests
from PIL import Image

#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
#https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = "종호의 웹페이지", page_icon="🐧",layout="wide")

#https://lottiefiles.com

def load_lottiefile(filepath):
    with open(filepath, "r", encoding='utf-8') as f:
        return json.load(f)
    
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_cat = load_lottiefile("lottiefiles/cat.json")
lottie_dragon = load_lottieurl("https://lottie.host/c20e742c-4143-4199-a71b-fbe14d03e8f7/u1FZwLwtxL.json")
image_form = Image.open("images/images.jpg")


with st.container():
    st.subheader("안녕, 나는 종호야 :wave:")
    st.title("도화1동 직원")
    st.write("나는 시호,시은이 아빠야")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("나는 누굴까?")
        st.write("##")
        st.write(
        """
        djaklfjal;fj;jaa;jfk;a
        alfj;ajklajlfja;lj;
        -ajlfajlfaj
        -akjfaljfdklajlf

        -ajflajfklajflajlfjlk
        """
        )
        st.write("[home page >](https://naver.com)")

    with right_column:
        st_lottie(lottie_dragon, height=300, key='cat')

    with st.container():
        st.write('----')
        st.header("종호 프로젝트")
        st.write("##")
        image_column, text_column = st.columns((1,2))

        with image_column:
            st.image(image_form)
        with text_column:
            st.write(
            """
            에펠탑
            """
            )
            st.markdown("[home page...](https://naver.com)")

#https://formsubmit.co/
with st.container():
    st.write("---")
    st.header("날 눌러줘")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/decrasse9001@gmail.com" method="POST">
        <input type = "hidden" name="_captcha" value = 'false'>
        <input type="text" name="name" placeholder = "baek jongho" required>
        <input type="email" name="email" placeholder = "decrasse9001@gmail.com" required>
        <textarea name="message" placeholder = "your message" required></textarea>
        <button type="submit">Send</button>
</form>
"""


left_column, right_column = st.columns(2)

with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)

with right_column:
    st.empty()