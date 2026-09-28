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
# SESSION STATE
# =========================================================

if "start_open" not in st.session_state:
    st.session_state.start_open = False


# =========================================================
# GLOBAL CSS
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
       STREAMLIT UI HIDE
       ===================================================== */

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
       ALL NATIVE CONTROLS
       ===================================================== */

    div[data-testid="stButton"],
    div[data-testid="stPageLink"] {{
        position: fixed !important;

        z-index: 1000000 !important;

        margin: 0 !important;
        padding: 0 !important;
    }}


    /* =====================================================
       START
       ===================================================== */

    div[data-testid="stButton"] {{
        top: 51vh !important;
        left: 50% !important;

        width: 170px !important;
        height: 55px !important;

        transform: translateX(-50%) !important;
    }}

    div[data-testid="stButton"] button {{
        width: 170px !important;
        height: 55px !important;

        padding: 0 !important;

        background: transparent !important;

        border: none !important;
        border-radius: 0 !important;

        color: #ffffff !important;

        font-family: "NeoDungGeunMo", monospace !important;
        font-size: 14px !important;
        font-weight: normal !important;

        cursor: pointer !important;
    }}

    div[data-testid="stButton"] button:hover {{
        background: #ffffff !important;
        color: #000000 !important;
    }}


    /* =====================================================
       HOW TO PLAY
       ===================================================== */

    div[data-testid="stPageLink"] a {{
        text-decoration: none !important;

        font-family: "NeoDungGeunMo", monospace !important;
        font-weight: normal !important;
    }}


    /*
       첫 번째 PageLink = HOW TO PLAY
    */

    div[data-testid="stPageLink"]:nth-of-type(1) {{
        top: 65vh !important;
        left: 50% !important;

        width: 220px !important;
        height: 55px !important;

        transform: translateX(-50%) !important;
    }}

    div[data-testid="stPageLink"]:nth-of-type(1) a {{
        width: 220px !important;
        height: 55px !important;

        display: flex !important;

        align-items: center !important;
        justify-content: center !important;

        padding: 0 !important;

        background: transparent !important;

        border: none !important;

        color: #ffffff !important;

        font-family: "NeoDungGeunMo", monospace !important;
        font-size: 14px !important;

        text-decoration: none !important;

        cursor: pointer !important;
    }}

    div[data-testid="stPageLink"]:nth-of-type(1) a:hover {{
        background: #ffffff !important;
        color: #000000 !important;
    }}


    /* =====================================================
       CONTINUE / NEW GAME
       ===================================================== */

    /*
       두 번째 PageLink = CONTINUE
       세 번째 PageLink = NEW GAME
    */

    div[data-testid="stPageLink"]:nth-of-type(2),
    div[data-testid="stPageLink"]:nth-of-type(3) {{
        left: calc(50% + 105px) !important;

        width: 190px !important;
        height: 42px !important;

        transform: none !important;

        z-index: 1000001 !important;
    }}


    /* CONTINUE */

    div[data-testid="stPageLink"]:nth-of-type(2) {{
        top: calc(51vh - 3px) !important;
    }}


    /* NEW GAME */

    div[data-testid="stPageLink"]:nth-of-type(3) {{
        top: calc(51vh + 39px) !important;
    }}


    div[data-testid="stPageLink"]:nth-of-type(2) a,
    div[data-testid="stPageLink"]:nth-of-type(3) a {{
        width: 190px !important;
        height: 42px !important;

        display: flex !important;

        align-items: center !important;
        justify-content: flex-start !important;

        padding: 0 0 0 18px !important;

        background: #050505 !important;

        border: none !important;

        color: #ffffff !important;

        font-family: "NeoDungGeunMo", monospace !important;
        font-size: 14px !important;

        text-decoration: none !important;

        cursor: pointer !important;
    }}


    div[data-testid="stPageLink"]:nth-of-type(2) a:hover,
    div[data-testid="stPageLink"]:nth-of-type(3) a:hover {{
        background: #ffffff !important;
        color: #000000 !important;
    }}


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 600px) {{

        div[data-testid="stPageLink"]:nth-of-type(1) {{
            top: 73vh !important;
        }}

        div[data-testid="stPageLink"]:nth-of-type(2) {{
            top: calc(59vh - 3px) !important;
            left: calc(50% - 95px) !important;
        }}

        div[data-testid="stPageLink"]:nth-of-type(3) {{
            top: calc(59vh + 39px) !important;
            left: calc(50% - 95px) !important;
        }}

    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# START SCREEN HTML
# =========================================================

popup_class = "show" if st.session_state.start_open else ""

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
   POPUP BACKGROUND VISUAL
   ===================================================== */

.popup-visual {{
    position: absolute;

    top: calc(51vh - 3px);
    left: calc(50% + 105px);

    width: 190px;
    height: 84px;

    background: #050505;

    border: 1px solid #ffffff;

    opacity: 0;

    visibility: hidden;

    transition:
        opacity 0.15s ease,
        visibility 0.15s;
}}


.popup-visual.show {{
    opacity: 1;
    visibility: visible;
}}


.popup-visual::after {{
    content: "";

    position: absolute;

    left: 0;
    top: 42px;

    width: 100%;
    height: 1px;

    background: #222222;
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

    .popup-visual {{
        top: 59vh;
        left: 50%;

        transform: translateX(-50%);
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

    <div class="popup-visual {popup_class}">
    </div>

</div>

</body>

</html>
"""


# =========================================================
# RENDER BACKGROUND
# =========================================================

components.html(
    html,
    height=900,
    scrolling=False,
)


# =========================================================
# START BUTTON
# =========================================================

start_clicked = st.button(
    "START",
    key="start_button",
)


if start_clicked:
    st.session_state.start_open = not st.session_state.start_open
    st.rerun()


# =========================================================
# HOW TO PLAY
# =========================================================

st.page_link(
    "pages/1_How_To_Play.py",
    label="HOW TO PLAY",
)


# =========================================================
# POPUP
# =========================================================

if st.session_state.start_open:

    st.page_link(
        "pages/1_How_To_Play.py",
        label="CONTINUE",
    )

    st.page_link(
        "pages/2_Game.py",
        label="NEW GAME",
    )
