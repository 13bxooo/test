import base64
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="PROJECT : LOGIC // HOW TO PLAY",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

font_data = ""
for candidate in (Path("neodgm.ttf"), Path("neodgm(2).ttf")):
    if candidate.exists():
        font_data = base64.b64encode(
            candidate.read_bytes()
        ).decode("ascii")
        break

st.markdown(f"""
<style>
@font-face {{
    font-family:Neo;
    src:url(data:font/ttf;base64,{font_data}) format('truetype');
}}
#MainMenu,header,footer,[data-testid=stSidebar] {{
    display:none;
}}
.stApp {{
    background:#000;
    color:#eee;
    font-family:Neo,monospace;
}}
.block-container {{
    max-width:760px;
    padding-top:10vh;
}}
button {{
    font-family:Neo,monospace!important;
    background:#000!important;
    color:#fff!important;
    border:1px solid #555!important;
    border-radius:0!important;
}}
</style>
""", unsafe_allow_html=True)

st.markdown("# PROJECT : LOGIC")
st.markdown("### HOW TO PLAY // SYSTEM MANUAL")

st.markdown("""
- 이동: **W A S D** 또는 모바일 방향 버튼
- 조사 / 상호작용: **E** 또는 화면의 **INTERACT** 버튼
- 대사: **SPACE**를 누르면 현재 출력 중인 문장만 완성됩니다. 필수 행동은 건너뛸 수 없습니다.
- 일시정지: 화면 오른쪽 위의 **Ⅱ** 버튼
- 단말기 기록과 보관 기록의 단서를 모아 보안 패널 코드를 찾으세요.
""")

if st.button("RETURN TO TITLE", use_container_width=True):
    st.switch_page("main.py")

if st.button("START TUTORIAL", use_container_width=True):
    st.session_state.game_started = True
    st.switch_page("pages/2_Game.py")
