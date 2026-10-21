import base64
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="PROJECT : LOGIC",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Navigation requests and persistent progress flags.
_page_action = st.query_params.get("action", "")

if _page_action == "title":
    st.query_params.clear()
    st.session_state.game_paused = False
    st.session_state.start_open = True
    st.session_state.show_title_warning = False
    st.rerun()

elif _page_action == "stage01":
    st.query_params.clear()
    st.session_state.stage01_started = True
    st.session_state.game_started = True
    st.session_state.game_paused = False
    st.session_state.start_open = False
    st.switch_page("pages/3_Stage_01.py")

elif _page_action == "restart":
    # RESTART is a full run restart: always begin at Stage 01, never retry Stage 02.
    st.query_params.clear()
    for _key in list(st.session_state.keys()):
        if _key.startswith(("s1_", "tutorial_", "stage01_", "stage02_")):
            del st.session_state[_key]
    st.session_state.tutorial_reset_save = True
    st.session_state.stage01_reset_save = True
    st.session_state.stage02_reset_save = True
    st.session_state.game_started = True
    st.session_state.game_paused = False
    st.session_state.game_finished = False
    st.session_state.tutorial_complete = True
    st.session_state.stage01_started = True
    st.session_state.stage02_started = False
    st.session_state.remaining_seconds = 15 * 60
    st.session_state.start_open = False
    st.switch_page("pages/3_Stage_01.py")

for key, value in {
    "start_open": False,
    "game_started": False,
    "game_paused": False,
    "game_finished": False,
    "remaining_seconds": 15 * 60,
    "new_game_confirm": False,
    "show_title_warning": False,
    "settings_open": False,
    "exit_notice": False,
    "sound_enabled": True,
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

lab_background_data = base64.b64encode((Path(__file__).resolve().parent / "assets" / "lab_background.jpeg").read_bytes()).decode("ascii")

font_data = ""
for candidate in (Path("neodgm.ttf"), Path("neodgm(2).ttf")):
    if candidate.exists():
        font_data = base64.b64encode(candidate.read_bytes()).decode("utf-8")
        break

st.markdown(f"""
<style>
@font-face {{
    font-family: NeoDungGeunMo;
    src: url(data:font/ttf;base64,{font_data}) format('truetype');
}}
#MainMenu,header,footer,[data-testid="stSidebar"] {{
    visibility:hidden;
    display:none;
}}
.stApp {{
    background: #000 url(data:image/jpeg;base64,{lab_background_data}) center center / cover no-repeat fixed!important;
    color:#fff;
    font-family:NeoDungGeunMo,monospace;
}}
.stApp::before {{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.38;background:repeating-linear-gradient(0deg,transparent 0 39px,#0a8fb522 40px,#0a8fb522 41px),linear-gradient(90deg,transparent 0 7%,#0a8fb51c 7.1%,transparent 7.3% 92%,#0a8fb51c 92.1%,transparent 92.3%);}}
.block-container>div {{position:relative;z-index:1;}}
.block-container {{
    padding:0!important;
    max-width:100%!important;
}}
.project-title {{
    position:fixed;
    top:20vh;
    left:0;
    width:100%;
    text-align:center;
    color:#fff;
    font-family:NeoDungGeunMo,monospace;
    font-size:42px;
    letter-spacing:3px;
    z-index:10;
    text-shadow:0 0 3px #fff,0 0 10px #aaa;
    animation:titleFlicker 5.2s infinite steps(1,end);
}}
.project-subtitle {{
    position:fixed;
    top:31vh;
    left:0;
    width:100%;
    text-align:center;
    color:#555;
    font-family:NeoDungGeunMo,monospace;
    font-size:13px;
    letter-spacing:2px;
    z-index:10;
}}
@keyframes titleFlicker {{
    0%,7%,9%,11%,44%,46%,48%,100% {{
        opacity:1;
        filter:brightness(1);
        text-shadow:0 0 3px #fff,0 0 10px #aaa;
    }}
    8%,10% {{
        opacity:.35;
        filter:brightness(.65);
        text-shadow:none;
    }}
    45%,47% {{
        opacity:.65;
        filter:brightness(.8);
        text-shadow:0 0 2px #fff;
    }}
    72% {{opacity:.92}}
    73% {{opacity:.55}}
    74% {{opacity:1}}
}}
@media(prefers-reduced-motion:reduce) {{
    .project-title {{animation:none}}
}}
.st-key-start_button,
.st-key-how_to_play_button {{
    position:fixed!important;
    left:50%!important;
    transform:translateX(-50%)!important;
    margin:0!important;
    padding:0!important;
    z-index:100!important;
}}
.st-key-start_button {{
    top:51vh!important;
    width:170px!important;
    height:55px!important;
}}
.st-key-how_to_play_button {{
    top:65vh!important;
    width:220px!important;
    height:55px!important;
}}
.st-key-start_button button,
.st-key-how_to_play_button button {{
    width:100%!important;
    height:55px!important;
    border:0!important;
    border-radius:0!important;
    background:rgba(0,0,0,.92)!important;
    color:#fff!important;
    border:1px solid #26d9f5!important;
    font-family:NeoDungGeunMo,monospace!important;
    font-size:19px!important;
    box-shadow:none!important;
}}
.st-key-start_button button:hover,
.st-key-how_to_play_button button:hover {{
    background:#fff!important;
    color:#000!important;
}}
.st-key-popup {{
    position:fixed!important;
    top:calc(51vh - 3px)!important;
    left:calc(50% + 105px)!important;
    width:190px!important;
    margin:0!important;
    padding:6px!important;
    background:#000!important;
    border:1px solid #26d9f5!important;
    box-shadow:0 0 18px #00dfff22!important;
    z-index:200!important;
}}
.st-key-confirm_modal {{
    position:fixed!important;
    inset:0!important;
    z-index:9999!important;
    display:flex!important;
    align-items:center!important;
    justify-content:center!important;
    padding:18px!important;
    background:rgba(0,0,0,.78)!important;
}}
.st-key-confirm_modal [data-testid="stVerticalBlockBorderWrapper"] {{
    width:min(430px,92vw)!important;
    max-width:430px!important;
    border:1px solid #aaa!important;
    background:#050505!important;
    box-shadow:0 0 0 1px #333,0 12px 40px #000!important;
    padding:22px 24px!important;
}}
.st-key-confirm_modal [data-testid="stMarkdownContainer"] p {{
    font-family:NeoDungGeunMo,monospace!important;
    font-size:13px!important;
    line-height:1.8!important;
    color:#ddd!important;
}}
.st-key-confirm_modal [data-testid="stButton"] button {{
    height:40px!important;
    border:1px solid #666!important;
    background:#050505!important;
    color:#fff!important;
    font-family:NeoDungGeunMo,monospace!important;
    border-radius:0!important;
}}
.st-key-confirm_modal [data-testid="stButton"] button:hover {{
    background:#fff!important;
    color:#000!important;
}}
.st-key-popup button {{
    width:100%!important;
    height:42px!important;
    margin:0 0 6px!important;
    padding:0!important;
    border:0!important;
    border-radius:0!important;
    background:#000!important;
    color:#fff!important;
    font-family:NeoDungGeunMo,monospace!important;
    font-size:14px!important;
}}
.st-key-popup button:last-child {{margin-bottom:0!important}}
.st-key-popup button:hover {{
    background:#fff!important;
    color:#000!important;
}}
[data-testid="stAlert"] {{
    position:fixed!important;
    top:calc(51vh + 115px)!important;
    left:50%!important;
    transform:translateX(-50%)!important;
    width:min(390px,85vw)!important;
    z-index:300!important;
    font-family:NeoDungGeunMo,monospace!important;
    font-size:13px!important;
}}
 .st-key-menu_panel{{position:fixed!important;top:49vh!important;left:50%!important;transform:translateX(-50%)!important;width:min(250px,78vw)!important;box-sizing:border-box!important;padding:12px 16px!important;border:2px solid #26d9f5!important;background:rgba(0,0,0,.84)!important;box-shadow:0 0 18px #00dfff20!important;z-index:100!important}}
.st-key-menu_panel [data-testid="stButton"]{{margin:0 0 5px!important}}
.st-key-menu_panel [data-testid="stButton"]:last-child{{margin-bottom:0!important}}
.st-key-menu_panel button{{width:100%!important;height:37px!important;min-height:37px!important;border:1px solid #147b94!important;border-radius:0!important;background:#000!important;color:#eafaff!important;font-family:NeoDungGeunMo,monospace!important;font-size:14px!important;box-shadow:none!important}}
.st-key-menu_panel button:hover{{background:#fff!important;color:#000!important;border-color:#fff!important}}
.st-key-settings_modal{{position:fixed!important;inset:0!important;z-index:9999!important;display:flex!important;align-items:center!important;justify-content:center!important;background:rgba(0,0,0,.82)!important;padding:18px!important}}
.st-key-settings_modal [data-testid="stVerticalBlockBorderWrapper"]{{width:min(400px,92vw)!important;border:2px solid #26d9f5!important;background:#000!important;padding:24px!important}}
.st-key-settings_modal button{{background:#000!important;color:#fff!important;border:1px solid #26d9f5!important;border-radius:0!important;font-family:NeoDungGeunMo,monospace!important}}
@media(max-width:700px) {{
    .st-key-menu_panel{{top:48vh!important;width:min(230px,80vw)!important}}
    .project-title {{
        top:17vh;
        font-size:30px;
        letter-spacing:2px;
    }}
    .project-subtitle {{top:28vh;font-size:10px}}
    .st-key-start_button {{top:56vh!important;width:160px!important}}
    .st-key-how_to_play_button {{top:73vh!important;width:200px!important}}
    .st-key-popup {{
        top:59vh!important;
        left:50%!important;
        transform:translateX(-50%)!important;
        width:180px!important;
    }}
    [data-testid="stAlert"] {{top:70vh!important}}
}}
</style>
""", unsafe_allow_html=True)

# Returning from a game lands on the clean title screen.
st.session_state.show_title_warning = False

st.markdown(
    '<div class="project-title">PROJECT : LOGIC</div>'
    '<div class="project-subtitle">INFORMATION IS NOT ALWAYS TRUE</div>',
    unsafe_allow_html=True,
)

with st.container(key="menu_panel"):
    new_game_clicked = st.button("NEW GAME", key="menu_new_game", use_container_width=True)
    continue_clicked = st.button("CONTINUE", key="menu_continue", use_container_width=True)
    settings_clicked = st.button("SETTINGS", key="menu_settings", use_container_width=True)
    exit_clicked = st.button("EXIT", key="menu_exit", use_container_width=True)

if settings_clicked:
    st.session_state.settings_open = not st.session_state.settings_open
    st.session_state.exit_notice = False
if exit_clicked:
    st.session_state.exit_notice = not st.session_state.exit_notice
    st.session_state.settings_open = False

if continue_clicked:
    st.session_state.start_open = False
    st.session_state.game_started = True
    st.session_state.game_paused = False
    if st.session_state.get("stage02_started", False):
        st.switch_page("pages/4_Stage_02.py")
    elif st.session_state.get("stage01_started", False):
        st.switch_page("pages/3_Stage_01.py")
    else:
        st.switch_page("pages/2_Game.py")

if new_game_clicked:
    # NEW GAME always overwrites the previous run and its browser-local saves.
    progress_prefixes = ("s1_", "tutorial_", "stage01_", "stage02_")
    for _key in list(st.session_state.keys()):
        if _key.startswith(progress_prefixes):
            del st.session_state[_key]
    st.session_state.tutorial_reset_save = True
    st.session_state.stage01_reset_save = True
    st.session_state.stage02_reset_save = True
    st.session_state.game_started = True
    st.session_state.game_paused = False
    st.session_state.game_finished = False
    st.session_state.tutorial_complete = False
    st.session_state.stage01_started = False
    st.session_state.stage02_started = False
    st.session_state.remaining_seconds = 15 * 60
    st.session_state.new_game_confirm = False
    st.session_state.start_open = False
    st.session_state.settings_open = False
    st.session_state.exit_notice = False
    st.switch_page("pages/2_Game.py")

if st.session_state.settings_open:
    with st.container(key="settings_modal", border=True):
        st.markdown("### SETTINGS")
        st.session_state.sound_enabled = st.toggle("SOUND", value=st.session_state.sound_enabled, key="sound_toggle")
        if st.button("CLOSE", key="close_settings", use_container_width=True):
            st.session_state.settings_open = False
            st.rerun()

if st.session_state.exit_notice:
    st.warning("SESSION MENU // 브라우저 탭을 닫으면 게임을 종료할 수 있습니다.")

if st.session_state.get("new_game_confirm", False):
    with st.container(key="confirm_modal", border=False):
        st.markdown("### SYSTEM CONFIRMATION")
        st.markdown(
            "이전 플레이 기록이 존재합니다.\n\n"
            "기록을 초기화하고 새 게임을 시작하시겠습니까?"
        )

        yes_col, no_col = st.columns(2, gap="small")

        with yes_col:
            yes_new_game = st.button(
                "YES", key="confirm_new_game_yes",
                use_container_width=True
            )

        with no_col:
            no_new_game = st.button(
                "NO", key="confirm_new_game_no",
                use_container_width=True
            )

    if yes_new_game:
        for _key in list(st.session_state.keys()):
            if _key.startswith(
                ("s1_", "tutorial_", "stage01_", "stage02_")
            ):
                del st.session_state[_key]

        st.session_state.tutorial_reset_save = True
        st.session_state.stage01_reset_save = True
        st.session_state.stage02_reset_save = True
        st.session_state.game_started = True
        st.session_state.game_paused = False
        st.session_state.game_finished = False
        st.session_state.remaining_seconds = 15 * 60
        st.session_state.tutorial_complete = False
        st.session_state.stage01_started = False
        st.session_state.stage02_started = False
        st.session_state.new_game_confirm = False
        st.session_state.start_open = False
        st.switch_page("pages/2_Game.py")

    if no_new_game:
        st.session_state.new_game_confirm = False
        st.rerun()
