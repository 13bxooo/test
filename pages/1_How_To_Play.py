import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="HOW TO PLAY | PROJECT : LOGIC",
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

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# HOW TO PLAY
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


/* =====================================================
   RESET
   ===================================================== */

* {{
    box-sizing: border-box;
}}


html,
body {{

    margin: 0;
    padding: 0;

    width: 100%;
    height: 100%;

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

    overflow-y: auto;

}}


/* =====================================================
   TOP BAR
   ===================================================== */

.top-bar {{

    position: absolute;

    top: 24px;

    left: 35px;
    right: 35px;

    display: flex;

    justify-content: space-between;

    align-items: center;

    color: #777777;

    font-size: 14px;

}}


.system-status {{

    color: #ffffff;

}}


/* =====================================================
   TITLE
   ===================================================== */

.page-title {{

    position: absolute;

    top: 70px;

    left: 50%;

    transform: translateX(-50%);

    white-space: nowrap;

    color: #ffffff;

    font-size: 32px;

    letter-spacing: 2px;

}}


.page-subtitle {{

    position: absolute;

    top: 112px;

    left: 50%;

    transform: translateX(-50%);

    white-space: nowrap;

    color: #777777;

    font-size: 13px;

    letter-spacing: 1px;

}}


/* =====================================================
   CONTENT
   ===================================================== */

.content {{

    position: absolute;

    top: 165px;

    left: 50%;

    transform: translateX(-50%);

    width: min(850px, 88vw);

    padding-bottom: 130px;

}}


/* =====================================================
   SECTION
   ===================================================== */

.section {{

    margin-bottom: 22px;

    border: 1px solid #3d4650;

    background: #080b0f;

}}


.section-title {{

    padding: 11px 16px;

    background: #111820;

    border-bottom: 1px solid #3d4650;

    color: #ffffff;

    font-size: 15px;

}}


.section-body {{

    padding: 15px 17px;

    color: #bdbdbd;

    font-size: 14px;

    line-height: 1.8;

}}


/* =====================================================
   CONTROL
   ===================================================== */

.control-row {{

    display: flex;

    align-items: center;

    gap: 18px;

    min-height: 48px;

    border-bottom: 1px solid #20262d;

}}


.control-row:last-child {{

    border-bottom: none;

}}


.key {{

    width: 105px;

    min-width: 105px;

    height: 32px;

    display: flex;

    align-items: center;

    justify-content: center;

    background: #eeeeee;

    color: #000000;

    border: 2px solid #ffffff;

    font-size: 13px;

}}


.description {{

    color: #bdbdbd;

    font-size: 13px;

}}


/* =====================================================
   WARNING
   ===================================================== */

.warning {{

    color: #d4d4d4;

    border-left: 3px solid #ffffff;

    padding-left: 13px;

    margin-top: 5px;

}}


/* =====================================================
   BACK BUTTON
   ===================================================== */

.back-button {{

    position: fixed;

    bottom: 30px;

    left: 50%;

    transform: translateX(-50%);

    width: 210px;

    height: 48px;

    display: flex;

    align-items: center;

    justify-content: center;

    background: #000000;

    border: 1px solid #ffffff;

    color: #ffffff;

    font-family: "NeoDungGeunMo", monospace;

    font-size: 15px;

    cursor: pointer;

}}


.back-button:hover {{

    background: #ffffff;

    color: #000000;

}}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {{

    margin-top: 30px;

    text-align: center;

    color: #4f555c;

    font-size: 11px;

}}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 600px) {{

    .top-bar {{

        left: 18px;
        right: 18px;

    }}

    .page-title {{

        top: 70px;

        font-size: 25px;

    }}

    .page-subtitle {{

        top: 108px;

        font-size: 11px;

    }}

    .content {{

        top: 150px;

        width: 90vw;

    }}

    .control-row {{

        gap: 12px;

    }}

    .key {{

        width: 80px;

        min-width: 80px;

    }}

}}


</style>

</head>


<body>


<div class="screen">


    <!-- =================================================
         TOP BAR
         ================================================= -->

    <div class="top-bar">

        <div>
            PROJECT : LOGIC
        </div>

        <div class="system-status">
            SYSTEM MANUAL // 01
        </div>

    </div>


    <!-- =================================================
         TITLE
         ================================================= -->

    <div class="page-title">
        HOW TO PLAY
    </div>


    <div class="page-subtitle">
        BASIC OPERATING INSTRUCTIONS
    </div>


    <!-- =================================================
         CONTENT
         ================================================= -->

    <div class="content">


        <!-- MOVEMENT -->

        <div class="section">

            <div class="section-title">
                [ 01 ] MOVEMENT
            </div>

            <div class="section-body">

                <div class="control-row">

                    <div class="key">
                        W A S D
                    </div>

                    <div class="description">
                        Move the player.
                    </div>

                </div>

            </div>

        </div>


        <!-- INTERACTION -->

        <div class="section">

            <div class="section-title">
                [ 02 ] INTERACTION
            </div>

            <div class="section-body">

                <div class="control-row">

                    <div class="key">
                        E
                    </div>

                    <div class="description">
                        Inspect objects, interact with devices, and collect items.
                    </div>

                </div>

            </div>

        </div>


        <!-- INVENTORY -->

        <div class="section">

            <div class="section-title">
                [ 03 ] INVENTORY
            </div>

            <div class="section-body">

                <div class="control-row">

                    <div class="key">
                        I
                    </div>

                    <div class="description">
                        Open or close the inventory.
                    </div>

                </div>


                <div class="control-row">

                    <div class="key">
                        ESC
                    </div>

                    <div class="description">
                        Close the inventory or current menu.
                    </div>

                </div>

            </div>

        </div>


        <!-- SYSTEM MESSAGE -->

        <div class="section">

            <div class="section-title">
                [ 04 ] SYSTEM MESSAGE
            </div>

            <div class="section-body">

                <div class="control-row">

                    <div class="key">
                        SPACE
                    </div>

                    <div class="description">
                        Advance system messages and dialogue.
                    </div>

                </div>

            </div>

        </div>


        <!-- IMPORTANT -->

        <div class="section">

            <div class="section-title">
                [ 05 ] IMPORTANT
            </div>

            <div class="section-body">

                <div class="warning">
                    Examine your surroundings carefully.
                    Not every piece of information provided by the system
                    should be trusted.
                </div>

                <br>

                <div class="warning">
                    Some clues may contradict one another.
                    Compare records, inspect objects, and determine
                    what information is actually reliable.
                </div>

            </div>

        </div>


        <div class="footer">
            ECHO SYSTEM // INFORMATION IS NOT ALWAYS TRUE
        </div>


    </div>


    <!-- =================================================
         BACK
         ================================================= -->

    <button
        id="back"
        class="back-button"
    >
        BACK TO TITLE
    </button>


</div>


<script>


document
    .getElementById("back")
    .addEventListener("click", function() {{

        window.parent.location.href = "?action=title";

    }});


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
    scrolling=True,
)
st.markdown(
    """
    <style>

    div[data-testid="stButton"] {
        position: fixed !important;

        bottom: 30px !important;
        left: 50% !important;

        transform: translateX(-50%) !important;

        width: 210px !important;
        height: 48px !important;

        z-index: 9999 !important;
    }

    div[data-testid="stButton"] > button {
        width: 210px !important;
        height: 48px !important;

        background: #000000 !important;

        border: 1px solid #ffffff !important;
        border-radius: 0 !important;

        color: #ffffff !important;

        font-family: "NeoDungGeunMo", monospace !important;

        font-size: 15px !important;
    }

    div[data-testid="stButton"] > button:hover {
        background: #ffffff !important;
        color: #000000 !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


if st.button("BACK TO TITLE", key="back_to_title"):
    st.switch_page("main.py")
