import base64
from pathlib import Path

import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PROJECT : LOGIC",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# FONT
# =========================================================

font_candidates = [
    Path("neodgm.ttf"),
    Path("neodgm(2).ttf"),
]

font_path = None

for candidate in font_candidates:
    if candidate.exists():
        font_path = candidate
        break

if font_path:
    with open(font_path, "rb") as f:
        font_data = base64.b64encode(f.read()).decode("utf-8")
else:
    font_data = ""


# =========================================================
# SESSION STATE
# =========================================================

if "start_menu" not in st.session_state:
    st.session_state.start_menu = False


# =========================================================
# CSS
# =========================================================

st.markdown(
    f"""
    <style>

    /* =====================================================
       FONT
       ===================================================== */

    @font-face {{
        font-family: "NeoDungGeunMo";
        src: url(data:font/ttf;base64,{font_data});
    }}


    /* =====================================================
       STREAMLIT RESET
       ===================================================== */

    html,
    body,
    [data-testid="stAppViewContainer"],
    [data-testid="stApp"] {{
        background: #000000 !important;
    }}

    .block-container {{
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }}

    header {{
        visibility: hidden !important;
    }}

    footer {{
        visibility: hidden !important;
    }}

    #MainMenu {{
        visibility: hidden !important;
    }}

    [data-testid="stSidebar"] {{
        display: none !important;
    }}

    [data-testid="collapsedControl"] {{
        display: none !important;
    }}

    [data-testid="stSidebarNav"] {{
        display: none !important;
    }}


    /* =====================================================
       ALL BUTTONS
       ===================================================== */

    div[data-testid="stButton"] {{
        font-family: "NeoDungGeunMo", monospace !important;
    }}

    div[data-testid="stButton"] button {{
        font-family: "NeoDungGeunMo", monospace !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }}


    /* =====================================================
       TITLE
       ===================================================== */

    .title {{
        position: fixed;

        top: 12vh;
        left: 50%;

        transform: translateX(-50%);

        color: white;

        font-family: "NeoDungGeunMo", monospace;

        font-size: clamp(28px, 4vw, 48px);

        letter-spacing: 2px;

        white-space: nowrap;

        z-index: 10;

        animation: title-flicker 4s infinite;
    }}


    /* =====================================================
       SUBTITLE
       ===================================================== */

    .subtitle {{
        position: fixed;

        top: 22vh;
        left: 50%;

        transform: translateX(-50%);

        color: #999999;

        font-family: "NeoDungGeunMo", monospace;

        font-size: clamp(13px, 1.5vw, 18px);

        letter-spacing: 1px;

        white-space: nowrap;

        z-index: 10;
    }}


    /* =====================================================
       START BUTTON
       ===================================================== */

    div[data-testid="stButton"]:has(button[kind="secondary"]) {{
        font-family: "NeoDungGeunMo", monospace;
    }}


    .start-area {{
        position: fixed;

        top: 51vh;
        left: 50%;

        transform: translateX(-50%);

        width: 170px;
        height: 55px;

        z-index: 100;
    }}


    .start-area button {{
        width: 170px !important;
        height: 55px !important;

        padding: 0 !important;

        background: transparent !important;

        border: none !important;

        color: white !important;

        font-family: "NeoDungGeunMo", monospace !important;

        font-size: 19px !important;

        border-radius: 0 !important;
    }}


    .start-area button:hover {{
        background: white !important;

        color: black !important;
    }}


    /* =====================================================
       HOW TO PLAY
       ===================================================== */

    .how-area {{
        position: fixed;

        top: 65vh;
        left: 50%;

        transform: translateX(-50%);

        width: 220px;
        height: 55px;

        z-index: 100;
    }}


    .how-area button {{
        width: 220px !important;
        height: 55px !important;

        padding: 0 !important;

        background: transparent !important;

        border: none !important;

        color: white !important;

        font-family: "NeoDungGeunMo", monospace !important;

        font-size: 19px !important;

        border-radius: 0 !important;
    }}


    .how-area button:hover {{
        background: white !important;

        color: black !important;
    }}


    /* =====================================================
       POPUP
       ===================================================== */

    .popup-area {{
        position: fixed;

        top: calc(51vh - 3px);

        left: calc(50% + 105px);

        width: 190px;

        z-index: 101;
    }}


    .popup-area button {{
        width: 190px !important;

        height: 42px !important;

        padding: 0 0 0 18px !important;

        background: #050505 !important;

        border: none !important;

        border-left: 1px solid white !important;
        border-right: 1px solid white !important;

        color: white !important;

        font-family: "NeoDungGeunMo", monospace !important;

        font-size: 14px !important;

        text-align: left !important;

        border-radius: 0 !important;
    }}


    .popup-area button:hover {{
        background: white !important;

        color: black !important;
    }}


    /* =====================================================
       TITLE FLICKER
       ===================================================== */

    @keyframes title-flicker {{

        0%,
        18%,
        20%,
        22%,
        63%,
        65%,
        100% {{
            opacity: 1;
        }}

        19% {{
            opacity: 0.35;
        }}

        21% {{
            opacity: 0.65;
        }}

        64% {{
            opacity: 0.15;
        }}

    }}


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 600px) {{

        .start-area {{
            top: 51vh;
        }}

        .popup-area {{
            top: 59vh;

            left: 50%;

            transform: translateX(-50%);
        }}

        .how-area {{
            top: 73vh;
        }}

    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="title">PROJECT : LOGIC</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">INFORMATION IS NOT ALWAYS TRUE</div>',
    unsafe_allow_html=True,
)


# =========================================================
# START
# =========================================================

st.markdown('<div class="start-area">', unsafe_allow_html=True)

if st.button(
    "START",
    key="start_button",
    use_container_width=True,
):
    st.session_state.start_menu = not st.session_state.start_menu

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# START POPUP
# =========================================================

if st.session_state.start_menu:

    st.markdown(
        '<div class="popup-area">',
        unsafe_allow_html=True,
    )

    if st.button(
        "CONTINUE",
        key="continue_button",
        use_container_width=True,
    ):
        st.session_state.start_menu = False

        st.warning(
            "이전 플레이 기록이 존재하지 않습니다. 새 게임을 시작해주세요."
        )

    if st.button(
        "NEW GAME",
        key="new_game_button",
        use_container_width=True,
    ):
        st.session_state.start_menu = False

        # 게임 페이지가 만들어지면 연결
        # st.switch_page("pages/2_Game.py")

        st.info("NEW GAME은 게임 화면 구현 후 연결됩니다.")

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# HOW TO PLAY
# =========================================================

st.markdown(
    '<div class="how-area">',
    unsafe_allow_html=True,
)

if st.button(
    "HOW TO PLAY",
    key="how_to_play_button",
    use_container_width=True,
):
    st.switch_page("pages/1_How_To_Play.py")

st.markdown("</div>", unsafe_allow_html=True)
