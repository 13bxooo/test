import base64
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="PROJECT : LOGIC // STAGE 01",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Native Streamlit state/navigation: no components.html, embedded JavaScript, or iframe.
DEFAULTS = {
    "s1_paused": False,
    "s1_confirm_restart": False,
    "s1_seconds": 720,
    "s1_message_index": 0,
    "s1_message_complete": False,
    "s1_found": {"A": False, "B": False, "C": False},
    "s1_archive_read": False,
    "s1_unlocked": False,
    "s1_finished": False,
    "s1_code": "",
    "s1_error": "",
    "s1_status": "ECHO SYSTEM // 안내된 행동을 먼저 완료하십시오.",
}
for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value.copy() if isinstance(value, dict) else value

# The page is reached from the tutorial through st.switch_page. Navigation buttons
# below also use Streamlit's own page navigation, not parent-window URL manipulation.
font_data = ""
for candidate in (Path("neodgm.ttf"), Path("neodgm(2).ttf"), Path(__file__).resolve().parents[1] / "neodgm(2).ttf"):
    if candidate.exists():
        font_data = base64.b64encode(candidate.read_bytes()).decode("ascii")
        break

st.markdown(f"""
<style>
@font-face {{ font-family: Neo; src: url(data:font/ttf;base64,{font_data}) format('truetype'); }}
#MainMenu, header, footer, [data-testid="stSidebar"] {{ display:none; visibility:hidden; }}
.stApp {{ background:#000; color:#eee; font-family:Neo,monospace; }}
.block-container {{ padding:1.2rem 2rem 2rem; max-width:1200px; }}
html, body, [class*="css"] {{ font-family:Neo,monospace !important; }}
.stButton button, .stTextInput input {{ font-family:Neo,monospace !important; border-radius:0 !important; }}
.stButton button {{ background:#050505; color:#eee; border:1px solid #555; min-height:42px; }}
.stButton button:hover {{ background:#eee; color:#000; border-color:#eee; }}
[data-testid="stTextInput"] input {{ background:#000; color:#fff; border:1px solid #666; }}
.stage-frame {{ border:1px solid #383838; padding:14px; background-color:#050505;
 background-image:linear-gradient(#ffffff0b 1px,transparent 1px),linear-gradient(90deg,#ffffff0b 1px,transparent 1px);
 background-size:36px 36px; }}
.stage-title {{ letter-spacing:2px; font-size:22px; line-height:1.65; white-space:pre-line; animation:stageSignFlicker 5.2s infinite steps(1,end); text-shadow:0 0 3px #fff,0 0 8px #888; }}
@keyframes stageSignFlicker {{
  0%,7%,9%,11%,44%,46%,48%,100% {{ opacity:1; filter:brightness(1); text-shadow:0 0 3px #fff,0 0 8px #888; }}
  8%,10% {{ opacity:.35; filter:brightness(.65); text-shadow:none; }}
  45%,47% {{ opacity:.65; filter:brightness(.8); text-shadow:0 0 2px #fff; }}
  72% {{ opacity:.92; }} 73% {{ opacity:.55; }} 74% {{ opacity:1; }}
}}
@media(prefers-reduced-motion:reduce) {{ .stage-title {{ animation:none; }} }}
.stage-sub {{ color:#777; font-size:11px; letter-spacing:1px; }}
.object {{ min-height:84px; border:1px solid #555; background:#080808; padding:14px 6px; text-align:center; color:#aaa; }}
.object-name {{ color:#bbb; font-size:12px; }}
.object-state {{ color:#666; font-size:10px; margin-top:7px; }}
.echo-box {{ border:1px solid #444; background:#050505; padding:14px 16px; min-height:100px; }}
.echo-name {{ font-size:11px; color:#fff; margin-bottom:8px; }}
.echo-copy {{ font-size:12px; color:#bbb; line-height:1.8; }}
.small-note {{ font-size:10px; color:#666; }}
</style>
""", unsafe_allow_html=True)

MESSAGES = [
    "연결이 확인되었습니다. 저는 ECHO입니다. 이 시설에서의 첫 번째 절차를 안내하겠습니다.",
    "이 구역에는 제한 시간이 적용됩니다. 주변의 단말기와 보관 기록을 조사하십시오.",
    "각 단말기에서 숫자를 하나씩 확보하십시오. 기록을 확보하면 보안 패널에 표시됩니다.",
    "ARCHIVE NOTE에는 숫자를 조합할 순서가 기록되어 있습니다. 단말기의 숫자와 기록의 순서를 함께 확인하십시오.",
    "세 구역의 기록과 보관 기록을 모두 확인했다면 SECURITY PANEL에서 세 자리 코드를 입력하십시오.",
    "인증이 완료되면 출구로 이동하십시오. 이동은 아래 방향 버튼으로 진행할 수 있습니다.",
]
DIGITS = {"A": "4", "B": "1", "C": "7"}


def reset_stage():
    for key, value in DEFAULTS.items():
        st.session_state[key] = value.copy() if isinstance(value, dict) else value


def navigate_title():
    st.session_state.s1_paused = False
    st.session_state.s1_confirm_restart = False
    st.session_state.show_title_warning = True
    st.switch_page("main.py")


def navigate_restart():
    st.session_state.tutorial_reset_save = True
    reset_stage()
    st.session_state.game_paused = False
    st.session_state.tutorial_complete = False
    st.session_state.stage01_started = False
    st.switch_page("pages/2_Game.py")


def close_pause():
    st.session_state.s1_paused = False


st.markdown('<div class="stage-title">STAGE 01<br>:ARCHIVE ACCESS</div>', unsafe_allow_html=True)
head_left, head_mid, head_right = st.columns([1, 2, 1])
with head_mid:
    mins, secs = divmod(max(0, st.session_state.s1_seconds), 60)
    st.markdown(f"<div style='text-align:center;font-size:20px;letter-spacing:2px'>{mins:02d}:{secs:02d}</div>", unsafe_allow_html=True)
with head_right:
    if st.button("Ⅱ  PAUSE", key="s1_pause_button", use_container_width=True, disabled=st.session_state.s1_finished):
        st.session_state.s1_paused = True
        st.rerun()

if st.session_state.s1_paused:
    st.markdown("---")
    st.subheader("GAME PAUSED")
    st.caption("일시정지 상태입니다. 현재 대사와 진행 기록은 유지됩니다.")
    p1, p2, p3 = st.columns(3)
    with p1:
        if st.button("RESUME", key="s1_resume", use_container_width=True):
            close_pause()
            st.rerun()
    with p2:
        if st.button("RESTART", key="s1_restart", use_container_width=True):
            st.session_state.s1_confirm_restart = True
            st.rerun()
    with p3:
        if st.button("TITLE", key="s1_title", use_container_width=True):
            navigate_title()
    if st.session_state.s1_confirm_restart:
        st.warning("처음부터 다시 시작할까요? 현재 스테이지 진행 기록은 초기화됩니다.")
        yes, no = st.columns(2)
        with yes:
            if st.button("YES — RESTART FROM TUTORIAL", key="s1_restart_yes", use_container_width=True):
                navigate_restart()
        with no:
            if st.button("NO — CANCEL", key="s1_restart_no", use_container_width=True):
                st.session_state.s1_confirm_restart = False
                st.rerun()
    st.stop()

# Draw the room with Streamlit columns and native buttons, not an HTML/JS game embedded in an iframe.
st.markdown('<div class="stage-frame">', unsafe_allow_html=True)
a, gap, b, gap2, c = st.columns([1, .25, 1, .25, 1])
with a:
    st.markdown(f'<div class="object"><div class="object-name">SECTOR A</div><div class="object-state">{"DATA FOUND" if st.session_state.s1_found["A"] else "DATA LOCKED"}</div></div>', unsafe_allow_html=True)
    if st.button("INSPECT A", key="s1_inspect_a", use_container_width=True, disabled=st.session_state.s1_paused or st.session_state.s1_finished):
        st.session_state.s1_found["A"] = True
        st.session_state.s1_status = "SECTOR A // 인증 숫자 4를 확보했습니다."
        st.session_state.s1_seconds = max(0, st.session_state.s1_seconds - 1)
        st.rerun()
with b:
    st.markdown(f'<div class="object"><div class="object-name">COMPUTER / SECTOR B</div><div class="object-state">{"DATA FOUND" if st.session_state.s1_found["B"] else "DATA LOCKED"}</div></div>', unsafe_allow_html=True)
    if st.button("INSPECT B", key="s1_inspect_b", use_container_width=True, disabled=st.session_state.s1_paused or st.session_state.s1_finished):
        st.session_state.s1_found["B"] = True
        st.session_state.s1_status = "SECTOR B // 인증 숫자 1을 확보했습니다."
        st.session_state.s1_seconds = max(0, st.session_state.s1_seconds - 1)
        st.rerun()
with c:
    st.markdown(f'<div class="object"><div class="object-name">SECTOR C</div><div class="object-state">{"DATA FOUND" if st.session_state.s1_found["C"] else "DATA LOCKED"}</div></div>', unsafe_allow_html=True)
    if st.button("INSPECT C", key="s1_inspect_c", use_container_width=True, disabled=st.session_state.s1_paused or st.session_state.s1_finished):
        st.session_state.s1_found["C"] = True
        st.session_state.s1_status = "SECTOR C // 인증 숫자 7을 확보했습니다."
        st.session_state.s1_seconds = max(0, st.session_state.s1_seconds - 1)
        st.rerun()

st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
left, center, right = st.columns([1, 1.2, 1])
with left:
    st.markdown(f'<div class="object"><div class="object-name">ARCHIVE NOTE</div><div class="object-state">{"ORDER RECORDED" if st.session_state.s1_archive_read else "UNREAD"}</div></div>', unsafe_allow_html=True)
    if st.button("READ ARCHIVE NOTE", key="s1_archive", use_container_width=True, disabled=st.session_state.s1_finished):
        st.session_state.s1_archive_read = True
        st.session_state.s1_status = "ARCHIVE NOTE // 코드 입력 순서: C → A → B"
        st.session_state.s1_seconds = max(0, st.session_state.s1_seconds - 1)
        st.rerun()
with center:
    st.markdown('<div class="object"><div class="object-name">ECHO TERMINAL</div><div class="object-state">FACILITY SYSTEM</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="small-note" style="text-align:center;margin-top:8px">SYSTEM MESSAGE // INTERACTION LOG</div>', unsafe_allow_html=True)
with right:
    st.markdown(f'<div class="object"><div class="object-name">SECURITY PANEL</div><div class="object-state">{"UNLOCKED" if st.session_state.s1_unlocked else "LOCKED"}</div></div>', unsafe_allow_html=True)
    st.text_input("3자리 코드", key="s1_code", max_chars=3, placeholder="예: 741", label_visibility="collapsed", disabled=st.session_state.s1_finished)
    if st.button("VERIFY CODE", key="s1_verify", use_container_width=True, disabled=st.session_state.s1_finished):
        if not all(st.session_state.s1_found.values()) or not st.session_state.s1_archive_read:
            st.session_state.s1_error = "먼저 A·B·C 단말기와 ARCHIVE NOTE를 모두 확인하십시오."
        elif st.session_state.s1_code.strip() == "741":
            st.session_state.s1_unlocked = True
            st.session_state.s1_error = ""
            st.session_state.s1_status = "SECURITY PANEL // 인증 완료. 출구로 이동하십시오."
        else:
            st.session_state.s1_error = "CODE INVALID // 기록의 순서를 다시 확인하십시오."
        st.session_state.s1_seconds = max(0, st.session_state.s1_seconds - 1)
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### MOVEMENT / EXIT")
move_left, move_mid, move_right = st.columns([1, 1, 1])
with move_left:
    if st.button("← MOVE", key="s1_move_left", use_container_width=True, disabled=st.session_state.s1_finished):
        st.session_state.s1_status = "이동했습니다. 주변 단말기와 기록을 조사하십시오."
        st.session_state.s1_seconds = max(0, st.session_state.s1_seconds - 1)
        st.rerun()
with move_mid:
    if st.button("↑ MOVE / EXIT", key="s1_move_exit", use_container_width=True, disabled=st.session_state.s1_finished):
        if st.session_state.s1_unlocked:
            st.session_state.s1_finished = True
            st.session_state.s1_status = "STAGE 01 CLEAR // 다음 구역의 신호가 감지되었습니다."
        else:
            st.session_state.s1_status = "EXIT SEALED // 먼저 SECURITY PANEL 인증을 완료하십시오."
        st.session_state.s1_seconds = max(0, st.session_state.s1_seconds - 1)
        st.rerun()
with move_right:
    if st.button("MOVE →", key="s1_move_right", use_container_width=True, disabled=st.session_state.s1_finished):
        st.session_state.s1_status = "이동했습니다. 주변 단말기와 기록을 조사하십시오."
        st.session_state.s1_seconds = max(0, st.session_state.s1_seconds - 1)
        st.rerun()

if st.session_state.s1_seconds <= 0 and not st.session_state.s1_finished:
    st.session_state.s1_finished = True
    st.session_state.s1_status = "TIME EXPIRED // RESTART를 선택해 다시 도전하십시오."

if st.session_state.s1_finished:
    st.success(st.session_state.s1_status)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("RESTART STAGE", key="s1_finish_restart", use_container_width=True):
            reset_stage()
            st.rerun()
    with col2:
        if st.button("TITLE", key="s1_finish_title", use_container_width=True):
            navigate_title()
else:
    st.markdown(f'<div class="echo-box"><div class="echo-name">ECHO // SYSTEM AI</div><div class="echo-copy">{MESSAGES[min(st.session_state.s1_message_index, len(MESSAGES)-1)]}</div></div>', unsafe_allow_html=True)
    st.caption(st.session_state.s1_status)
    if st.session_state.s1_error:
        st.error(st.session_state.s1_error)
    if st.button("NEXT / CONTINUE", key="s1_next_message", use_container_width=True):
        st.session_state.s1_message_index = (st.session_state.s1_message_index + 1) % len(MESSAGES)
        st.session_state.s1_seconds = max(0, st.session_state.s1_seconds - 1)
        st.rerun()

st.caption("조작: 각 구역의 INSPECT 버튼으로 기록을 확보하고, ARCHIVE NOTE를 읽은 뒤 코드 741을 입력하세요. 인증 후 MOVE / EXIT를 누르면 스테이지가 완료됩니다.")
