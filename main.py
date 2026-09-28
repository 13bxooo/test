import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


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
# PAGE ROUTING
# =========================================================

action = st.query_params.get("action")


if action == "how_to_play":
    st.query_params.clear()
    st.switch_page("pages/1_How_To_Play.py")


elif action == "new_game":
    st.query_params.clear()

    # 나중에 게임 페이지가 만들어지면 연결
    # st.switch_page("pages/2_Game.py")

    st.info("GAME SYSTEM은 현재 준비 중입니다.")


elif action == "continue":
    st.query_params.clear()

    st.warning(
        "이전 플레이 기록이 존재하지 않습니다. 새 게임을 시작해주세요."
    )


# =========================================================
# HIDE STREAMLIT UI
# =========================================================

st.markdown(
    """
    <style>

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    .stApp {
        background: #000000;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# START SCREEN
# =========================================================

html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<style>

/* =====================================================
   FONT
   ===================================================== */

@font-face {{
    font-family: "NeoDungGeunMo";
    src: url(data:font/ttf;base64,{font_data});
}}


* {{
    box-sizing: border-box;
}}


html,
body {{
    margin: 0;
    padding: 0;

    width: 100%;
    height: 100%;

    overflow: hidden;

    background: #000000;
}}


body {{
    font-family: "NeoDungGeunMo", monospace;
}}


/* =====================================================
   SCREEN
   ===================================================== */

.screen {{
    position: fixed;

    inset: 0;

    width: 100vw;
    height: 100vh;

    background: #000000;

    color: #ffffff;
}}


/* =====================================================
   TITLE
   ===================================================== */

.title {{
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


.subtitle {{
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
   START
   ===================================================== */

.start {{
    position: absolute;

    top: 51vh;
    left: 50%;

    transform: translateX(-50%);

    width: 170px;
    height: 55px;

    display: flex;

    align-items: center;
    justify-content: center;

    background: transparent;

    border: none;

    color: #ffffff;

    font-family: "NeoDungGeunMo", monospace;

    font-size: 14px;

    cursor: pointer;

    user-select: none;
}}


.start:hover {{
    background: #ffffff;

    color: #000000;
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

    opacity: 0;

    visibility: hidden;

    transform: translateX(-10px);

    transition:
        opacity 0.15s ease,
        transform 0.15s ease,
        visibility 0.15s;
}}


.popup.show {{
    opacity: 1;

    visibility: visible;

    transform: translateX(0);
}}


/* =====================================================
   POPUP BUTTON
   ===================================================== */

.popup-button {{
    width: 100%;
    height: 42px;

    display: flex;

    align-items: center;

    padding-left: 18px;

    background: #050505;

    border: none;

    color: #ffffff;

    font-family: "NeoDungGeunMo", monospace;

    font-size: 14px;

    text-align: left;

    cursor: pointer;

    text-decoration: none;
}}


.popup-button:hover {{
    background: #ffffff;

    color: #000000;
}}


/* =====================================================
   HOW TO PLAY
   ===================================================== */

.how {{
    position: absolute;

    top: 65vh;
    left: 50%;

    transform: translateX(-50%);

    width: 220px;
    height: 55px;

    display: flex;

    align-items: center;
    justify-content: center;

    background: transparent;

    border: none;

    color: #ffffff;

    font-family: "NeoDungGeunMo", monospace;

    font-size: 14px;

    cursor: pointer;

    user-select: none;

    text-decoration: none;
}}


.how:hover {{
    background: #ffffff;

    color: #000000;
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

    .title {{
        top: 12vh;
        font-size: 30px;
    }}

    .subtitle {{
        top: 22vh;
        font-size: 12px;
    }}

    .start {{
        top: 51vh;
    }}

    .popup {{
        top: 59vh;
        left: 50%;

        transform: translateX(-50%);
    }}

    .popup.show {{
        transform: translateX(-50%);
    }}

    .how {{
        top: 73vh;
    }}

}}

</style>

</head>


<body>

<div class="screen">


    <!-- =================================================
         TITLE
         ================================================= -->

    <div class="title">
        PROJECT : LOGIC
    </div>


    <div class="subtitle">
        INFORMATION IS NOT ALWAYS TRUE
    </div>


    <!-- =================================================
         START
         ================================================= -->

    <button
        id="start"
        class="start"
    >
        START
    </button>


    <!-- =================================================
         START POPUP
         ================================================= -->

    <div
        id="popup"
        class="popup"
    >

        <a
            class="popup-button"
            href="?action=continue"
            target="_top"
        >
            CONTINUE
        </a>


        <a
            class="popup-button"
            href="?action=new_game"
            target="_top"
        >
            NEW GAME
        </a>

    </div>


    <!-- =================================================
         HOW TO PLAY
         ================================================= -->

    <a
        class="how"
        href="?action=how_to_play"
        target="_top"
    >
        HOW TO PLAY
    </a>


</div>


<script>

/* =======================================================
   START BUTTON
   ======================================================= */

const start =
    document.getElementById("start");

const popup =
    document.getElementById("popup");


start.addEventListener(
    "click",
    function() {{

        popup.classList.toggle("show");

    }}
);

</script>


</body>

</html>
"""


# =========================================================
# RENDER
# =========================================================

components.html(
    html,
    height=900,
    scrolling=False,
)
