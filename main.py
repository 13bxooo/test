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
    initial_sidebar_state="collapsed"
)


# =========================================================
# FONT LOAD
# =========================================================

# GitHub에는 neodgm.ttf로 올리는 것을 권장
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
# QUERY ACTION
# =========================================================

action = st.query_params.get("action")


if action == "new_game":

    st.query_params.clear()

    st.switch_page("pages/1_Game.py")


elif action == "continue":

    st.query_params.clear()

    st.warning(
        "이전 플레이 기록이 존재하지 않습니다. "
        "새 게임을 시작해주세요."
    )


elif action == "how_to_play":

    st.query_params.clear()

    st.switch_page("pages/2_How_to_Play.py")


# =========================================================
# STREAMLIT UI HIDE
# =========================================================

st.markdown(
    """
    <style>

    html,
    body {

        margin: 0 !important;
        padding: 0 !important;

        background: #000000 !important;
    }


    .stApp {

        background: #000000 !important;

        margin: 0 !important;
        padding: 0 !important;
    }


    [data-testid="stAppViewContainer"] {

        background: #000000 !important;
    }


    [data-testid="stHeader"] {

        display: none !important;
    }


    [data-testid="stSidebar"] {

        display: none !important;
    }


    #MainMenu {

        visibility: hidden !important;
    }


    footer {

        visibility: hidden !important;
    }


    .block-container {

        padding: 0 !important;
        margin: 0 !important;

        max-width: none !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# GAME START SCREEN
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

    src: url(
        "data:font/ttf;base64,{font_data}"
    ) format("truetype");

    font-weight: normal;

    font-style: normal;
}}


/* =====================================================
   RESET
   ===================================================== */

* {{

    box-sizing: border-box;

}}


html,
body {{

    width: 100%;
    height: 100%;

    margin: 0;
    padding: 0;

    overflow: hidden;

    background: #000000;

}}


/* =====================================================
   전체 화면
   ===================================================== */

.screen {{

    position: fixed;

    inset: 0;

    width: 100vw;
    height: 100vh;

    background: #000000;

    color: #ffffff;

    font-family:
        "NeoDungGeunMo",
        monospace;

    overflow: hidden;

}}


/* =====================================================
   PROJECT : LOGIC
   ===================================================== */

.title {{

    position: fixed;

    top: 12vh;

    left: 50%;

    transform: translateX(-50%);

    color: #ffffff;

    font-family:
        "NeoDungGeunMo",
        monospace;

    font-size: clamp(32px, 4vw, 58px);

    font-weight: normal;

    letter-spacing: 0.12em;

    white-space: nowrap;

    text-align: center;

    z-index: 10;

    text-shadow:
        0 0 4px rgba(255,255,255,0.85),
        0 0 12px rgba(255,255,255,0.25);

    animation:
        title-flicker
        4.2s
        infinite;

}}


/* =====================================================
   SUBTITLE
   ===================================================== */

.subtitle {{

    position: fixed;

    top: 22vh;

    left: 50%;

    transform: translateX(-50%);

    color: #9a9a9a;

    font-family:
        "NeoDungGeunMo",
        monospace;

    font-size: clamp(10px, 1.1vw, 15px);

    letter-spacing: 0.25em;

    white-space: nowrap;

    text-align: center;

    z-index: 10;

}}


/* =====================================================
   START
   ===================================================== */

.start {{

    position: fixed;

    top: 51vh;

    left: 50%;

    transform: translateX(-50%);

    width: 170px;

    height: 55px;

    display: flex;

    align-items: center;

    justify-content: center;

    color: #ffffff;

    font-family:
        "NeoDungGeunMo",
        monospace;

    font-size: 22px;

    letter-spacing: 0.12em;

    cursor: pointer;

    user-select: none;

    z-index: 20;

}}


.start:hover {{

    text-shadow:
        0 0 5px rgba(255,255,255,0.5);

}}


/* =====================================================
   START POPUP
   ===================================================== */

.popup {{

    position: fixed;

    top: calc(51vh - 3px);

    left: calc(50% + 105px);

    width: 190px;

    padding: 7px 0;

    background: #080808;

    border: 1px solid #555555;

    box-shadow:
        0 0 0 1px #111111,
        0 0 12px rgba(255,255,255,0.08);

    display: none;

    z-index: 30;

    animation:
        popup-appear
        0.12s
        steps(2, end);

}}


.popup.show {{

    display: block;

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

    color: #ffffff;

    font-family:
        "NeoDungGeunMo",
        monospace;

    font-size: 14px;

    letter-spacing: 0.1em;

    cursor: pointer;

    user-select: none;

}}


.popup-button + .popup-button {{

    border-top: 1px solid #222222;

}}


/* =====================================================
   POPUP HOVER FLICKER
   ===================================================== */

.popup-button:hover {{

    background: #ffffff;

    color: #000000;

    animation:
        menu-flicker
        0.55s
        steps(1, end)
        infinite;

}}


/* =====================================================
   HOW TO PLAY
   ===================================================== */

.how {{

    position: fixed;

    top: 65vh;

    left: 50%;

    transform: translateX(-50%);

    width: 220px;

    height: 55px;

    display: flex;

    align-items: center;

    justify-content: center;

    color: #ffffff;

    font-family:
        "NeoDungGeunMo",
        monospace;

    font-size: 17px;

    letter-spacing: 0.12em;

    cursor: pointer;

    user-select: none;

    z-index: 20;

}}


.how:hover {{

    text-shadow:
        0 0 5px rgba(255,255,255,0.5);

}}


/* =====================================================
   PROJECT : LOGIC FLICKER
   ===================================================== */

@keyframes title-flicker {{

    0%,
    4% {{
        opacity: 1;
    }}

    5% {{
        opacity: 0.45;
    }}

    6% {{
        opacity: 1;
    }}

    13% {{
        opacity: 1;
    }}

    14% {{
        opacity: 0.2;
    }}

    15% {{
        opacity: 0.85;
    }}

    16% {{
        opacity: 1;
    }}

    38% {{
        opacity: 1;
    }}

    39% {{
        opacity: 0.4;
    }}

    40% {{
        opacity: 0.1;
    }}

    41% {{
        opacity: 0.9;
    }}

    42% {{
        opacity: 1;
    }}

    70% {{
        opacity: 1;
    }}

    71% {{
        opacity: 0.3;
    }}

    72% {{
        opacity: 1;
    }}

    100% {{
        opacity: 1;
    }}

}}


/* =====================================================
   MENU FLICKER
   ===================================================== */

@keyframes menu-flicker {{

    0% {{
        opacity: 1;
    }}

    18% {{
        opacity: 0.15;
    }}

    19% {{
        opacity: 1;
    }}

    38% {{
        opacity: 0.35;
    }}

    39% {{
        opacity: 1;
    }}

    60% {{
        opacity: 0.1;
    }}

    61% {{
        opacity: 1;
    }}

    80% {{
        opacity: 0.45;
    }}

    81% {{
        opacity: 1;
    }}

    100% {{
        opacity: 1;
    }}

}}


/* =====================================================
   POPUP APPEAR
   ===================================================== */

@keyframes popup-appear {{

    0% {{

        opacity: 0;

        transform:
            translateX(-8px);

    }}

    100% {{

        opacity: 1;

        transform:
            translateX(0);

    }}

}}


/* =====================================================
   SMALL SCREEN
   ===================================================== */

@media (max-width: 700px) {{

    .title {{

        top: 12vh;

        font-size: 30px;

    }}


    .subtitle {{

        top: 21vh;

        font-size: 9px;

    }}


    .start {{

        top: 51vh;

    }}


    .popup {{

        top: 59vh;

        left: 50%;

        transform:
            translateX(-50%);

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

    <div
        class="start"
        id="start"
    >

        START

    </div>


    <!-- =================================================
         START POPUP
         ================================================= -->

    <div
        class="popup"
        id="popup"
    >

        <div
            class="popup-button"
            id="continue"
        >

            CONTINUE

        </div>


        <div
            class="popup-button"
            id="new-game"
        >

            NEW GAME

        </div>

    </div>


    <!-- =================================================
         HOW TO PLAY
         ================================================= -->

    <div
        class="how"
        id="how"
    >

        HOW TO PLAY

    </div>


</div>


<script>

/* =====================================================
   START → POPUP
   ===================================================== */

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


/* =====================================================
   NEW GAME
   ===================================================== */

document
    .getElementById("new-game")
    .addEventListener(
        "click",
        function() {{

            window.parent.location.href =
                "?action=new_game";

        }}
    );


/* =====================================================
   CONTINUE
   ===================================================== */

document
    .getElementById("continue")
    .addEventListener(
        "click",
        function() {{

            window.parent.location.href =
                "?action=continue";

        }}
    );


/* =====================================================
   HOW TO PLAY
   ===================================================== */

document
    .getElementById("how")
    .addEventListener(
        "click",
        function() {{

            window.parent.location.href =
                "?action=how_to_play";

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
    scrolling=False
)
