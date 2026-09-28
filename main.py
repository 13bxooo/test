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
# SESSION STATE
# =========================================================

if "start_open" not in st.session_state:
    st.session_state.start_open = False


# =========================================================
# FONT
# =========================================================

font_candidates = [
    Path("neodgm.ttf"),
    Path("neodgm(2).ttf"),
]

font_path = next(
    (path for path in font_candidates if path.exists()),
    None,
)

font_data = ""

if font_path:
    font_data = base64.b64encode(
        font_path.read_bytes()
    ).decode("utf-8")


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

        src: url(
            "data:font/ttf;base64,{font_data}"
        ) format("truetype");

        font-weight: normal;
        font-style: normal;
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

    [data-testid="stSidebarCollapsedControl"] {{
        display: none;
    }}


    /* =====================================================
       MAIN PAGE
       ===================================================== */

    .stApp {{
        background: #000000 !important;
        overflow: hidden !important;
    }}

    .main {{
        background: #000000 !important;
    }}

    .block-container {{
        padding: 0 !important;
        margin: 0 !important;
        max-width: none !important;
    }}


    /* =====================================================
       START
       ===================================================== */

    div[data-testid="stButton"] {{
        position: fixed !important;

        top: 51vh !important;
        left: 50% !important;

        width: 170px !important;
        height: 55px !important;

        transform: translateX(-50%) !important;

        z-index: 1000000 !important;

        margin: 0 !important;
        padding: 0 !important;
    }}

    div[data-testid="stButton"] button {{
        width: 170px !important;
        height: 55px !important;

        padding: 0 !important;
        margin: 0 !important;

        background: transparent !important;

        border: none !important;
        border-radius: 0 !important;

        box-shadow: none !important;

        color: #ffffff !important;

        font-family: "NeoDungGeunMo", monospace !important;
        font-size: 19px !important;
        font-weight: normal !important;

        transition:
            background-color 0.08s linear,
            color 0.08s linear !important;
    }}

    div[data-testid="stButton"] button:hover {{
        background: #ffffff !important;
        color: #000000 !important;

        border: none !important;
    }}

    div[data-testid="stButton"] button:focus {{
        outline: none !important;
        box-shadow: none !important;
    }}


    /* =====================================================
       HOW TO PLAY
       ===================================================== */

    div[data-testid="stPageLink"] {{
        position: fixed !important;

        z-index: 1000000 !important;

        margin: 0 !important;
        padding: 0 !important;
    }}

    div[data-testid="stPageLink"] a {{
        font-family: "NeoDungGeunMo", monospace !important;

        text-decoration: none !important;

        font-weight: normal !important;
    }}

    .how-link {{
        position: fixed !important;

        top: 65vh !important;
        left: 50% !important;

        width: 220px !important;
        height: 55px !important;

        transform: translateX(-50%) !important;

        z-index: 1000000 !important;

        margin: 0 !important;
        padding: 0 !important;
    }}

    .how-link a {{
        width: 220px !important;
        height: 55px !important;

        display: flex !important;

        align-items: center !important;
        justify-content: center !important;

        padding: 0 !important;
        margin: 0 !important;

        background: transparent !important;

        color: #ffffff !important;

        font-family: "NeoDungGeunMo", monospace !important;
        font-size: 19px !important;
        font-weight: normal !important;

        border: none !important;
        border-radius: 0 !important;

        box-shadow: none !important;

        transition:
            background-color 0.08s linear,
            color 0.08s linear !important;
    }}

    .how-link a:hover {{
        background: #ffffff !important;
        color: #000000 !important;
    }}


    /* =====================================================
       POPUP
       ===================================================== */

    .popup-box {{
        position: fixed !important;

        top: calc(51vh - 3px) !important;
        left: calc(50% + 105px) !important;

        width: 190px !important;
        height: 84px !important;

        background: #050505 !important;

        border: 1px solid #ffffff !important;

        box-sizing: border-box !important;

        z-index: 999998 !important;

        pointer-events: none !important;
    }}


    /* =====================================================
       CONTINUE
       ===================================================== */

    .continue-link {{
        position: fixed !important;

        top: calc(51vh - 3px) !important;
        left: calc(50% + 105px) !important;

        width: 190px !important;
        height: 42px !important;

        z-index: 1000001 !important;

        margin: 0 !important;
        padding: 0 !important;
    }}

    .continue-link a {{
        width: 190px !important;
        height: 42px !important;

        display: flex !important;

        align-items: center !important;
        justify-content: center !important;

        padding: 0 !important;
        margin: 0 !important;

        background: transparent !important;

        color: #ffffff !important;

        font-family: "NeoDungGeunMo", monospace !important;
        font-size: 17px !important;
        font-weight: normal !important;

        text-decoration: none !important;

        border: none !important;
        border-radius: 0 !important;

        box-shadow: none !important;

        transition:
            background-color 0.08s linear,
            color 0.08s linear !important;
    }}

    .continue-link a:hover {{
        background: #ffffff !important;
        color: #000000 !important;
    }}


    /* =====================================================
       NEW GAME
       ===================================================== */

    .newgame-link {{
        position: fixed !important;

        top: calc(51vh + 39px) !important;
        left: calc(50% + 105px) !important;

        width: 190px !important;
        height: 42px !important;

        z-index: 1000001 !important;

        margin: 0 !important;
        padding: 0 !important;
    }}

    .newgame-link a {{
        width: 190px !important;
        height: 42px !important;

        display: flex !important;

        align-items: center !important;
        justify-content: center !important;

        padding: 0 !important;
        margin: 0 !important;

        background: transparent !important;

        color: #ffffff !important;

        font-family: "NeoDungGeunMo", monospace !important;
        font-size: 17px !important;
        font-weight: normal !important;

        text-decoration: none !important;

        border: none !important;
        border-radius: 0 !important;

        box-shadow: none !important;

        transition:
            background-color 0.08s linear,
            color 0.08s linear !important;
    }}

    .newgame-link a:hover {{
        background: #ffffff !important;
        color: #000000 !important;
    }}


    /* =====================================================
       REMOVE STREAMLIT PAGE LINK DEFAULT EFFECTS
       ===================================================== */

    div[data-testid="stPageLink"] a:focus {{
        outline: none !important;
        box-shadow: none !important;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# TITLE SCREEN
# =========================================================

popup_class = "popup-visible" if st.session_state.start_open else ""

title_screen = f"""
<style>

    .logic-screen {{
        position: fixed;

        inset: 0;

        width: 100vw;
        height: 100vh;

        background: #000000;

        overflow: hidden;

        pointer-events: none;

        z-index: 1;
    }}


    /* =====================================================
       TITLE
       ===================================================== */

    .logic-title {{
        position: absolute;

        top: 29vh;
        left: 50%;

        transform: translateX(-50%);

        width: 100%;

        text-align: center;

        color: #ffffff;

        font-family: "NeoDungGeunMo", monospace;

        font-size: clamp(38px, 5vw, 72px);

        letter-spacing: 3px;

        white-space: nowrap;

        animation:
            title-flicker
            4.2s
            infinite;
    }}


    /* =====================================================
       SUBTITLE
       ===================================================== */

    .logic-subtitle {{
        position: absolute;

        top: 39vh;
        left: 50%;

        transform: translateX(-50%);

        width: 100%;

        text-align: center;

        color: #ffffff;

        font-family: "NeoDungGeunMo", monospace;

        font-size: 16px;

        letter-spacing: 2px;

        white-space: nowrap;

        opacity: 0.82;
    }}


    /* =====================================================
       TITLE FLICKER
       ===================================================== */

    @keyframes title-flicker {{

        0% {{
            opacity: 1;
        }}

        3% {{
            opacity: 0.92;
        }}

        4% {{
            opacity: 0.35;
        }}

        5% {{
            opacity: 1;
        }}

        38% {{
            opacity: 1;
        }}

        39% {{
            opacity: 0.55;
        }}

        40% {{
            opacity: 1;
        }}

        71% {{
            opacity: 1;
        }}

        72% {{
            opacity: 0.25;
        }}

        73% {{
            opacity: 0.85;
        }}

        74% {{
            opacity: 1;
        }}

        100% {{
            opacity: 1;
        }}

    }}

</style>

<div class="logic-screen">

    <div class="logic-title">
        PROJECT : LOGIC
    </div>

    <div class="logic-subtitle">
        INFORMATION IS NOT ALWAYS TRUE
    </div>

</div>
"""


components.html(
    title_screen,
    height=900,
    scrolling=False,
)


# =========================================================
# START
# =========================================================

start_clicked = st.button(
    "START",
    key="start_button",
)

if start_clicked:
    st.session_state.start_open = (
        not st.session_state.start_open
    )

    st.rerun()


# =========================================================
# HOW TO PLAY
# =========================================================

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


# =========================================================
# POPUP
# =========================================================

if st.session_state.start_open:

    # -----------------------------------------------------
    # Popup background
    # -----------------------------------------------------

    st.markdown(
        """
        <div class="popup-box"></div>
        """,
        unsafe_allow_html=True,
    )


    # -----------------------------------------------------
    # CONTINUE
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # NEW GAME
    # -----------------------------------------------------

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
