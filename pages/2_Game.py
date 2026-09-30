import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PROJECT : LOGIC",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# SESSION STATE
# =========================================================

if "game_paused" not in st.session_state:
    st.session_state.game_paused = False


# =========================================================
# PAGE ACTION
# =========================================================

action = st.query_params.get("action")


if action == "restart":

    st.session_state.game_paused = False
    st.query_params.clear()
    st.rerun()


elif action == "title":

    # TITLE로 돌아갔다는 사실을 main.py에 전달
    st.session_state.show_continue_warning = True

    st.query_params.clear()

    st.switch_page("main.py")


# =========================================================
# FONT
# =========================================================

font_path = None

for name in ["neodgm.ttf", "neodgm(2).ttf"]:

    candidate = Path(name)

    if candidate.exists():
        font_path = candidate
        break


if font_path:

    font_base64 = base64.b64encode(
        font_path.read_bytes()
    ).decode("utf-8")

else:

    font_base64 = ""


# =========================================================
# STREAMLIT CSS
# =========================================================

st.markdown(
    f"""
    <style>

    @font-face {{
        font-family: 'NeoDungGeunMo';
        src: url(data:font/ttf;base64,{font_base64})
             format('truetype');
    }}

    html,
    body,
    [class*="css"] {{
        font-family:
            'NeoDungGeunMo',
            monospace !important;
    }}

    #MainMenu,
    header,
    footer {{
        visibility: hidden;
    }}

    .stApp {{
        background: #000000 !important;
    }}

    .block-container {{
        padding: 0 !important;
        max-width: 100vw !important;
    }}


    /* =====================================================
       PAUSE BUTTON
       ===================================================== */

    .st-key-pause_game_button {{
        position: fixed !important;

        top: 24px !important;
        right: 28px !important;

        width: 45px !important;
        height: 45px !important;

        z-index: 999999 !important;

        padding: 0 !important;
        margin: 0 !important;
    }}

    .st-key-pause_game_button button {{
        width: 45px !important;
        height: 45px !important;

        padding: 0 !important;
        margin: 0 !important;

        border: none !important;
        outline: none !important;
        box-shadow: none !important;

        border-radius: 0 !important;

        background: #000000 !important;
        color: #ffffff !important;

        font-family:
            'NeoDungGeunMo',
            monospace !important;

        font-size: 24px !important;

        cursor: pointer !important;
    }}

    .st-key-pause_game_button button:hover {{
        background: #ffffff !important;
        color: #000000 !important;
    }}


    @media (max-width: 700px) {{

        .st-key-pause_game_button {{
            top: 14px !important;
            right: 14px !important;

            width: 42px !important;
            height: 42px !important;
        }}

        .st-key-pause_game_button button {{
            width: 42px !important;
            height: 42px !important;

            font-size: 20px !important;
        }}

    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# PAUSE BUTTON
# =========================================================

pause_clicked = st.button(
    "▶"
    if st.session_state.game_paused
    else "||",
    key="pause_game_button",
)


if pause_clicked:

    st.session_state.game_paused = (
        not st.session_state.game_paused
    )

    st.rerun()


paused = st.session_state.game_paused


# =========================================================
# GAME HTML
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
    font-family: 'NeoDungGeunMo';

    src:
        url(data:font/ttf;base64,{font_base64})
        format('truetype');
}}


/* =====================================================
   GLOBAL
   ===================================================== */

* {{
    box-sizing: border-box;

    user-select: none;
    -webkit-user-select: none;

    -webkit-touch-callout: none;
}}

html,
body {{
    width: 100%;
    height: 100%;

    margin: 0;
    padding: 0;

    overflow: hidden;

    background: #000000;

    font-family:
        'NeoDungGeunMo',
        monospace;
}}

body {{
    color: #ffffff;
}}


/* =====================================================
   GAME ROOT
   ===================================================== */

.game {{
    position: relative;

    width: 100vw;
    height: 100vh;

    overflow: hidden;

    background: #000000;

    outline: none;
}}


/* =====================================================
   HEADER
   ===================================================== */

.project-title {{
    position: absolute;

    top: 24px;
    left: 28px;

    font-size: 18px;

    letter-spacing: 1px;

    z-index: 50;
}}

.stage-title {{
    position: absolute;

    top: 52px;
    left: 28px;

    font-size: 13px;

    color: #777777;

    letter-spacing: 1px;

    z-index: 50;
}}


/* =====================================================
   GAME AREA
   ===================================================== */

.game-area {{
    position: absolute;

    top: 90px;
    left: 28px;
    right: 28px;
    bottom: 70px;

    overflow: hidden;

    background-color: #080808;

    background-image:
        linear-gradient(
            rgba(255,255,255,0.045) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(255,255,255,0.045) 1px,
            transparent 1px
        );

    background-size: 40px 40px;
}}


/* =====================================================
   ROOM
   ===================================================== */

.room {{
    position: absolute;

    left: 7%;
    top: 8%;

    width: 86%;
    height: 82%;

    border: 1px solid
        rgba(255,255,255,0.15);

    overflow: hidden;
}}


/* =====================================================
   FLOOR GRID
   ===================================================== */

.room-line-horizontal {{
    position: absolute;

    left: 0;
    right: 0;

    top: 50%;

    height: 1px;

    background:
        rgba(255,255,255,0.045);
}}

.room-line-vertical {{
    position: absolute;

    top: 0;
    bottom: 0;

    left: 50%;

    width: 1px;

    background:
        rgba(255,255,255,0.045);
}}


/* =====================================================
   OBJECTS
   ===================================================== */

.object {{
    position: absolute;

    display: flex;

    align-items: center;
    justify-content: center;

    background: #0b0b0b;

    border:
        1px solid
        rgba(255,255,255,0.28);

    color: #777777;

    font-size: 12px;

    text-align: center;

    z-index: 8;
}}


/* =====================================================
   COMPUTER
   ===================================================== */

.computer {{
    left: 42%;
    top: 13%;

    width: 16%;
    height: 14%;
}}


/* =====================================================
   COMPUTER SCREEN
   ===================================================== */

.computer::before {{
    content: "";

    position: absolute;

    left: 14%;
    right: 14%;

    top: 16%;
    bottom: 25%;

    border:
        1px solid
        rgba(255,255,255,0.30);

    background: #000000;
}}


/* =====================================================
   DESK
   ===================================================== */

.desk {{
    left: 35%;
    top: 62%;

    width: 30%;
    height: 12%;
}}


/* =====================================================
   DESK TOP LINE
   ===================================================== */

.desk::before {{
    content: "";

    position: absolute;

    left: 0;
    right: 0;

    top: 0;

    height: 3px;

    background: #222222;
}}


/* =====================================================
   OBJECT LABEL
   ===================================================== */

.object-label {{
    position: absolute;

    bottom: -22px;

    left: 50%;

    transform:
        translateX(-50%);

    white-space: nowrap;

    font-size: 10px;

    color: #555555;
}}


/* =====================================================
   ACCESS KEY
   ===================================================== */

.access-key {{
    position: absolute;

    width: 30px;
    height: 11px;

    left: 50%;
    top: 42%;

    transform:
        translate(-50%, -50%);

    background: #ffffff;

    display: none;

    z-index: 20;

    box-shadow:
        0 0 8px
        rgba(255,255,255,0.35);
}}

.access-key::after {{
    content: "";

    position: absolute;

    right: -9px;
    top: 3px;

    width: 9px;
    height: 5px;

    background: #ffffff;
}}

.access-key::before {{
    content: "";

    position: absolute;

    left: 4px;
    top: 3px;

    width: 5px;
    height: 5px;

    border:
        1px solid #000000;

    border-radius: 50%;
}}

.access-key.visible {{
    display: block;

    animation:
        keyAppear
        0.45s ease-out;
}}

@keyframes keyAppear {{
    0% {{
        opacity: 0;
        transform:
            translate(-50%, -50%)
            scale(0.5);
    }}

    100% {{
        opacity: 1;
        transform:
            translate(-50%, -50%)
            scale(1);
    }}
}}


/* =====================================================
   EXIT WALL
   ===================================================== */

.exit-wall {{
    position: absolute;

    right: 0;
    top: 29%;

    width: 11%;
    height: 42%;

    background:
        repeating-linear-gradient(
            0deg,
            #0b0b0b,
            #0b0b0b 8px,
            #101010 9px,
            #101010 10px
        );

    border-left:
        2px solid #252525;

    border-top:
        1px solid #222222;

    border-bottom:
        1px solid #222222;

    z-index: 7;

    display: flex;

    align-items: center;
    justify-content: center;
}}

.exit-wall::before {{
    content: "";

    position: absolute;

    left: 8px;
    right: 8px;
    top: 8px;
    bottom: 8px;

    border:
        1px solid
        rgba(255,255,255,0.08);
}}

.exit-label {{
    position: absolute;

    left: -125px;

    top: 50%;

    transform:
        translateY(-50%);

    white-space: nowrap;

    color: #555555;

    font-size: 11px;
}}

.exit-label span {{
    color: #ffffff;
}}


/* =====================================================
   EXIT ARROW
   ===================================================== */

.exit-arrow {{
    position: absolute;

    left: -68px;

    top: 38%;

    font-size: 24px;

    color: #ffffff;

    opacity: 0;

    transform: translateY(0);

    transition:
        opacity 0.4s ease;
}}

.exit-arrow.active {{
    opacity: 1;

    animation:
        exitArrowMove
        1.1s
        ease-in-out
        infinite;
}}

@keyframes exitArrowMove {{
    0% {{
        transform:
            translateY(-5px);
    }}

    50% {{
        transform:
            translateY(7px);
    }}

    100% {{
        transform:
            translateY(-5px);
    }}
}}


/* =====================================================
   PLAYER
   ===================================================== */

.player {{
    position: absolute;

    width: 24px;
    height: 24px;

    transform:
        translate(-50%, -50%);

    background: #ffffff;

    z-index: 30;

    box-shadow:
        0 0 0 1px #000000;
}}

.player::after {{
    content: "";

    position: absolute;

    left: 4px;
    right: 4px;

    bottom: -5px;

    height: 4px;

    background:
        rgba(255,255,255,0.15);
}}


/* =====================================================
   INTERACTION MESSAGE
   ===================================================== */

.interaction-message {{
    position: absolute;

    left: 50%;

    bottom: 20%;

    transform:
        translateX(-50%);

    padding: 9px 16px;

    background: #000000;

    border:
        1px solid #333333;

    font-size: 12px;

    color: #ffffff;

    opacity: 0;

    pointer-events: none;

    transition:
        opacity 0.1s linear;

    z-index: 45;

    white-space: nowrap;
}}

.interaction-message.visible {{
    opacity: 1;
}}


/* =====================================================
   ECHO CHAT
   ===================================================== */

.echo-bar {{
    position: absolute;

    left: 50%;

    bottom: 3%;

    transform:
        translateX(-50%);

    width:
        min(760px, 82%);

    min-height: 82px;

    padding: 13px 18px;

    background: #050505;

    border:
        1px solid #3a3a3a;

    z-index: 40;
}}

.echo-name {{
    font-size: 11px;

    color: #ffffff;

    letter-spacing: 1px;

    margin-bottom: 8px;
}}

.echo-message {{
    min-height: 34px;

    font-size: 12px;

    color: #999999;

    line-height: 1.7;

    padding-right: 20px;
}}

.echo-next {{
    position: absolute;

    right: 12px;
    bottom: 8px;

    font-size: 9px;

    color: #555555;

    opacity: 0;
}}

.echo-next.visible {{
    opacity: 1;
    color: #888888;
}}


/* =====================================================
   STATUS
   ===================================================== */

.status {{
    position: absolute;

    bottom: 24px;
    left: 28px;

    font-size: 14px;

    color: #777777;

    z-index: 50;
}}


/* =====================================================
   COMMON OVERLAY
   ===================================================== */

.overlay {{
    position: absolute;

    inset: 0;

    z-index: 100;

    display: flex;

    align-items: center;
    justify-content: center;

    background:
        rgba(0,0,0,0.92);
}}


/* =====================================================
   COMPUTER OVERLAY
   ===================================================== */

.computer-overlay {{
    position: absolute;

    inset: 0;

    z-index: 120;

    display: none;

    align-items: center;
    justify-content: center;

    background:
        rgba(0,0,0,0.95);
}}

.computer-panel {{
    width:
        min(520px, 86vw);

    background: #050505;

    border:
        1px solid #333333;

    padding: 28px;
}}

.computer-title {{
    font-size: 20px;

    margin-bottom: 8px;
}}

.computer-sub {{
    color: #666666;

    font-size: 11px;

    line-height: 1.7;

    margin-bottom: 20px;
}}

.code-display {{
    padding: 16px;

    margin-bottom: 18px;

    border:
        1px solid #292929;

    background: #000000;

    text-align: center;
}}

.code-display-label {{
    color: #555555;

    font-size: 9px;

    margin-bottom: 8px;
}}

.code-display-number {{
    font-size: 28px;

    letter-spacing: 8px;

    color: #ffffff;
}}

.code-input {{
    width: 100%;

    height: 48px;

    border:
        1px solid #444444;

    background: #000000;

    color: #ffffff;

    font-family:
        'NeoDungGeunMo',
        monospace;

    font-size: 22px;

    text-align: center;

    letter-spacing: 6px;

    outline: none;
}}

.code-input:focus {{
    border-color: #ffffff;
}}

.code-button {{
    width: 100%;

    height: 44px;

    margin-top: 10px;

    border: none;

    background: #ffffff;

    color: #000000;

    font-family:
        'NeoDungGeunMo',
        monospace;

    cursor: pointer;
}}

.code-button:hover {{
    background: #bbbbbb;
}}

.code-error {{
    min-height: 20px;

    margin-top: 12px;

    color: #777777;

    font-size: 11px;

    text-align: center;
}}


/* =====================================================
   CARD SWIPE
   ===================================================== */

.card-overlay {{
    position: absolute;

    inset: 0;

    z-index: 180;

    display: none;

    align-items: center;
    justify-content: center;

    background:
        rgba(0,0,0,0.94);
}}

.card-panel {{
    width:
        min(600px, 88vw);

    padding: 30px;

    background: #050505;

    border:
        1px solid #333333;

    text-align: center;
}}

.card-title {{
    font-size: 20px;

    margin-bottom: 8px;
}}

.card-sub {{
    font-size: 10px;

    color: #666666;

    margin-bottom: 30px;
}}

.card-reader {{
    position: relative;

    width: min(460px, 80vw);

    height: 150px;

    margin: 0 auto;

    border:
        1px solid #222222;

    background: #000000;

    overflow: hidden;
}}

.card-reader-line {{
    position: absolute;

    top: 50%;

    left: 30px;
    right: 30px;

    height: 2px;

    background: #222222;
}}

.card-reader-slot {{
    position: absolute;

    top: calc(50% - 12px);

    right: 28px;

    width: 70px;
    height: 24px;

    border:
        1px solid #555555;

    background: #0a0a0a;
}}

.access-card {{
    position: absolute;

    left: 20px;

    top: calc(50% - 25px);

    width: 95px;
    height: 50px;

    background: #ffffff;

    color: #000000;

    cursor: grab;

    touch-action: none;

    z-index: 5;

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 10px;

    letter-spacing: 1px;

    box-shadow:
        0 0 12px
        rgba(255,255,255,0.15);
}}

.access-card:active {{
    cursor: grabbing;
}}

.card-reader.success .access-card {{
    animation:
        cardSuccess
        0.6s
        ease-out
        forwards;
}}

@keyframes cardSuccess {{
    to {{
        left: calc(100% - 123px);
    }}
}}

.card-instruction {{
    margin-top: 18px;

    font-size: 10px;

    color: #666666;
}}

.card-close {{
    margin-top: 18px;
}}


/* =====================================================
   PAUSE
   ===================================================== */

.pause-overlay {{
    position: absolute;

    inset: 0;

    z-index: 160;

    display: none;

    align-items: center;
    justify-content: center;

    background:
        rgba(0,0,0,0.94);
}}

.pause-title {{
    font-size: 28px;

    text-align: center;

    margin-bottom: 10px;
}}

.pause-sub {{
    color: #777777;

    font-size: 12px;

    text-align: center;
}}


/* =====================================================
   INVENTORY
   ===================================================== */

.inventory-panel {{
    width:
        min(820px, 88vw);

    background: #050505;

    padding: 34px 38px;
}}

.inventory-header {{
    display: flex;

    justify-content: space-between;
    align-items: center;

    padding-bottom: 18px;

    margin-bottom: 22px;

    border-bottom:
        1px solid #333333;
}}

.inventory-title {{
    font-size: 24px;
}}

.inventory-close {{
    font-size: 12px;

    color: #666666;
}}

.inventory-grid {{
    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 10px;
}}

.inventory-slot {{
    position: relative;

    aspect-ratio: 1 / 1;

    background: #090909;

    border:
        1px solid #292929;

    display: flex;

    align-items: center;
    justify-content: center;

    cursor: pointer;
}}

.inventory-slot:hover,
.inventory-slot.selected {{
    background: #ffffff;

    color: #000000;
}}

.slot-number {{
    position: absolute;

    top: 7px;
    left: 9px;

    font-size: 10px;

    color: #555555;
}}

.item-name {{
    font-size: 13px;

    text-align: center;
}}

.empty-text {{
    color: #444444;

    font-size: 11px;
}}

.item-description {{
    min-height: 70px;

    margin-top: 20px;

    padding: 15px;

    background: #090909;

    border-top:
        1px solid #292929;

    font-size: 12px;

    line-height: 1.8;

    color: #888888;
}}


/* =====================================================
   HELP
   ===================================================== */

.help-panel {{
    width:
        min(760px, 86vw);

    max-height: 82vh;

    overflow-y: auto;

    background: #050505;

    padding: 36px 40px;
}}

.help-header {{
    display: flex;

    justify-content: space-between;

    padding-bottom: 18px;

    margin-bottom: 20px;

    border-bottom:
        1px solid #333333;
}}

.help-title {{
    font-size: 24px;
}}

.help-close {{
    font-size: 12px;

    color: #666666;
}}

.help-row {{
    display: flex;

    gap: 20px;

    padding: 14px 0;

    border-bottom:
        1px solid #1f1f1f;
}}

.help-number {{
    width: 30px;

    color: #555555;
}}

.help-key {{
    width: 145px;

    font-size: 14px;
}}

.help-description {{
    color: #888888;

    font-size: 12px;

    line-height: 1.7;
}}


/* =====================================================
   MOBILE CONTROLS
   ===================================================== */

.mobile-controls {{
    display: none;

    position: absolute;

    right: 16px;
    bottom: 18px;

    width: 150px;
    height: 150px;

    z-index: 300;

    pointer-events: none;
}}

.control-button {{
    position: absolute;

    width: 46px;
    height: 46px;

    padding: 0;

    border:
        1px solid #555555;

    background:
        rgba(0,0,0,0.92);

    color: #ffffff;

    font-family:
        'NeoDungGeunMo',
        monospace;

    font-size: 20px;

    display: flex;

    align-items: center;
    justify-content: center;

    touch-action: none;

    pointer-events: auto;

    -webkit-tap-highlight-color: transparent;
}}

.control-button:active {{
    background: #ffffff;

    color: #000000;
}}

.control-up {{
    top: 0;
    left: 52px;
}}

.control-left {{
    top: 52px;
    left: 0;
}}

.control-right {{
    top: 52px;
    right: 0;
}}

.control-down {{
    bottom: 0;
    left: 52px;
}}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {{

    .project-title {{
        top: 16px;
        left: 16px;

        font-size: 14px;
    }}

    .stage-title {{
        top: 38px;
        left: 16px;

        font-size: 10px;
    }}

    .game-area {{
        top: 64px;

        left: 12px;
        right: 12px;

        bottom: 54px;

        background-size: 28px 28px;
    }}

    .status {{
        left: 12px;
        bottom: 14px;

        font-size: 10px;
    }}

    .echo-bar {{
        width: 88%;

        min-height: 90px;

        bottom: 2%;

        padding: 11px 13px;
    }}

    .echo-message {{
        font-size: 10px;
    }}

    .interaction-message {{
        bottom: 25%;
    }}

    .mobile-controls {{
        display: block;
    }}

    .inventory-panel,
    .help-panel {{
        width: 92vw;

        padding: 24px 20px;
    }}

    .inventory-grid {{
        gap: 6px;
    }}

    .item-name {{
        font-size: 10px;
    }}

    .help-row {{
        gap: 10px;
    }}

    .help-key {{
        width: 90px;

        font-size: 11px;
    }}

    .help-description {{
        font-size: 10px;
    }}

    .exit-label {{
        left: -92px;

        font-size: 8px;
    }}

    .exit-arrow {{
        left: -50px;

        font-size: 18px;
    }}

}}

</style>

</head>


<body>


<div
    class="game"
    id="gameRoot"
    tabindex="0"
>


    <!-- =================================================
         HEADER
         ================================================= -->

    <div class="project-title">
        PROJECT : LOGIC
    </div>

    <div class="stage-title">
        STAGE 01 // CONTROL ROOM
    </div>


    <!-- =================================================
         GAME AREA
         ================================================= -->

    <div class="game-area">


        <div class="room">


            <div class="room-line-horizontal"></div>

            <div class="room-line-vertical"></div>


            <!-- =================================================
                 COMPUTER
                 ================================================= -->

            <div
                class="object computer"
                id="computer"
            >

                COMPUTER

                <div class="object-label">
                    ECHO TERMINAL
                </div>

            </div>


            <!-- =================================================
                 DESK
                 ================================================= -->

            <div
                class="object desk"
                id="desk"
            >

                DESK

                <div class="object-label">
                    RESEARCH DESK
                </div>

                <div
                    class="access-key"
                    id="accessKey"
                ></div>

            </div>


            <!-- =================================================
                 EXIT WALL
                 ================================================= -->

            <div
                class="exit-wall"
                id="exitWall"
            >

                <div class="exit-label">
                    [<span>EXIT</span>] SECURITY ROOM
                </div>

                <div
                    class="exit-arrow"
                    id="exitArrow"
                >
                    ↓
                </div>

            </div>


            <!-- =================================================
                 PLAYER
                 ================================================= -->

            <div
                class="player"
                id="player"
            ></div>


            <!-- =================================================
                 INTERACTION
                 ================================================= -->

            <div
                class="interaction-message"
                id="interactionMessage"
            >
                PRESS E
            </div>


            <!-- =================================================
                 ECHO
                 ================================================= -->

            <div
                class="echo-bar"
                id="echoBar"
            >

                <div class="echo-name">
                    ECHO // AI SYSTEM
                </div>

                <div
                    class="echo-message"
                    id="echoMessage"
                ></div>

                <div
                    class="echo-next"
                    id="echoNext"
                >
                    SPACE // NEXT
                </div>

            </div>


            <!-- =================================================
                 MOBILE CONTROLS
                 ================================================= -->

            <div
                class="mobile-controls"
                id="mobileControls"
            >

                <button
                    class="control-button control-up"
                    data-direction="w"
                    type="button"
                >
                    ▲
                </button>

                <button
                    class="control-button control-left"
                    data-direction="a"
                    type="button"
                >
                    ◀
                </button>

                <button
                    class="control-button control-right"
                    data-direction="d"
                    type="button"
                >
                    ▶
                </button>

                <button
                    class="control-button control-down"
                    data-direction="s"
                    type="button"
                >
                    ▼
                </button>

            </div>


            <!-- =================================================
                 INVENTORY
                 ================================================= -->

            <div
                class="overlay"
                id="inventoryOverlay"
                style="display:none;"
            >

                <div class="inventory-panel">

                    <div class="inventory-header">

                        <div class="inventory-title">
                            INVENTORY
                        </div>

                        <div class="inventory-close">
                            I / ESC TO CLOSE
                        </div>

                    </div>

                    <div class="inventory-grid">

                        <div
                            class="inventory-slot"
                            data-slot="0"
                        ></div>

                        <div
                            class="inventory-slot"
                            data-slot="1"
                        ></div>

                        <div
                            class="inventory-slot"
                            data-slot="2"
                        ></div>

                        <div
                            class="inventory-slot"
                            data-slot="3"
                        ></div>

                        <div
                            class="inventory-slot"
                            data-slot="4"
                        ></div>

                        <div
                            class="inventory-slot"
                            data-slot="5"
                        ></div>

                        <div
                            class="inventory-slot"
                            data-slot="6"
                        ></div>

                        <div
                            class="inventory-slot"
                            data-slot="7"
                        ></div>

                    </div>

                    <div
                        class="item-description"
                        id="itemDescription"
                    >
                        ITEM DESCRIPTION

                        <br><br>

                        아이템을 선택하면 설명이 표시됩니다.
                    </div>

                </div>

            </div>


            <!-- =================================================
                 HELP
                 ================================================= -->

            <div
                class="overlay"
                id="helpOverlay"
                style="display:none;"
            >

                <div class="help-panel">

                    <div class="help-header">

                        <div class="help-title">
                            HOW TO PLAY
                        </div>

                        <div class="help-close">
                            H / ESC TO CLOSE
                        </div>

                    </div>


                    <div class="help-row">

                        <div class="help-number">
                            01
                        </div>

                        <div class="help-key">
                            MOVEMENT<br>
                            W A S D
                        </div>

                        <div class="help-description">
                            시설 내부를 이동합니다.
                        </div>

                    </div>


                    <div class="help-row">

                        <div class="help-number">
                            02
                        </div>

                        <div class="help-key">
                            INTERACTION<br>
                            E
                        </div>

                        <div class="help-description">
                            가까운 물체를 조사하거나
                            아이템을 획득합니다.
                        </div>

                    </div>


                    <div class="help-row">

                        <div class="help-number">
                            03
                        </div>

                        <div class="help-key">
                            INVENTORY<br>
                            I
                        </div>

                        <div class="help-description">
                            획득한 아이템을 확인합니다.
                        </div>

                    </div>


                    <div class="help-row">

                        <div class="help-number">
                            04
                        </div>

                        <div class="help-key">
                            ECHO<br>
                            SPACE
                        </div>

                        <div class="help-description">
                            현재 채팅을 즉시 완성하거나
                            다음 채팅으로 넘어갑니다.
                        </div>

                    </div>


                    <div class="help-row">

                        <div class="help-number">
                            05
                        </div>

                        <div class="help-key">
                            CONTROLS<br>
                            H
                        </div>

                        <div class="help-description">
                            조작 방법을 확인합니다.
                        </div>

                    </div>

                </div>

            </div>


            <!-- =================================================
                 COMPUTER
                 ================================================= -->

            <div
                class="computer-overlay"
                id="computerOverlay"
            >

                <div class="computer-panel">

                    <div class="computer-title">
                        ECHO TERMINAL
                    </div>

                    <div class="computer-sub">
                        SYSTEM ACCESS REQUIRED.<br>
                        ECHO HAS GENERATED A TEMPORARY ACCESS SEQUENCE.
                    </div>


                    <div class="code-display">

                        <div class="code-display-label">
                            ACCESS SEQUENCE
                        </div>

                        <div
                            class="code-display-number"
                            id="codeDisplayNumber"
                        >
                            ----
                        </div>

                    </div>


                    <input
                        class="code-input"
                        id="codeInput"
                        type="text"
                        inputmode="numeric"
                        autocomplete="off"
                        maxlength="4"
                        aria-label="Access code"
                    >


                    <button
                        class="code-button"
                        id="codeButton"
                        type="button"
                    >
                        EXECUTE
                    </button>


                    <div
                        class="code-error"
                        id="codeError"
                    ></div>

                </div>

            </div>


            <!-- =================================================
                 CARD SWIPE
                 ================================================= -->

            <div
                class="card-overlay"
                id="cardOverlay"
            >

                <div class="card-panel">

                    <div class="card-title">
                        SECURITY ACCESS
                    </div>

                    <div class="card-sub">
                        MOVE THE ACCESS KEY ACROSS THE READER.
                    </div>


                    <div
                        class="card-reader"
                        id="cardReader"
                    >

                        <div class="card-reader-line"></div>

                        <div class="card-reader-slot"></div>

                        <div
                            class="access-card"
                            id="accessCard"
                        >
                            ACCESS KEY
                        </div>

                    </div>


                    <div class="card-instruction">
                        CLICK / TOUCH AND DRAG
                    </div>


                    <button
                        class="code-button card-close"
                        id="cardClose"
                        type="button"
                        style="width:170px;"
                    >
                        CANCEL
                    </button>

                </div>

            </div>


            <!-- =================================================
                 PAUSE
                 ================================================= -->

            <div
                class="pause-overlay"
                id="pauseOverlay"
            >

                <div>

                    <div class="pause-title">
                        GAME PAUSED
                    </div>

                    <div class="pause-sub">
                        PRESS ▶ TO CONTINUE
                    </div>


                    <div
                        style="
                        margin-top:24px;
                        display:flex;
                        flex-direction:column;
                        gap:8px;
                        align-items:center;
                        "
                    >

                        <button
                            class="code-button"
                            id="restartButton"
                            type="button"
                            style="width:170px;"
                        >
                            RESTART
                        </button>


                        <button
                            class="code-button"
                            id="titleButton"
                            type="button"
                            style="
                            width:170px;
                            background:#000;
                            color:#fff;
                            border:1px solid #333;
                            "
                        >
                            TITLE
                        </button>

                    </div>

                </div>

            </div>


        </div>

    </div>


    <!-- =================================================
         STATUS
         ================================================= -->

    <div
        class="status"
        id="status"
    >
        ECHO SYSTEM // ONLINE
    </div>


</div>


<script>

/* =====================================================
   STATE
   ===================================================== */

let paused = {str(paused).lower()};

let tutorialStep = 0;

let inventoryOpen = false;
let helpOpen = false;
let computerOpen = false;
let cardOpen = false;

let accessKeyCreated = false;
let accessKeyCollected = false;

let chatIndex = 0;
let chatTyping = false;
let chatFinished = false;
let chatTimer = null;


/* =====================================================
   RANDOM ACCESS CODE
   ===================================================== */

const ACCESS_CODE =
    String(
        Math.floor(
            1000 +
            Math.random() * 9000
        )
    );


/* =====================================================
   ELEMENTS
   ===================================================== */

const gameRoot =
    document.getElementById("gameRoot");

const player =
    document.getElementById("player");

const room =
    document.querySelector(".room");

const inventoryOverlay =
    document.getElementById("inventoryOverlay");

const helpOverlay =
    document.getElementById("helpOverlay");

const computerOverlay =
    document.getElementById("computerOverlay");

const cardOverlay =
    document.getElementById("cardOverlay");

const pauseOverlay =
    document.getElementById("pauseOverlay");

const interactionMessage =
    document.getElementById("interactionMessage");

const echoMessage =
    document.getElementById("echoMessage");

const echoNext =
    document.getElementById("echoNext");

const status =
    document.getElementById("status");

const accessKey =
    document.getElementById("accessKey");

const exitArrow =
    document.getElementById("exitArrow");

const codeInput =
    document.getElementById("codeInput");

const codeButton =
    document.getElementById("codeButton");

const codeError =
    document.getElementById("codeError");

const codeDisplayNumber =
    document.getElementById("codeDisplayNumber");

const cardReader =
    document.getElementById("cardReader");

const accessCard =
    document.getElementById("accessCard");

const cardClose =
    document.getElementById("cardClose");

const inventorySlots =
    document.querySelectorAll(".inventory-slot");

const itemDescription =
    document.getElementById("itemDescription");


/* =====================================================
   CHAT DATA
   ===================================================== */

const tutorialMessages = [

    "연결이 확인되었습니다. 저는 ECHO입니다. 이 시설에서의 첫 번째 절차를 안내하겠습니다.",

    "먼저 이동 방법을 익혀야 합니다. W A S D 키를 사용하여 시설 내부를 이동해 보세요. 중앙의 COMPUTER로 이동하십시오.",

    "좋습니다. COMPUTER에 접근했습니다. 가까운 물체에서는 E 키를 사용하여 상호작용할 수 있습니다. COMPUTER를 조사하십시오.",

    "확인되었습니다. 이제 COMPUTER 화면에 표시된 접근 코드를 입력하십시오.",

    "코드가 확인되었습니다. DESK를 확인하십시오. ACCESS KEY가 생성되었습니다.",

    "ACCESS KEY를 획득했습니다. 이제 EXIT로 이동하십시오. SECURITY ROOM으로 연결되는 출구입니다.",

    "출구 보안 시스템이 활성화되었습니다. ACCESS KEY를 리더기에 긁어 다음 구역으로 이동하십시오."

];


/* =====================================================
   CHAT TYPEWRITER
   ===================================================== */

function startChat(index) {{

    if (
        index < 0 ||
        index >= tutorialMessages.length
    ) {{
        return;
    }}

    chatIndex = index;

    chatFinished = false;
    chatTyping = true;

    echoNext.classList.remove("visible");

    echoMessage.textContent = "";

    if (chatTimer) {{
        clearInterval(chatTimer);
    }}

    const message =
        tutorialMessages[index];

    let position = 0;

    chatTimer =
        setInterval(
            function() {{

                if (position >= message.length) {{

                    clearInterval(chatTimer);

                    chatTimer = null;

                    chatTyping = false;

                    chatFinished = true;

                    echoNext.classList.add(
                        "visible"
                    );

                    return;
                }}

                echoMessage.textContent +=
                    message[position];

                position++;

            }},
            28
        );
}}


/* =====================================================
   SPACE CHAT
   ===================================================== */

function handleChatSpace() {{

    /*
     * 첫 번째 SPACE:
     * 현재 문장을 끝까지 출력
     */

    if (chatTyping) {{

        if (chatTimer) {{
            clearInterval(chatTimer);
            chatTimer = null;
        }}

        echoMessage.textContent =
            tutorialMessages[chatIndex];

        chatTyping = false;
        chatFinished = true;

        echoNext.classList.add(
            "visible"
        );

        return;
    }}


    /*
     * 두 번째 SPACE:
     * 다음 채팅
     */

    advanceChat();

}}


/* =====================================================
   CHAT ADVANCE
   ===================================================== */

function advanceChat() {{

    /*
     * 현재 행동이 완료되지 않았다면
     * 채팅만 넘어가지 않도록 한다.
     */

    if (
        chatIndex === 0 &&
        tutorialStep === 0
    ) {{
        status.textContent =
            "ECHO SYSTEM // 먼저 이동을 시작하십시오.";
        return;
    }}


    if (
        chatIndex === 1 &&
        tutorialStep < 2
    ) {{
        status.textContent =
            "ECHO SYSTEM // COMPUTER로 이동하십시오.";
        return;
    }}


    if (
        chatIndex === 2 &&
        tutorialStep < 2
    ) {{
        status.textContent =
            "ECHO SYSTEM // COMPUTER와 먼저 상호작용하십시오.";
        return;
    }}


    if (
        chatIndex === 3 &&
        tutorialStep < 3
    ) {{
        status.textContent =
            "ECHO SYSTEM // COMPUTER에 접근 코드를 입력하십시오.";
        return;
    }}


    if (
        chatIndex === 4 &&
        tutorialStep < 4
    ) {{
        status.textContent =
            "ECHO SYSTEM // DESK에서 ACCESS KEY를 확인하십시오.";
        return;
    }}


    if (
        chatIndex === 5 &&
        tutorialStep < 5
    ) {{
        status.textContent =
            "ECHO SYSTEM // ACCESS KEY를 획득하십시오.";
        return;
    }}


    if (
        chatIndex === 6
    ) {{
        return;
    }}


    startChat(
        chatIndex + 1
    );
}}


/* =====================================================
   INITIAL CHAT
   ===================================================== */

startChat(0);


/* =====================================================
   INVENTORY
   ===================================================== */

const inventory = [
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null
];


function renderInventory() {{

    inventory.forEach(
        function(item, index) {{

            const slot =
                inventorySlots[index];

            if (!item) {{

                slot.innerHTML =
                    `
                    <div class="slot-number">
                        ${{String(index + 1).padStart(2, "0")}}
                    </div>

                    <div class="empty-text">
                        EMPTY
                    </div>
                    `;

            }} else {{

                slot.innerHTML =
                    `
                    <div class="slot-number">
                        ${{String(index + 1).padStart(2, "0")}}
                    </div>

                    <div class="item-name">
                        ${{item.name}}
                    </div>
                    `;

            }}

        }}
    );
}}


renderInventory();


/* =====================================================
   PLAYER
   ===================================================== */

let playerX = 50;
let playerY = 43;

const moveSpeed = 0.62;


/* =====================================================
   MOVEMENT
   ===================================================== */

const keys = {{
    w: false,
    a: false,
    s: false,
    d: false
}};


function clearMovementKeys() {{

    keys.w = false;
    keys.a = false;
    keys.s = false;
    keys.d = false;
}}


/* =====================================================
   COLLISION
   ===================================================== */

function rectanglesOverlap(
    a,
    b
) {{

    return (
        a.left < b.right &&
        a.right > b.left &&
        a.top < b.bottom &&
        a.bottom > b.top
    );
}}


function getPlayerRect(
    x,
    y
) {{

    const roomRect =
        room.getBoundingClientRect();

    const playerWidth = 24;
    const playerHeight = 24;

    const px =
        roomRect.left +
        (x / 100) *
        roomRect.width;

    const py =
        roomRect.top +
        (y / 100) *
        roomRect.height;

    return {{
        left:
            px -
            playerWidth / 2,

        right:
            px +
            playerWidth / 2,

        top:
            py -
            playerHeight / 2,

        bottom:
            py +
            playerHeight / 2
    }};
}}


function getObstacleRects() {{

    return [
        document.getElementById("computer"),
        document.getElementById("desk"),
        document.getElementById("exitWall")
    ].map(
        function(element) {{
            return element.getBoundingClientRect();
        }}
    );
}}


function canMoveTo(
    nextX,
    nextY
) {{

    const nextRect =
        getPlayerRect(
            nextX,
            nextY
        );

    const obstacles =
        getObstacleRects();

    for (
        const obstacle
        of obstacles
    ) {{

        if (
            rectanglesOverlap(
                nextRect,
                obstacle
            )
        ) {{
            return false;
        }}
    }}

    return true;
}}


/* =====================================================
   OBJECTS
   ===================================================== */

const objects = [

    {{
        id: "computer",
        name: "ECHO TERMINAL"
    }},

    {{
        id: "desk",
        name: "RESEARCH DESK"
    }},

    {{
        id: "exitWall",
        name: "SECURITY EXIT"
    }}

];


let nearbyObject = null;


/* =====================================================
   OBJECT DISTANCE
   ===================================================== */

function distanceToObject(
    object
) {{

    const element =
        document.getElementById(
            object.id
        );

    if (!element) {{
        return Infinity;
    }}

    const roomRect =
        room.getBoundingClientRect();

    const rect =
        element.getBoundingClientRect();

    const centerX =
        (
            rect.left +
            rect.right
        ) / 2;

    const centerY =
        (
            rect.top +
            rect.bottom
        ) / 2;

    const playerRect =
        getPlayerRect(
            playerX,
            playerY
        );

    const playerCenterX =
        (
            playerRect.left +
            playerRect.right
        ) / 2;

    const playerCenterY =
        (
            playerRect.top +
            playerRect.bottom
        ) / 2;

    const dx =
        playerCenterX -
        centerX;

    const dy =
        playerCenterY -
        centerY;

    return Math.sqrt(
        dx * dx +
        dy * dy
    );
}}


/* =====================================================
   INTERACTION
   ===================================================== */

function checkInteraction() {{

    nearbyObject = null;

    let closest =
        Infinity;

    objects.forEach(
        function(object) {{

            const distance =
                distanceToObject(
                    object
                );

            if (
                distance < 90 &&
                distance < closest
            ) {{

                nearbyObject =
                    object;

                closest =
                    distance;
            }}
        }}
    );


    if (
        nearbyObject &&
        !computerOpen &&
        !inventoryOpen &&
        !helpOpen &&
        !cardOpen
    ) {{

        interactionMessage.textContent =
            "E  //  " +
            nearbyObject.name;

        interactionMessage.classList.add(
            "visible"
        );

    }} else {{

        interactionMessage.classList.remove(
            "visible"
        );
    }}
}}


/* =====================================================
   INACCESSIBLE
   ===================================================== */

function inaccessible() {{

    status.textContent =
        "SYSTEM // 접근할 수 없는 과정입니다.";
}}


/* =====================================================
   INTERACTION
   ===================================================== */

function interact() {{

    if (
        paused ||
        computerOpen ||
        inventoryOpen ||
        helpOpen ||
        cardOpen
    ) {{
        return;
    }}

    if (!nearbyObject) {{
        return;
    }}


    /* =================================================
       COMPUTER
       ================================================= */

    if (
        nearbyObject.id ===
        "computer"
    ) {{

        if (
            tutorialStep === 1
        ) {{

            tutorialStep = 2;

            startChat(2);

        }} else if (
            tutorialStep !== 2
        ) {{

            inaccessible();

            return;
        }}

        openComputer();

        return;
    }}


    /* =================================================
       DESK
       ================================================= */

    if (
        nearbyObject.id ===
        "desk"
    ) {{

        if (
            tutorialStep !== 3 &&
            tutorialStep !== 4
        ) {{

            inaccessible();

            return;
        }}


        if (
            tutorialStep === 3
        ) {{

            if (
                !accessKeyCreated
            ) {{
                inaccessible();
                return;
            }}

            tutorialStep = 4;

            startChat(4);

            status.textContent =
                "DESK // ACCESS KEY READY";

            return;
        }}


        if (
            tutorialStep === 4
        ) {{

            collectAccessKey();

            return;
        }}

        return;
    }}


    /* =================================================
       EXIT
       ================================================= */

    if (
        nearbyObject.id ===
        "exitWall"
    ) {{

        if (
            tutorialStep !== 5
        ) {{

            inaccessible();

            return;
        }}

        if (
            !accessKeyCollected
        ) {{

            inaccessible();

            return;
        }}

        openCardSwipe();

        return;
    }}
}}


/* =====================================================
   COMPUTER
   ===================================================== */

function openComputer() {{

    if (
        tutorialStep !== 2
    ) {{

        inaccessible();

        return;
    }}


    computerOpen = true;

    clearMovementKeys();

    interactionMessage.classList.remove(
        "visible"
    );

    codeDisplayNumber.textContent =
        ACCESS_CODE;

    codeInput.value = "";

    codeError.textContent = "";

    computerOverlay.style.display =
        "flex";


    setTimeout(
        function() {{
            codeInput.focus();
        }},
        80
    );
}}


function closeComputer() {{

    computerOpen = false;

    computerOverlay.style.display =
        "none";

    codeInput.blur();

    focusGame();
}}


/* =====================================================
   CODE SUBMIT
   ===================================================== */

function submitCode() {{

    const entered =
        codeInput.value.trim();


    if (
        entered ===
        ACCESS_CODE
    ) {{

        tutorialStep = 3;

        closeComputer();


        /*
         * 코드 입력 즉시
         * 책상 위에 ACCESS KEY 생성
         */

        accessKeyCreated = true;

        accessKey.classList.add(
            "visible"
        );


        status.textContent =
            "ECHO TERMINAL // CODE VERIFIED";


        startChat(4);

    }} else {{

        codeError.textContent =
            "ACCESS DENIED // 화면에 표시된 숫자를 그대로 입력하십시오.";

        codeInput.select();
    }}
}}


codeButton.addEventListener(
    "click",
    submitCode
);


codeInput.addEventListener(
    "keydown",
    function(event) {{

        if (
            event.key === "Enter"
        ) {{

            submitCode();

            event.preventDefault();
        }}

        if (
            event.key === "Escape"
        ) {{

            closeComputer();

            event.preventDefault();
        }}
    }}
);


/* =====================================================
   ACCESS KEY
   ===================================================== */

function collectAccessKey() {{

    if (
        !accessKeyCreated
    ) {{
        inaccessible();
        return;
    }}


    accessKeyCreated = false;

    accessKeyCollected = true;

    accessKey.classList.remove(
        "visible"
    );


    inventory[0] = {{
        name:
            "ACCESS KEY",

        description:
            "ECHO TERMINAL에서 인증된 보안구역 접근 키입니다."
    }};


    renderInventory();


    tutorialStep = 5;


    exitArrow.classList.add(
        "active"
    );


    startChat(5);


    status.textContent =
        "SYSTEM // ACCESS KEY ACQUIRED";
}}


/* =====================================================
   CARD SWIPE
   ===================================================== */

function openCardSwipe() {{

    cardOpen = true;

    clearMovementKeys();

    cardOverlay.style.display =
        "flex";

    cardReader.classList.remove(
        "success"
    );

    accessCard.style.left =
        "20px";
}}


function closeCardSwipe() {{

    cardOpen = false;

    cardOverlay.style.display =
        "none";

    focusGame();
}}


cardClose.addEventListener(
    "click",
    closeCardSwipe
);


/* =====================================================
   CARD DRAG
   ===================================================== */

let draggingCard = false;

let cardPointerOffsetX = 0;


accessCard.addEventListener(
    "pointerdown",
    function(event) {{

        if (!cardOpen) {{
            return;
        }}

        draggingCard = true;

        accessCard.setPointerCapture(
            event.pointerId
        );


        const cardRect =
            accessCard.getBoundingClientRect();

        cardPointerOffsetX =
            event.clientX -
            cardRect.left;

        event.preventDefault();
    }}
);


accessCard.addEventListener(
    "pointermove",
    function(event) {{

        if (!draggingCard) {{
            return;
        }}


        const readerRect =
            cardReader.getBoundingClientRect();

        const cardWidth =
            accessCard.offsetWidth;


        let x =
            event.clientX -
            readerRect.left -
            cardPointerOffsetX;


        const minX = 10;

        const maxX =
            readerRect.width -
            cardWidth -
            10;


        x =
            Math.max(
                minX,
                Math.min(
                    maxX,
                    x
                )
            );


        accessCard.style.left =
            x + "px";


        /*
         * 리더기 위치까지 이동하면
         * 인증 성공
         */

        if (
            x >=
            maxX - 25
        ) {{

            draggingCard = false;

            cardReader.classList.add(
                "success"
            );


            setTimeout(
                function() {{

                    closeCardSwipe();

                    status.textContent =
                        "SECURITY DOOR // ACCESS GRANTED";

                    startChat(6);

                }},
                650
            );
        }}

        event.preventDefault();
    }}
);


function stopCardDrag(event) {{

    if (!draggingCard) {{
        return;
    }}

    draggingCard = false;

    try {{
        accessCard.releasePointerCapture(
            event.pointerId
        );
    }} catch (error) {{}}
}}


accessCard.addEventListener(
    "pointerup",
    stopCardDrag
);

accessCard.addEventListener(
    "pointercancel",
    stopCardDrag
);


/* =====================================================
   INVENTORY
   ===================================================== */

inventorySlots.forEach(
    function(slot) {{

        slot.addEventListener(
            "click",
            function() {{

                const index =
                    Number(
                        slot.dataset.slot
                    );


                inventorySlots.forEach(
                    function(other) {{

                        other.classList.remove(
                            "selected"
                        );
                    }}
                );


                slot.classList.add(
                    "selected"
                );


                const item =
                    inventory[index];


                if (item) {{

                    itemDescription.innerHTML =
                        `${{item.name}}
                        <br><br>
                        ${{item.description}}`;

                }} else {{

                    itemDescription.innerHTML =
                        "ITEM DESCRIPTION<br><br>비어 있는 슬롯입니다.";
                }}
            }}
        );
    }}
);


/* =====================================================
   INVENTORY
   ===================================================== */

function openInventory() {{

    if (
        paused ||
        computerOpen ||
        cardOpen
    ) {{
        return;
    }}


    helpOpen = false;

    helpOverlay.style.display =
        "none";

    inventoryOpen = true;

    inventoryOverlay.style.display =
        "flex";

    clearMovementKeys();
}}


function closeInventory() {{

    inventoryOpen = false;

    inventoryOverlay.style.display =
        "none";

    focusGame();
}}


/* =====================================================
   HELP
   ===================================================== */

function openHelp() {{

    if (
        paused ||
        computerOpen ||
        cardOpen
    ) {{
        return;
    }}


    inventoryOpen = false;

    inventoryOverlay.style.display =
        "none";

    helpOpen = true;

    helpOverlay.style.display =
        "flex";

    clearMovementKeys();
}}


function closeHelp() {{

    helpOpen = false;

    helpOverlay.style.display =
        "none";

    focusGame();
}}


/* =====================================================
   FOCUS
   ===================================================== */

function focusGame() {{

    try {{

        gameRoot.focus(
            {{
                preventScroll: true
            }}
        );

    }} catch (error) {{

        gameRoot.focus();
    }}
}}


gameRoot.addEventListener(
    "pointerdown",
    function() {{

        if (
            !computerOpen &&
            !cardOpen
        ) {{
            focusGame();
        }}
    }}
);


window.addEventListener(
    "load",
    function() {{

        setTimeout(
            focusGame,
            100
        );
    }}
);


window.addEventListener(
    "blur",
    clearMovementKeys
);


/* =====================================================
   KEYBOARD
   ===================================================== */

function handleKeyDown(event) {{

    const key =
        event.key.toLowerCase();


    /*
     * 컴퓨터 입력창
     */

    if (
        document.activeElement ===
        codeInput
    ) {{

        if (
            key === "escape"
        ) {{

            closeComputer();

            event.preventDefault();
        }}

        return;
    }


    /*
     * 카드 드래그
     */

    if (
        cardOpen
    ) {{
        return;
    }}


    /*
     * SPACE
     */

    if (
        key === " "
    ) {{

        handleChatSpace();

        event.preventDefault();

        return;
    }}


    /*
     * ESC
     */

    if (
        key === "escape"
    ) {{

        if (computerOpen) {{

            closeComputer();

            event.preventDefault();

            return;
        }}

        if (helpOpen) {{

            closeHelp();

            event.preventDefault();

            return;
        }}

        if (inventoryOpen) {{

            closeInventory();

            event.preventDefault();

            return;
        }}
    }}


    /*
     * H
     */

    if (
        key === "h"
    ) {{

        if (
            computerOpen
        ) {{
            return;
        }}

        if (
            helpOpen
        ) {{
            closeHelp();
        }} else {{
            openHelp();
        }}

        event.preventDefault();

        return;
    }}


    /*
     * I
     */

    if (
        key === "i"
    ) {{

        if (
            computerOpen ||
            helpOpen
        ) {{
            return;
        }}

        if (
            inventoryOpen
        ) {{
            closeInventory();
        }} else {{
            openInventory();
        }}

        event.preventDefault();

        return;
    }}


    /*
     * E
     */

    if (
        key === "e"
    ) {{

        interact();

        event.preventDefault();

        return;
    }}


    /*
     * WASD
     */

    if (
        key === "w" ||
        key === "a" ||
        key === "s" ||
        key === "d"
    ) {{

        if (
            !paused &&
            !helpOpen &&
            !inventoryOpen &&
            !computerOpen
        ) {{

            keys[key] = true;


            if (
                tutorialStep === 0
            ) {{

                tutorialStep = 1;

                startChat(1);

                status.textContent =
                    "TUTORIAL // MOVEMENT ENABLED";
            }}
        }}

        event.preventDefault();

        return;
    }}
}}


function handleKeyUp(event) {{

    const key =
        event.key.toLowerCase();


    if (
        key === "w" ||
        key === "a" ||
        key === "s" ||
        key === "d"
    ) {{

        keys[key] = false;

        event.preventDefault();
    }}
}}


document.addEventListener(
    "keydown",
    handleKeyDown,
    true
);


document.addEventListener(
    "keyup",
    handleKeyUp,
    true
);


/* =====================================================
   MOBILE CONTROLS
   ===================================================== */

document
    .querySelectorAll(
        ".control-button"
    )
    .forEach(
        function(button) {{

            const direction =
                button.dataset.direction;


            function press(event) {{

                event.preventDefault();

                if (
                    paused ||
                    helpOpen ||
                    inventoryOpen ||
                    computerOpen ||
                    cardOpen
                ) {{
                    return;
                }}


                keys[direction] = true;


                if (
                    tutorialStep === 0
                ) {{

                    tutorialStep = 1;

                    startChat(1);

                    status.textContent =
                        "TUTORIAL // MOVEMENT ENABLED";
                }}
            }}


            function release(event) {{

                event.preventDefault();

                keys[direction] = false;
            }}


            button.addEventListener(
                "pointerdown",
                press
            );

            button.addEventListener(
                "pointerup",
                release
            );

            button.addEventListener(
                "pointercancel",
                release
            );

            button.addEventListener(
                "pointerleave",
                release
            );
        }
    );


/* =====================================================
   MOVEMENT
   ===================================================== */

function updatePlayer() {{

    if (
        !paused &&
        !helpOpen &&
        !inventoryOpen &&
        !computerOpen &&
        !cardOpen
    ) {{

        let nextX = playerX;
        let nextY = playerY;


        if (keys.w) {{
            nextY -= moveSpeed;
        }}

        if (keys.s) {{
            nextY += moveSpeed;
        }}

        if (keys.a) {{
            nextX -= moveSpeed;
        }}

        if (keys.d) {{
            nextX += moveSpeed;
        }}


        nextX =
            Math.max(
                2,
                Math.min(
                    98,
                    nextX
                )
            );


        nextY =
            Math.max(
                2,
                Math.min(
                    98,
                    nextY
                )
            );


        /*
         * X와 Y를 각각 검사해서
         * 벽/물체 모서리에 부딪혀도
         * 미끄러지듯 움직일 수 있도록 한다.
         */

        if (
            canMoveTo(
                nextX,
                playerY
            )
        ) {{
            playerX = nextX;
        }}


        if (
            canMoveTo(
                playerX,
                nextY
            )
        ) {{
            playerY = nextY;
        }}


        player.style.left =
            playerX + "%";

        player.style.top =
            playerY + "%";


        checkInteraction();
    }}


    requestAnimationFrame(
        updatePlayer
    );
}}


/* =====================================================
   RESTART
   ===================================================== */

document
    .getElementById(
        "restartButton"
    )
    .addEventListener(
        "click",
        function(event) {{

            event.preventDefault();

            event.stopPropagation();


            /*
             * iframe에서 부모 URL을 읽지 않고
             * 직접 Streamlit 페이지에 action 전달
             */

            try {{

                window.top.location.href =
                    "?action=restart";

            }} catch (error) {{

                window.parent.location.href =
                    "?action=restart";
            }}
        }}
    );


/* =====================================================
   TITLE
   ===================================================== */

document
    .getElementById(
        "titleButton"
    )
    .addEventListener(
        "click",
        function(event) {{

            event.preventDefault();

            event.stopPropagation();


            try {{

                window.top.location.href =
                    "?action=title";

            }} catch (error) {{

                window.parent.location.href =
                    "?action=title";
            }}
        }}
    );


/* =====================================================
   PAUSE INITIAL
   ===================================================== */

if (
    paused
) {{

    pauseOverlay.style.display =
        "flex";
}}


/* =====================================================
   INITIAL POSITION
   ===================================================== */

player.style.left =
    playerX + "%";

player.style.top =
    playerY + "%";


/* =====================================================
   INITIAL
   ===================================================== */

checkInteraction();

focusGame();


/* =====================================================
   MOVEMENT LOOP
   ===================================================== */

requestAnimationFrame(
    updatePlayer
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
    height=1000,
    scrolling=False,
)
