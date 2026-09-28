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
# STREAMLIT STATE
# =========================================================

if "start_open" not in st.session_state:
    st.session_state.start_open = False


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

    /* =====================================================
       NATIVE STREAMLIT PAGE LINKS
       ===================================================== */

    div[data-testid="stPageLink"] {
        position: fixed !important;

        z-index: 999999 !important;

        margin: 0 !important;
        padding: 0 !important;
    }

    div[data-testid="stPageLink"] a {
        font-family: "NeoDungGeunMo", monospace !important;

        text-decoration: none !important;

        box-sizing: border-box !important;
    }


    /* =====================================================
       HOW TO PLAY NATIVE LINK
       ===================================================== */

    div[data-testid="stPageLink"].how-link {
        top: 65vh !important;
        left: 50% !important;

        transform: translateX(-50%) !important;

        width: 220px !important;
        height: 55px !important;
    }

    div[data-testid="stPageLink"].how-link a {
        width: 220px !important;
        height: 55px !important;

        display: flex !important;

        align-items: center !important;
        justify-content: center !important;

        background: transparent !important;

        border: none !important;

        color: #ffffff !important;

        font-size: 19px !important;

        cursor: pointer !important;
    }

    div[data-testid="stPageLink"].how-link a:hover {
        background: #ffffff !important;

        color: #000000 !important;
    }


    /* =====================================================
       CONTINUE / NEW GAME
       ===================================================== */

    div[data-testid="stPageLink"].continue-link,
    div[data-testid="stPageLink"].newgame-link {

        width: 190px !important;
        height: 42px !important;

        left: calc(50% + 105px) !important;

        margin: 0 !important;
        padding: 0 !important;
    }


    div[data-testid="stPageLink"].continue-link {
        top: calc(51vh - 3px) !important;
    }


    div[data-testid="stPageLink"].newgame-link {
        top: calc(51vh + 39px) !important;
    }


    div[data-testid="stPageLink"].continue-link a,
    div[data-testid="stPageLink"].newgame-link a {

        width: 190px !important;
        height: 42px !important;

        display: flex !important;

        align-items: center !important;

        padding-left: 18px !important;

        background: #050505 !important;

        color: #ffffff !important;

        border: none !important;

        font-size: 14px !important;

        cursor: pointer !important;
    }


    div[data-testid="stPageLink"].continue-link a:hover,
    div[data-testid="stPageLink"].newgame-link a:hover {

        background: #ffffff !important;

        color: #000000 !important;
    }


    /* =====================================================
       HIDE LINKS WHEN POPUP IS CLOSED
       ===================================================== */

    body:not(.popup-open)
    div[data-testid="stPageLink"].continue-link,

    body:not(.popup-open)
    div[data-testid="stPageLink"].newgame-link {

        display: none !important;
    }


    /* =====================================================
       START BUTTON
       ===================================================== */

    div[data-testid="stButton"].start-streamlit {

        position: fixed !important;

        top: 51vh !important;
        left: 50% !important;

        transform: translateX(-50%) !important;

        width: 170px !important;
        height: 55px !important;

        z-index: 999999 !important;
    }


    div[data-testid="stButton"].start-streamlit button {

        width: 170px !important;
        height: 55px !important;

        padding: 0 !important;

        background: transparent !important;

        border: none !important;

        border-radius: 0 !important;

        color: #ffffff !important;

        font-family: "NeoDungGeunMo", monospace !important;

        font-size: 19px !important;

        cursor: pointer !important;
    }


    div[data-testid="stButton"].start-streamlit button:hover {

        background: #ffffff !important;

        color: #000000 !important;
    }


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 600px) {

        div[data-testid="stPageLink"].how-link {

            top: 73vh !important;

        }

        div[data-testid="stPageLink"].continue-link,
        div[data-testid="stPageLink"].newgame-link {

            left: 50% !important;

            transform: translateX(-50%) !important;

        }

        div[data-testid="stPageLink"].continue-link {

            top: 59vh !important;

        }

        div[data-testid="stPageLink"].newgame-link {

            top: calc(59vh + 42px) !important;

        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# POPUP STATE → BODY CLASS
# =========================================================

if st.session_state.start_open:
    st.markdown(
        """
        <script>
        document.body.classList.add("popup-open");
        </script>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <script>
        document.body.classList.remove("popup-open");
        </script>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# START SCREEN HTML
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
   START VISUAL
   ===================================================== */

.start-visual {{

    position: absolute;

    top: 51vh;
    left: 50%;

    transform: translateX(-50%);

    width: 170px;
    height: 55px;

    display: flex;

    align-items: center;
    justify-content: center;

    color: #ffffff;

    font-size: 19px;

    pointer-events: none;
}}


/* =====================================================
   POPUP VISUAL
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


/* =====================================================
   POPUP SEPARATOR
   ===================================================== */

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
   HOW TO PLAY VISUAL
   ===================================================== */

.how-visual {{

    position: absolute;

    top: 65vh;
    left: 50%;

    transform: translateX(-50%);

    width: 220px;
    height: 55px;

    display: flex;

    align-items: center;
    justify-content: center;

    color: #ffffff;

    font-family: "NeoDungGeunMo", monospace;

    font-size: 19px;

    pointer-events: none;
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


    <!-- START VISUAL -->

    <div class="start-visual">
        START
    </div>


    <!-- POPUP VISUAL -->

    <div
        id="popupVisual"
        class="popup-visual"
    >

    </div>


    <!-- HOW TO PLAY VISUAL -->

    <div class="how-visual">
        HOW TO PLAY
    </div>


</div>


</body>

</html>
"""


# =========================================================
# RENDER HTML
# =========================================================

components.html(
    html,
    height=900,
    scrolling=False,
)


# =========================================================
# NATIVE STREAMLIT CONTROLS
# =========================================================

# START
st.markdown(
    '<div class="start-streamlit">',
    unsafe_allow_html=True,
)

start_clicked = st.button(
    "START",
    key="start_button",
    use_container_width=False,
)

st.markdown(
    "</div>",
    unsafe_allow_html=True,
)


if start_clicked:
    st.session_state.start_open = not st.session_state.start_open
    st.rerun()


# =========================================================
# PAGE LINKS
# =========================================================

# HOW TO PLAY
st.markdown(
    '<div class="how-link">',
    unsafe_allow_html=True,
)

st.page_link(
    "pages/1_How_To_Play.py",
    label="HOW TO PLAY",
)

st.markdown(
    "</div>",
    unsafe_allow_html=True,
)


# CONTINUE
if st.session_state.start_open:

    st.markdown(
        '<div class="continue-link">',
        unsafe_allow_html=True,
    )

    st.page_link(
        "pages/1_How_To_Play.py",
        label="CONTINUE",
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


    # NEW GAME
    st.markdown(
        '<div class="newgame-link">',
        unsafe_allow_html=True,
    )

    st.page_link(
        "pages/2_Game.py",
        label="NEW GAME",
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )
