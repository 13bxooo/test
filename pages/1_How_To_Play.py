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
@font-face {{font-family:Neo;src:url(data:font/ttf;base64,{font_data}) format('truetype');}}
#MainMenu,header,footer,[data-testid=stSidebar],[data-testid=stToolbar],.stDeployButton,#stDecoration {{display:none!important;visibility:hidden!important}}
.stApp {{background:#020609;color:#f4f8fa;font-family:Neo,monospace}}
.block-container {{max-width:1040px;padding:clamp(24px,6vh,64px) clamp(18px,5vw,60px) 48px!important}}
.manual-shell {{border:1px solid #26dfff;padding:clamp(20px,4vw,42px);background:linear-gradient(135deg,#06121b,#020609 65%);box-shadow:0 0 0 1px #0a3d4a,0 0 24px #00dfff18}}
.manual-kicker {{font-size:12px;letter-spacing:3px;color:#38e5ff;margin-bottom:14px}}
.manual-title {{font-size:clamp(25px,4vw,42px);letter-spacing:2px;margin:0 0 8px;color:#fff}}
.manual-subtitle {{font-size:clamp(13px,2vw,18px);color:#75eaff;margin:0 0 28px;letter-spacing:1px}}
.manual-rule {{height:1px;background:linear-gradient(90deg,#25e8ff,transparent);margin:18px 0 24px}}
.manual-list {{display:grid;gap:12px}}
.manual-row {{display:grid;grid-template-columns:150px 1fr;gap:18px;padding:12px 14px;border:1px solid #17404c;background:#041018;line-height:1.8;font-size:clamp(12px,1.5vw,15px)}}
.manual-key {{color:#52eaff;letter-spacing:1px}}
div.stButton>button {{font-family:Neo,monospace!important;border:1px solid #27dfff!important;border-radius:0!important;background:#03090d!important;color:#fff!important;min-height:46px!important;letter-spacing:1px}}
div.stButton>button:hover {{background:#fff!important;color:#000!important;border-color:#fff!important}}
@media(max-width:600px) {{.manual-row{{grid-template-columns:1fr;gap:4px}}}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="manual-shell">
  <div class="manual-kicker">PROJECT : LOGIC // FACILITY CONTROL SYSTEM</div>
  <h1 class="manual-title">HOW TO PLAY</h1>
  <div class="manual-subtitle">SYSTEM MANUAL / FIELD OPERATIONS</div>
  <div class="manual-rule"></div>
  <div class="manual-list">
    <div class="manual-row"><div class="manual-key">MOVEMENT</div><div>W A S D 또는 화면의 방향 버튼으로 이동합니다.</div></div>
    <div class="manual-row"><div class="manual-key">INTERACT</div><div>E 또는 화면의 INTERACT 버튼으로 주변 장치와 상호작용합니다.</div></div>
    <div class="manual-row"><div class="manual-key">DIALOGUE</div><div>SPACE를 누르면 현재 출력 중인 문장이 완성됩니다. 필수 행동은 건너뛸 수 없습니다.</div></div>
    <div class="manual-row"><div class="manual-key">PAUSE</div><div>화면 오른쪽 위의 Ⅱ 버튼으로 일시정지 메뉴를 엽니다.</div></div>
    <div class="manual-row"><div class="manual-key">OBJECTIVE</div><div>단말기 기록과 보관 기록에서 단서를 모아 보안 패널의 코드를 찾으세요.</div></div>
  </div>
</div>
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
