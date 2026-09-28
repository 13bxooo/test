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
# STREAMLIT UI HIDE
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

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# TITLE SCREEN
# =========================================================

st.markdown(
    f"""
    <style>

    .screen {{
        position: fixed;
        inset: 0;

        background: #000000;

        font-family: "NeoDungGeunMo", monospace;
        color: white;
    }}

    .title {{
        position: absolute;

        top: 12vh;
        left: 50%;

        transform: translateX(-50%);

        white-space: nowrap;

        font-size: clamp(28px, 4vw, 48px);

        letter-spacing: 2px;

        animation: flicker 4s infinite;
    }}

    .subtitle {{
        position: absolute;

        top: 22vh;
        left: 50%;

        transform: translateX(-50%);

        white-space: nowrap;

        color: #999999;

        font-size: clamp(13px, 1.5vw, 18px);
    }}

    @keyframes flicker {{

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

    </style>

    <div class="screen">

        <div class="title">
            PROJECT : LOGIC
        </div>

        <div class="subtitle">
            INFORMATION IS NOT ALWAYS TRUE
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# BUTTON AREA
# =========================================================

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    st.markdown(
        """
        <style>

        div.stButton > button {{
            font-family: "NeoDungGeunMo", monospace;

            background: transparent;
            color: white;

            border: none;

            font-size: 19px;

            height: 55px;

            border-radius: 0;
        }}

        div.stButton > button:hover {{
            background: white;
            color: black;

            border: none;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # START
    # -----------------------------------------------------

    if st.button(
        "START",
        key="start_button",
        use_container_width=True,
    ):

        st.session_state["start_open"] = not st.session_state.get(
            "start_open",
            False
        )


    # -----------------------------------------------------
    # START MENU
    # -----------------------------------------------------

    if st.session_state.get("start_open", False):

        if st.button(
            "CONTINUE",
            key="continue_button",
            use_container_width=True,
        ):

            st.warning(
                "이전 플레이 기록이 존재하지 않습니다. 새 게임을 시작해주세요."
            )


        if st.button(
            "NEW GAME",
            key="new_game_button",
            use_container_width=True,
        ):

            st.switch_page("pages/2_Game.py")


    # -----------------------------------------------------
    # HOW TO PLAY
    # -----------------------------------------------------

    if st.button(
        "HOW TO PLAY",
        key="how_to_play_button",
        use_container_width=True,
    ):

        st.switch_page("pages/1_How_to_Play.py")
