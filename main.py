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

font_data = ""

for font_path in font_candidates:
    if font_path.exists():
        with open(font_path, "rb") as f:
            font_data = base64.b64encode(f.read()).decode("utf-8")
        break


# =========================================================
# STREAMLIT UI HIDDEN
# =========================================================

st.markdown(
    f"""
    <style>

    @font-face {{
        font-family: "NeoDungGeunMo";
        src: url(data:font/ttf;base64,{font_data});
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    header {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    [data-testid="stSidebar"] {{
        display: none;
    }}

    .stApp {{
        background: #000000;
    }}

    .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
    }}


    /* =====================================================
       START SCREEN
       ===================================================== */

    .screen {{
        position: fixed;
        inset: 0;

        width: 100vw;
        height: 100vh;

        background: #000000;
        color: #ffffff;

        overflow: hidden;
    }}


    /* =====================================================
       TITLE
       ===================================================== */

    .project-title {{
        position: absolute;

        top: 12vh;
        left: 50%;

        transform: translateX(-50%);

        white-space: nowrap;

        font-family: "NeoDungGeunMo", monospace;

        font-size: clamp(28px, 4vw, 48px);

        letter-spacing: 2px;

        animation: title-flicker 4s infinite;
    }}


    .project-subtitle {{
        position: absolute;

        top: 22vh;
        left: 50%;

        transform: translateX(-50%);

        white-space: nowrap;

        color: #9c9c9c;

        font-family: "NeoDungGeunMo", monospace;

        font-size: clamp(13px, 1.5vw, 18px);

        letter-spacing: 1px;
    }}


    /* =====================================================
       STREAMLIT BUTTON COMMON
       ===================================================== */

    div.stButton {{
        position: absolute;
        z-index: 100;
    }}

    div.stButton > button {{
        border-radius: 0 !important;

        background: transparent !important;

        border: none !important;

        color: #ffffff !important;

        font-family: "NeoDungGeunMo", monospace !important;

        cursor: pointer !important;

        box-shadow: none !important;

        transition:
            background 0.15s ease,
            color 0.15s ease !important;
    }}

    div.stButton > button:hover {{
        background: #ffffff !important;

        color: #000000 !important;

        border: none !important;
    }}

    div.stButton > button:focus {{
        background: transparent !important;

        color: #ffffff !important;

        border: none !important;

        box-shadow: none !important;
    }}

    div.stButton > button:focus:hover {{
        background: #ffffff !important;

        color: #000000 !important;
    }}


    /* =====================================================
       START BUTTON
       ===================================================== */

    .start-button {{
        top: 51vh;
        left: 50%;

        transform: translateX(-50%);

        width: 170px;
        height: 55px;
    }}

    .start-button button {{
        width: 170px !important;
        height: 55px !important;

        padding: 0 !important;

        font-size: 19px !important;
    }}


    /* =====================================================
       HOW TO PLAY
       ===================================================== */

    .how-button {{
        top: 65vh;
        left: 50%;

        transform: translateX(-50%);

        width: 220px;
        height: 55px;
    }}

    .how-button button {{
        width: 220px !important;
        height: 55px !important;

        padding: 0 !important;

        font-size: 19px !important;
    }}


    /* =====================================================
       START POPUP
       ===================================================== */

    .popup {{
        position: absolute;

        top: calc(51vh - 3px);
        left: calc(50% + 105px);

        width: 190px;

        background: #050505;

        border: 1px solid #ffffff;

        z-index: 200;
    }}


    .popup-title {{
        display: none;
    }}


    /* =====================================================
       POPUP BUTTONS
       ===================================================== */

    .popup-area {{
        position: absolute;

        top: calc(51vh - 3px);
        left: calc(50% + 105px);

        width: 190px;

        z-index: 300;
    }}

    .popup-area div.stButton {{
        position: relative !important;

        width: 190px;

        height: 42px;

        left: 0;
        top: 0;

        transform: none;
    }}

    .popup-area div.stButton > button {{
        width: 190px !important;
        height: 42px !important;

        padding: 0 18px !important;

        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;

        background: #050505 !important;

        border: none !important;

        color: #ffffff !important;

        font-size: 14px !important;

        text-align: left !important;
    }}

    .popup-area div.stButton > button:hover {{
        background: #ffffff !important;

        color: #000000 !important;
    }}


    /* =====================================================
       TITLE FLICKER
       ===================================================== */

    @keyframes title-flicker {{

        0%, 18%, 20%, 22%, 63%, 65%, 100% {{
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

        .start-button {{
            top: 51vh;
        }}

        .how-button {{
            top: 73vh;
        }}

        .popup-area {{
            top: 59vh;
            left: 50%;

            transform: translateX(-50%);
        }}

    }}

    </style>

    <div class="screen">

        <div class="project-title">
            PROJECT : LOGIC
        </div>

        <div class="project-subtitle">
            INFORMATION IS NOT ALWAYS TRUE
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# START BUTTON
# =========================================================

st.markdown(
    '<div class="start-button">',
    unsafe_allow_html=True,
)

start_clicked = st.button(
    "START",
    key="start_button",
)

st.markdown(
    "</div>",
    unsafe_allow_html=True,
)


# =========================================================
# START POPUP
# =========================================================

if start_clicked:
    st.session_state.start_open = not st.session_state.get(
        "start_open",
        False,
    )


if st.session_state.get("start_open", False):

    st.markdown(
        '<div class="popup-area">',
        unsafe_allow_html=True,
    )

    continue_clicked = st.button(
        "CONTINUE",
        key="continue_button",
    )

    new_game_clicked = st.button(
        "NEW GAME",
        key="new_game_button",
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    if continue_clicked:
        st.warning(
            "이전 플레이 기록이 존재하지 않습니다. 새 게임을 시작해주세요."
        )

    if new_game_clicked:
        st.info(
            "GAME SYSTEM은 현재 준비 중입니다."
        )


# =========================================================
# HOW TO PLAY
# =========================================================

st.markdown(
    '<div class="how-button">',
    unsafe_allow_html=True,
)

how_to_play_clicked = st.button(
    "HOW TO PLAY",
    key="how_to_play_button",
)

st.markdown(
    "</div>",
    unsafe_allow_html=True,
)


# =========================================================
# PAGE NAVIGATION
# =========================================================

if how_to_play_clicked:
    st.switch_page("pages/1_How_To_Play.py")
