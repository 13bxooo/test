import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PROJECT : LOGIC // HOW TO PLAY",
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
# HOW TO PLAY SCREEN
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

    overflow-y: auto;
}}


/* =====================================================
   HEADER
   ===================================================== */

.header {{
    position: absolute;

    top: 32px;
    left: 50px;
    right: 50px;

    display: flex;

    justify-content: space-between;
    align-items: center;

    font-size: 15px;

    letter-spacing: 1px;

    color: #ffffff;
}}


.header-right {{
    color: #666666;
}}


/* =====================================================
   TITLE
   ===================================================== */

.title-area {{
    position: absolute;

    top: 100px;

    left: 50px;
}}


.main-title {{
    font-size: clamp(32px, 4vw, 48px);

    letter-spacing: 2px;

    margin-bottom: 14px;
}}


.subtitle {{
    color: #777777;

    font-size: 15px;

    letter-spacing: 1px;
}}


/* =====================================================
   CONTENT
   ===================================================== */

.content {{
    position: absolute;

    top: 230px;

    left: 50%;

    transform: translateX(-50%);

    width: calc(100% - 100px);

    max-width: 1000px;

    display: grid;

    grid-template-columns: repeat(2, minmax(280px, 1fr));

    gap: 18px;

    padding-bottom: 120px;
}}


/* =====================================================
   INSTRUCTION CARD
   ===================================================== */

.card {{
    min-height: 125px;

    border: 1px solid #333333;

    background: #050505;

    padding: 20px;

    transition:
        border-color 0.15s ease,
        background 0.15s ease;
}}


.card:hover {{
    border-color: #ffffff;

    background: #0b0b0b;
}}


.card-header {{
    display: flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 15px;
}}


.number {{
    color: #666666;

    font-size: 13px;
}}


.card-title {{
    color: #ffffff;

    font-size: 19px;

    letter-spacing: 1px;
}}


/* =====================================================
   KEY
   ===================================================== */

.key {{
    display: inline-flex;

    align-items: center;
    justify-content: center;

    min-width: 58px;
    height: 32px;

    padding: 0 10px;

    border: 1px solid #777777;

    background: #111111;

    color: #ffffff;

    font-size: 14px;

    margin-right: 8px;

    vertical-align: middle;
}}


/* =====================================================
   DESCRIPTION
   ===================================================== */

.description {{
    color: #999999;

    font-size: 14px;

    line-height: 1.8;
}}


/* =====================================================
   IMPORTANT
   ===================================================== */

.important {{
    grid-column: 1 / -1;

    border: 1px solid #555555;

    padding: 20px;

    margin-top: 4px;

    background: #030303;
}}


.important-title {{
    color: #ffffff;

    font-size: 16px;

    margin-bottom: 12px;

    letter-spacing: 1px;
}}


.important-text {{
    color: #888888;

    font-size: 14px;

    line-height: 1.9;
}}


.warning {{
    color: #ffffff;
}}


/* =====================================================
   BACK BUTTON
   ===================================================== */

.back {{
    position: fixed;

    bottom: 35px;

    left: 50%;

    transform: translateX(-50%);

    width: 190px;
    height: 48px;

    display: flex;

    align-items: center;
    justify-content: center;

    border: 1px solid #555555;

    background: #050505;

    color: #ffffff;

    font-family: "NeoDungGeunMo", monospace;

    font-size: 16px;

    cursor: pointer;

    text-decoration: none;

    z-index: 100;
}}


.back:hover {{
    background: #ffffff;

    color: #000000;

    border-color: #ffffff;
}}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {{
    position: fixed;

    bottom: 18px;

    left: 50px;

    color: #444444;

    font-size: 11px;

    letter-spacing: 1px;
}}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {{

    .header {{
        left: 25px;
        right: 25px;

        font-size: 12px;
    }}

    .title-area {{
        left: 25px;

        top: 90px;
    }}

    .content {{
        top: 210px;

        width: calc(100% - 50px);

        grid-template-columns: 1fr;

        padding-bottom: 120px;
    }}

    .important {{
        grid-column: auto;
    }}

    .footer {{
        left: 25px;
    }}

    .back {{
        bottom: 25px;
    }}

}}

</style>

</head>


<body>

<div class="screen">


    <!-- =================================================
         HEADER
         ================================================= -->

    <div class="header">

        <div>
            PROJECT : LOGIC
        </div>

        <div class="header-right">
            SYSTEM MANUAL // 01
        </div>

    </div>


    <!-- =================================================
         TITLE
         ================================================= -->

    <div class="title-area">

        <div class="main-title">
            HOW TO PLAY
        </div>

        <div class="subtitle">
            BASIC OPERATING INSTRUCTIONS
        </div>

    </div>


    <!-- =================================================
         INSTRUCTIONS
         ================================================= -->

    <div class="content">


        <!-- MOVEMENT -->

        <div class="card">

            <div class="card-header">

                <span class="number">
                    01
                </span>

                <span class="card-title">
                    MOVEMENT
                </span>

            </div>

            <div class="description">

                <span class="key">W</span>
                <span class="key">A</span>
                <span class="key">S</span>
                <span class="key">D</span>

                <br>

                연구시설 내부를 이동합니다.

            </div>

        </div>


        <!-- INTERACTION -->

        <div class="card">

            <div class="card-header">

                <span class="number">
                    02
                </span>

                <span class="card-title">
                    INTERACTION
                </span>

            </div>

            <div class="description">

                <span class="key">E</span>

                주변의 물체를 조사하거나

                <br>

                아이템을 획득합니다.

            </div>

        </div>


        <!-- INVENTORY -->

        <div class="card">

            <div class="card-header">

                <span class="number">
                    03
                </span>

                <span class="card-title">
                    INVENTORY
                </span>

            </div>

            <div class="description">

                <span class="key">I</span>

                보유한 아이템과 단서를 확인합니다.

                <br>

                <span class="key">ESC</span>

                인벤토리 또는 메뉴를 닫습니다.

            </div>

        </div>


        <!-- SYSTEM MESSAGE -->

        <div class="card">

            <div class="card-header">

                <span class="number">
                    04
                </span>

                <span class="card-title">
                    SYSTEM MESSAGE
                </span>

            </div>

            <div class="description">

                <span class="key">SPACE</span>

                대화와 시스템 메시지를 진행합니다.

                <br>

                중요한 정보가 표시될 수 있습니다.

            </div>

        </div>


        <!-- IMPORTANT -->

        <div class="important">

            <div class="important-title">
                IMPORTANT
            </div>

            <div class="important-text">

                주변의 물체와 기록을 자세히 조사하십시오.

                <br>

                <span class="warning">
                    ECHO가 제공하는 모든 정보가 사실이라고 가정하지 마십시오.
                </span>

                <br>

                서로 모순되는 단서가 발견될 수 있습니다.

                무엇을 믿을 것인지는 당신의 판단에 달려 있습니다.

            </div>

        </div>


    </div>


    <!-- =================================================
         BACK TO TITLE
         ================================================= -->

    <a
        class="back"
        href="/"
        target="_top"
    >
        BACK TO TITLE
    </a>


    <!-- =================================================
         FOOTER
         ================================================= -->

    <div class="footer">
        ECHO SYSTEM // INFORMATION IS NOT ALWAYS TRUE
    </div>


</div>

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
