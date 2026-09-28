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

font_path = None

for candidate in font_candidates:
    if candidate.exists():
        font_path = candidate
        break

if font_path is not None:
    with open(font_path, "rb") as f:
        font_data = base64.b64encode(f.read()).decode("utf-8")
else:
    font_data = ""


# =========================================================
# HIDE STREAMLIT UI
# =========================================================

st.markdown(
    """
    <style>

    #MainMenu {
        visibility: hidden !important;
    }

    header {
        visibility: hidden !important;
    }

    footer {
        visibility: hidden !important;
    }

    [data-testid="stSidebar"] {
        display: none !important;
    }

    [data-testid="collapsedControl"] {
        display: none !important;
    }

    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    .stApp {
        background: #000000 !important;
    }


    /* =====================================================
       HOW TO PLAY - STREAMLIT NATIVE PAGE LINK
       ===================================================== */

    div[data-testid="stPageLink-NavLink"] {
        position: fixed !important;

        top: 65vh !important;
        left: 50% !important;

        transform: translateX(-50%) !important;

        width: 220px !important;
        height: 55px !important;

        z-index: 9999 !important;
    }

    div[data-testid="stPageLink-NavLink"] a {
        width: 100% !important;
        height: 100% !important;

        display: flex !important;

        align-items: center !important;
        justify-content: center !important;

        background: transparent !important;

        border: none !important;
        border-radius: 0 !important;

        color: white !important;

        font-family: "NeoDungGeunMo", monospace !important;

        font-size: 19px !important;

        text-decoration: none !important;
    }

    div[data-testid="stPageLink-NavLink"] a:hover {
        background: white !important;
        color: black !important;
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

.screen {{

    position: fixed;

    inset: 0;

    width: 100vw;
    height: 100vh;

    background: #000000;

    color: #ffffff;

    font-family: "NeoDungGeunMo", monospace;

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

    color: #ffffff;

    font-size: clamp(28px, 4vw, 48px);

    letter-spacing: 2px;

    animation: title-flicker 4s infinite;

}}


/* =====================================================
   SUBTITLE
   ===================================================== */

.subtitle {{

    position: absolute;

    top: 22vh;
    left: 50%;

    transform: translateX(-50%);

    white-space: nowrap;

    color: #999999;

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

    font-size: 19px;

    cursor: pointer;

}}


.start:hover {{

    background: #ffffff;

    color: #000000;

}}


/* =====================================================
   POPUP
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

}}


.popup-button:hover {{

    background: #ffffff;

    color: #000000;

}}


/* =====================================================
   FLICKER
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

}}

</style>

</head>


<body>

<div class="screen">


    <div class="title">
        PROJECT : LOGIC
    </div>


    <div class="subtitle">
        INFORMATION IS NOT ALWAYS TRUE
    </div>


    <!-- START -->

    <button
        id="start"
        class="start"
    >
        START
    </button>


    <!-- START POPUP -->

    <div
        id="popup"
        class="popup"
    >

        <button
            id="continue"
            class="popup-button"
        >
            CONTINUE
        </button>

        <button
            id="new-game"
            class="popup-button"
        >
            NEW GAME
        </button>

    </div>


</div>


<script>

const start = document.getElementById("start");
const popup = document.getElementById("popup");


start.addEventListener("click", function() {{

    popup.classList.toggle("show");

}});


// CONTINUE

document
    .getElementById("continue")
    .addEventListener("click", function() {{

        window.parent.location.href = "?action=continue";

    }});


// NEW GAME

document
    .getElementById("new-game")
    .addEventListener("click", function() {{

        window.parent.location.href = "?action=new_game";

    }});

</script>

</body>

</html>
"""


components.html(
    html,
    height=900,
    scrolling=False,
)


# =========================================================
# HOW TO PLAY
# =========================================================
#
# components.html 밖에서 실제 Streamlit 페이지 링크를 생성한다.
# 따라서 Streamlit이 페이지 이동을 직접 처리한다.
#

# =========================================================
# HOW TO PLAY BUTTON
# =========================================================

st.markdown(
    """
    <style>

    div.stButton {
        position: fixed !important;

        top: 65vh !important;
        left: 50% !important;

        transform: translateX(-50%) !important;

        width: 220px !important;
        height: 55px !important;

        z-index: 99999 !important;
    }

    div.stButton > button {
        width: 220px !important;
        height: 55px !important;

        background: transparent !important;

        border: none !important;
        border-radius: 0 !important;

        color: white !important;

        font-family: "NeoDungGeunMo", monospace !important;

        font-size: 19px !important;

        box-shadow: none !important;
    }

    div.stButton > button:hover {
        background: white !important;

        color: black !important;

        border: none !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


if st.button("HOW TO PLAY", key="how_to_play_button"):
    st.switch_page("pages/1_How_To_Play.py")
