# import streamlit as st

# # HTML 파일을 읽어오기
# with open("./a.html", "r", encoding="utf-8") as f:
#     html_code = f.read()
# st.markdown(
#     """
#     <script>
#         const width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
#         const height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

#     </script>
#     """,
#     unsafe_allow_html=True
# )
# # Streamlit 앱에 HTML 표시
# st.components.v1.html(html_code,  width = window.innerWidth, height= window.innerHeight, scrolling=True)

import streamlit as st

# HTML 파일을 읽어오기
with open("./a.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Streamlit 앱에 HTML 표시
st.components.v1.html(html_code, scrolling=True)

# Streamlit 앱에 JavaScript 추가
st.markdown(
    """
    <script>
        // 창 크기 변경 이벤트를 감지하고 body 크기를 조정하는 함수
        function adjustBodySize() {
            const width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
            const height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
            document.body.style.width = `${width}px`;
            document.body.style.height = `${height}px`;
        }

        // 페이지 로드 시 초기 조정 실행
        adjustBodySize();

        // 창 크기가 변경될 때마다 조정 실행
        window.addEventListener('resize', adjustBodySize);
    </script>
    """,
    unsafe_allow_html=True
)
