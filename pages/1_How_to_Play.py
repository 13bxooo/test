import streamlit as st

st.set_page_config(
    page_title="HOW TO PLAY",
    page_icon="◈",
)

st.title("HOW TO PLAY")

st.write("PROJECT : LOGIC")

st.write("WASD : 이동")
st.write("E : 상호작용")
st.write("I : 인벤토리")
st.write("SPACE : 대화 진행")
st.write("ESC : 메뉴 닫기")

if st.button("BACK TO TITLE"):
    st.switch_page("main.py")
