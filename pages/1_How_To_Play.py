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
        font_data = base64.b64encode(candidate.read_bytes()).decode("ascii")
        break

st.markdown(f"""
<style>
@font-face {{
    font-family: Neo;
    src: url(data:font/ttf;base64,{font_data}) format('truetype');
}}
#MainMenu, header, footer, [data-testid="stSidebar"],
[data-testid="stToolbar"], [data-testid="stDecoration"] {{display:none!important;}}
html, body, [data-testid="stAppViewContainer"], .stApp {{
    background:#020609!important; color:#eefaff!important; font-family:Neo,monospace!important;
}}
.block-container {{max-width:1040px!important;padding:clamp(24px,6vh,70px) clamp(18px,4vw,48px) 44px!important;}}
.manual-head {{border:3px double #26d9f5;padding:26px clamp(18px,4vw,42px);position:relative;
 background:linear-gradient(135deg,#03111b,#020609 72%);box-shadow:0 0 18px #00dfff18;margin-bottom:22px;}}
.manual-kicker {{color:#42eaff;letter-spacing:3px;font-size:12px;margin-bottom:14px;}}
.manual-title {{font-size:clamp(26px,4vw,44px);letter-spacing:2px;line-height:1.4;margin:0;color:#f5fdff;}}
.manual-subtitle {{color:#a8eafa;letter-spacing:1px;margin-top:10px;font-size:clamp(12px,1.8vw,16px);}}
.manual-grid {{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:18px 0 22px;}}
.manual-card {{border:2px solid #147b94;background:#030b11;padding:18px 20px;min-height:105px;box-shadow:inset 0 0 18px #00cfff08;}}
.manual-card .num {{color:#38eaff;font-size:12px;letter-spacing:2px;margin-bottom:10px;}}
.manual-card .label {{font-size:17px;color:#fff;margin-bottom:8px;}}
.manual-card .detail {{font-size:13px;line-height:1.9;color:#c8e7ef;}}
.manual-note {{border:2px solid #25bcd7;background:#041018;padding:16px 20px;color:#d9f7ff;line-height:1.9;font-size:13px;margin:16px 0 22px;}}
div[data-testid="stButton"] button {{font-family:Neo,monospace!important;border-radius:0!important;min-height:48px!important;
 background:#020609!important;color:#eefaff!important;border:2px solid #26d9f5!important;box-shadow:0 0 10px #00dfff18!important;}}
div[data-testid="stButton"] button:hover {{background:#26d9f5!important;border-color:#26d9f5!important;color:#000!important;}}
@media(max-width:650px) {{
 .manual-grid {{grid-template-columns:1fr;}}
 .manual-head {{padding:22px 18px;}}
 .manual-card {{min-height:0;}}
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<section class="manual-head">
  <div class="manual-kicker">PROJECT : LOGIC // SYSTEM MANUAL</div>
  <h1 class="manual-title">HOW TO PLAY</h1>
  <div class="manual-subtitle">INFORMATION IS NOT ALWAYS TRUE</div>
</section>
<div class="manual-grid">
  <div class="manual-card"><div class="num">01 // MOVEMENT</div><div class="label">이동</div><div class="detail">키보드의 W A S D 또는 화면에 표시되는 방향 버튼으로 이동합니다.</div></div>
  <div class="manual-card"><div class="num">02 // INTERACTION</div><div class="label">조사 / 상호작용</div><div class="detail">E 키 또는 화면의 INTERACT 버튼으로 주변 장치와 기록을 조사합니다.</div></div>
  <div class="manual-card"><div class="num">03 // DIALOGUE</div><div class="label">대사 진행</div><div class="detail">SPACE를 누르면 현재 출력 중인 문장만 완성됩니다. 필수 행동은 건너뛸 수 없습니다.</div></div>
  <div class="manual-card"><div class="num">04 // INVENTORY</div><div class="label">인벤토리 / 기록</div><div class="detail">I 키로 아이템을, H 키로 도움말을 확인합니다. 기록과 단서를 모아 보안 코드를 찾으세요.</div></div>
</div>
<div class="manual-note"><span style="color:#42eaff">SYSTEM TIP //</span> 단말기 기록과 보관 기록의 단서를 비교하세요. 표시된 숫자나 기록이 그대로 정답이라는 보장은 없습니다.</div>
""", unsafe_allow_html=True)

left, right = st.columns(2, gap="medium")
with left:
    if st.button("RETURN TO TITLE", use_container_width=True):
        st.switch_page("main.py")
with right:
    if st.button("START TUTORIAL", use_container_width=True):
        st.session_state.game_started = True
        st.session_state.game_paused = False
        st.session_state.start_open = False
        st.switch_page("pages/2_Game.py")
