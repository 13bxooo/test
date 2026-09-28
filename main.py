import streamlit as st

st.set_page_config(
    page_title="PROJECT : LOGIC",
    page_icon="◈",
)

st.title("PROJECT : LOGIC")

st.write("INFORMATION IS NOT ALWAYS TRUE")

if st.button("START"):
    st.write("START MENU")

if st.button("HOW TO PLAY"):
    st.switch_page("pages/1_How_to_Play.py")
