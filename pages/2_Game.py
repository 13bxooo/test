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
# PAGE ACTION
# =========================================================

action = st.query_params.get("action")


if action == "restart":

    # 게임 전체 초기화

    st.session_state.game_paused = False

    st.query_params.clear()

    st.rerun()


elif action == "title":

    # query parameter 제거

    st.query_params.clear()

    # 실제 타이틀 페이지 이동

    st.switch_page("main.py")


# =========================================================
# SESSION STATE
# =========================================================

if "game_paused" not in st.session_state:

    st.session_state.game_paused = False


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

        src:
            url(data:font/ttf;base64,{font_base64})
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

        background:
            #000000 !important;

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

            top: 16px !important;
            right: 16px !important;

            width: 40px !important;
            height: 40px !important;

        }}


        .st-key-pause_game_button button {{

            width: 40px !important;
            height: 40px !important;

            font-size: 21px !important;

        }}

    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# PAUSE
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

    font-family:
        'NeoDungGeunMo';

    src:
        url(data:font/ttf;base64,{font_base64})
        format('truetype');

}}


/* =====================================================
   GLOBAL
   ===================================================== */

* {{

    box-sizing:
        border-box;

    user-select:
        none;

    -webkit-user-select:
        none;

}}


html,
body {{

    margin: 0;
    padding: 0;

    width: 100%;
    height: 100%;

    overflow: hidden;

    background:
        #000000;

    font-family:
        'NeoDungGeunMo',
        monospace;

}}


body {{

    color:
        #ffffff;

}}


/* =====================================================
   GAME
   ===================================================== */

.game {{

    position:
        relative;

    width:
        100vw;

    height:
        100vh;

    background:
        #000000;

    overflow:
        hidden;

    outline:
        none;

}}


/* =====================================================
   TOP
   ===================================================== */

.project-title {{

    position:
        absolute;

    top:
        24px;

    left:
        28px;

    font-size:
        18px;

    letter-spacing:
        1px;

    z-index:
        20;

}}


.stage-title {{

    position:
        absolute;

    top:
        52px;

    left:
        28px;

    font-size:
        13px;

    color:
        #777777;

    letter-spacing:
        1px;

    z-index:
        20;

}}


/* =====================================================
   GAME AREA
   ===================================================== */

.game-area {{

    position:
        absolute;

    top:
        90px;

    left:
        28px;

    right:
        28px;

    bottom:
        70px;

    overflow:
        hidden;

    background-color:
        #080808;

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

    background-size:
        40px 40px;

}}


/* =====================================================
   ROOM
   ===================================================== */

.room {{

    position:
        absolute;

    left:
        7%;

    top:
        8%;

    width:
        86%;

    height:
        82%;

    border:
        1px solid
        rgba(255,255,255,0.12);

    overflow:
        hidden;

}}


/* =====================================================
   ROOM LINES
   ===================================================== */

.room-line-horizontal {{

    position:
        absolute;

    left:
        0;

    right:
        0;

    top:
        50%;

    height:
        1px;

    background:
        rgba(255,255,255,0.045);

}}


.room-line-vertical {{

    position:
        absolute;

    top:
        0;

    bottom:
        0;

    left:
        50%;

    width:
        1px;

    background:
        rgba(255,255,255,0.045);

}}


/* =====================================================
   OBJECT
   ===================================================== */

.object {{

    position:
        absolute;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    background:
        #0b0b0b;

    border:
        1px solid
        rgba(255,255,255,0.22);

    color:
        #777777;

    font-size:
        12px;

    text-align:
        center;

}}


/* =====================================================
   COMPUTER
   ===================================================== */

.computer {{

    left:
        42%;

    top:
        13%;

    width:
        16%;

    height:
        14%;

}}


/* =====================================================
   DESK
   ===================================================== */

.desk {{

    left:
        35%;

    top:
        62%;

    width:
        30%;

    height:
        12%;

}}


/* =====================================================
   EXIT
   ===================================================== */

.exit-door {{

    right:
        0;

    top:
        35%;

    width:
        8%;

    height:
        30%;

    background:
        #111111;

    writing-mode:
        vertical-rl;

    letter-spacing:
        2px;

}}


/* =====================================================
   LABEL
   ===================================================== */

.object-label {{

    position:
        absolute;

    bottom:
        -22px;

    left:
        50%;

    transform:
        translateX(-50%);

    white-space:
        nowrap;

    font-size:
        10px;

    color:
        #555555;

}}


/* =====================================================
   ACCESS KEY
   ===================================================== */

.access-key {{

    position:
        absolute;

    width:
        18px;

    height:
        8px;

    left:
        50%;

    top:
        45%;

    transform:
        translate(-50%, -50%);

    background:
        #ffffff;

    box-shadow:
        0 0 0 1px #000000;

    display:
        none;

}}


.access-key::after {{

    content:
        "";

    position:
        absolute;

    right:
        -7px;

    top:
        2px;

    width:
        7px;

    height:
        4px;

    background:
        #ffffff;

}}


.access-key.visible {{

    display:
        block;

}}


/* =====================================================
   PLAYER
   ===================================================== */

.player {{

    position:
        absolute;

    width:
        24px;

    height:
        24px;

    left:
        50%;

    top:
        43%;

    transform:
        translate(-50%, -50%);

    background:
        #ffffff;

    z-index:
        15;

    box-shadow:
        0 0 0 1px #000000;

}}


.player::after {{

    content:
        "";

    position:
        absolute;

    left:
        4px;

    right:
        4px;

    bottom:
        -5px;

    height:
        4px;

    background:
        rgba(255,255,255,0.15);

}}


/* =====================================================
   INTERACTION MESSAGE
   ===================================================== */

.interaction-message {{

    position:
        absolute;

    left:
        50%;

    bottom:
        19%;

    transform:
        translateX(-50%);

    padding:
        9px 16px;

    background:
        #000000;

    border:
        1px solid #333333;

    font-size:
        12px;

    color:
        #ffffff;

    opacity:
        0;

    pointer-events:
        none;

    transition:
        opacity 0.1s linear;

    z-index:
        40;

    white-space:
        nowrap;

}}


.interaction-message.visible {{

    opacity:
        1;

}}


/* =====================================================
   ECHO CHAT
   ===================================================== */

.echo-bar {{

    position:
        absolute;

    left:
        50%;

    bottom:
        3%;

    transform:
        translateX(-50%);

    width:
        min(760px, 82%);

    min-height:
        74px;

    padding:
        13px 18px;

    background:
        #050505;

    border:
        1px solid #3a3a3a;

    z-index:
        35;

}}


.echo-name {{

    font-size:
        11px;

    color:
        #ffffff;

    letter-spacing:
        1px;

    margin-bottom:
        8px;

}}


.echo-message {{

    font-size:
        12px;

    color:
        #999999;

    line-height:
        1.7;

}}


.echo-next {{

    position:
        absolute;

    right:
        12px;

    bottom:
        8px;

    font-size:
        9px;

    color:
        #555555;

}}


/* =====================================================
   STATUS
   ===================================================== */

.status {{

    position:
        absolute;

    bottom:
        24px;

    left:
        28px;

    font-size:
        14px;

    color:
        #777777;

    z-index:
        20;

}}


/* =====================================================
   COMMON OVERLAY
   ===================================================== */

.overlay {{

    position:
        absolute;

    inset:
        0;

    z-index:
        100;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    background:
        rgba(0,0,0,0.90);

}}


/* =====================================================
   INVENTORY
   ===================================================== */

.inventory-panel {{

    width:
        min(820px, 88vw);

    background:
        #050505;

    padding:
        34px 38px;

}}


.inventory-header {{

    display:
        flex;

    justify-content:
        space-between;

    align-items:
        center;

    padding-bottom:
        18px;

    margin-bottom:
        22px;

    border-bottom:
        1px solid #333333;

}}


.inventory-title {{

    font-size:
        24px;

}}


.inventory-close {{

    font-size:
        12px;

    color:
        #666666;

}}


.inventory-grid {{

    display:
        grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap:
        10px;

}}


.inventory-slot {{

    position:
        relative;

    aspect-ratio:
        1 / 1;

    background:
        #090909;

    border:
        1px solid #292929;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    cursor:
        pointer;

}}


.inventory-slot:hover,
.inventory-slot.selected {{

    background:
        #ffffff;

    color:
        #000000;

}}


.slot-number {{

    position:
        absolute;

    top:
        7px;

    left:
        9px;

    font-size:
        10px;

    color:
        #555555;

}}


.item-name {{

    font-size:
        13px;

    text-align:
        center;

}}


.empty-text {{

    color:
        #444444;

    font-size:
        11px;

}}


.item-description {{

    min-height:
        70px;

    margin-top:
        20px;

    padding:
        15px;

    background:
        #090909;

    border-top:
        1px solid #292929;

    font-size:
        12px;

    line-height:
        1.8;

    color:
        #888888;

}}


/* =====================================================
   HELP
   ===================================================== */

.help-panel {{

    width:
        min(760px, 86vw);

    max-height:
        82vh;

    overflow-y:
        auto;

    background:
        #050505;

    padding:
        36px 40px;

}}


.help-header {{

    display:
        flex;

    justify-content:
        space-between;

    padding-bottom:
        18px;

    margin-bottom:
        20px;

    border-bottom:
        1px solid #333333;

}}


.help-title {{

    font-size:
        24px;

}}


.help-close {{

    font-size:
        12px;

    color:
        #666666;

}}


.help-row {{

    display:
        flex;

    gap:
        20px;

    padding:
        14px 0;

    border-bottom:
        1px solid #1f1f1f;

}}


.help-number {{

    width:
        30px;

    color:
        #555555;

}}


.help-key {{

    width:
        145px;

    font-size:
        14px;

}}


.help-description {{

    color:
        #888888;

    font-size:
        12px;

    line-height:
        1.7;

}}


/* =====================================================
   COMPUTER
   ===================================================== */

.computer-overlay {{

    position:
        absolute;

    inset:
        0;

    z-index:
        120;

    display:
        none;

    align-items:
        center;

    justify-content:
        center;

    background:
        rgba(0,0,0,0.94);

}}


.computer-panel {{

    width:
        min(520px, 86vw);

    background:
        #050505;

    border:
        1px solid #333333;

    padding:
        28px;

}}


.computer-title {{

    font-size:
        20px;

    margin-bottom:
        8px;

}}


.computer-sub {{

    color:
        #666666;

    font-size:
        11px;

    margin-bottom:
        24px;

}}


.code-input {{

    width:
        100%;

    height:
        48px;

    border:
        1px solid #444444;

    background:
        #000000;

    color:
        #ffffff;

    font-family:
        'NeoDungGeunMo',
        monospace;

    font-size:
        22px;

    text-align:
        center;

    letter-spacing:
        6px;

    outline:
        none;

}}


.code-input:focus {{

    border-color:
        #ffffff;

}}


.code-button {{

    width:
        100%;

    height:
        44px;

    margin-top:
        10px;

    border:
        none;

    background:
        #ffffff;

    color:
        #000000;

    font-family:
        'NeoDungGeunMo',
        monospace;

    cursor:
        pointer;

}}


.code-button:hover {{

    background:
        #bbbbbb;

}}


.code-error {{

    min-height:
        20px;

    margin-top:
        12px;

    color:
        #777777;

    font-size:
        11px;

    text-align:
        center;

}}


/* =====================================================
   PAUSE
   ===================================================== */

.pause-overlay {{

    position:
        absolute;

    inset:
        0;

    z-index:
        90;

    display:
        none;

    align-items:
        center;

    justify-content:
        center;

    background:
        rgba(0,0,0,0.90);

}}


.pause-title {{

    font-size:
        28px;

    text-align:
        center;

    margin-bottom:
        14px;

}}


.pause-sub {{

    color:
        #777777;

    font-size:
        13px;

    text-align:
        center;

}}


/* =====================================================
   MOBILE CONTROLS
   ===================================================== */

.mobile-controls {{

    display:
        none;

    position:
        absolute;

    right:
        22px;

    bottom:
        22px;

    width:
        132px;

    height:
        132px;

    z-index:
        150;

}}


.control-button {{

    position:
        absolute;

    width:
        42px;

    height:
        42px;

    padding:
        0;

    border:
        1px solid #555555;

    background:
        rgba(0,0,0,0.88);

    color:
        #ffffff;

    font-family:
        'NeoDungGeunMo',
        monospace;

    font-size:
        20px;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    touch-action:
        none;

}}


.control-button:active {{

    background:
        #ffffff;

    color:
        #000000;

}}


.control-up {{

    top:
        0;

    left:
        45px;

}}


.control-left {{

    top:
        45px;

    left:
        0;

}}


.control-right {{

    top:
        45px;

    right:
        0;

}}


.control-down {{

    bottom:
        0;

    left:
        45px;

}}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {{

    .project-title {{

        top:
            18px;

        left:
            16px;

        font-size:
            14px;

    }}


    .stage-title {{

        top:
            40px;

        left:
            16px;

        font-size:
            11px;

    }}


    .game-area {{

        top:
            68px;

        left:
            16px;

        right:
            16px;

        bottom:
            58px;

        background-size:
            30px 30px;

    }}


    .status {{

        left:
            16px;

        bottom:
            18px;

        font-size:
            11px;

    }}


    .echo-bar {{

        width:
            90%;

        bottom:
            2%;

    }}


    .inventory-panel,
    .help-panel {{

        width:
            90vw;

        padding:
            24px 20px;

    }}


    .inventory-grid {{

        gap:
            6px;

    }}


    .item-name {{

        font-size:
            10px;

    }}


    .help-row {{

        gap:
            10px;

    }}


    .help-key {{

        width:
            90px;

        font-size:
            11px;

    }}


    .help-description {{

        font-size:
            10px;

    }}


    .mobile-controls {{

        display:
            block;

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
         TOP
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


        <!-- =================================================
             MOBILE CONTROLS
             ================================================= -->

        <div class="mobile-controls">


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
             ROOM
             ================================================= -->

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
                 EXIT
                 ================================================= -->

            <div
                class="object exit-door"
                id="exitDoor"
            >

                EXIT

                <div class="object-label">
                    SECURITY DOOR
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
                 ECHO CHAT
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


                <div class="echo-next">
                    E // NEXT
                </div>

            </div>


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
                        연구시설 내부를 이동합니다.
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
                        SYSTEM<br>
                        SPACE
                    </div>

                    <div class="help-description">
                        시스템 메시지를 확인합니다.
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
                        조작 방법을 다시 확인합니다.
                    </div>

                </div>


                <div
                    style="
                    margin-top:22px;
                    padding:16px;
                    background:#090909;
                    border-left:2px solid #ffffff;
                    "
                >

                    <div
                        style="
                        margin-bottom:8px;
                        font-size:13px;
                        "
                    >
                        IMPORTANT
                    </div>


                    <div
                        style="
                        color:#888888;
                        font-size:11px;
                        line-height:1.8;
                        "
                    >

                        시설 내부의 물체와 기록을
                        자세히 조사하세요.<br>

                        ECHO가 제공하는 모든 정보가
                        사실이라고 가정해서는 안 됩니다.<br>

                        서로 모순되는 단서가 발견될 수도 있습니다.

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
                    ENTER THE ACCESS SEQUENCE PROVIDED BY ECHO.
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
   GAME STATE
   ===================================================== */

let paused =
    {str(paused).lower()};


let tutorialStep =
    0;


let inventoryOpen =
    false;


let helpOpen =
    false;


let computerOpen =
    false;


let accessKeyCreated =
    false;


let accessKeyCollected =
    false;


/* =====================================================
   ACCESS CODE
   ===================================================== */

const ACCESS_CODE =
    "4817";


/* =====================================================
   ELEMENTS
   ===================================================== */

const gameRoot =
    document.getElementById(
        "gameRoot"
    );


const player =
    document.getElementById(
        "player"
    );


const room =
    document.querySelector(
        ".room"
    );


const inventoryOverlay =
    document.getElementById(
        "inventoryOverlay"
    );


const helpOverlay =
    document.getElementById(
        "helpOverlay"
    );


const computerOverlay =
    document.getElementById(
        "computerOverlay"
    );


const pauseOverlay =
    document.getElementById(
        "pauseOverlay"
    );


const interactionMessage =
    document.getElementById(
        "interactionMessage"
    );


const echoMessage =
    document.getElementById(
        "echoMessage"
    );


const status =
    document.getElementById(
        "status"
    );


const accessKey =
    document.getElementById(
        "accessKey"
    );


const codeInput =
    document.getElementById(
        "codeInput"
    );


const codeButton =
    document.getElementById(
        "codeButton"
    );


const codeError =
    document.getElementById(
        "codeError"
    );


const inventorySlots =
    document.querySelectorAll(
        ".inventory-slot"
    );


const itemDescription =
    document.getElementById(
        "itemDescription"
    );


/* =====================================================
   PLAYER
   ===================================================== */

let playerX =
    50;


let playerY =
    43;


const moveSpeed =
    0.65;


/* =====================================================
   KEY STATE
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
   ECHO TUTORIAL
   ===================================================== */

const tutorialMessages = [

    "연결이 확인되었습니다. 저는 ECHO입니다. 이 시설에서의 첫 번째 절차를 안내하겠습니다.",

    "먼저 이동 방법을 익혀야 합니다. W A S D 키를 사용하여 시설 내부를 이동해 보세요. 중앙의 COMPUTER로 이동하십시오.",

    "좋습니다. COMPUTER에 접근했습니다. 가까운 물체에서는 E 키를 사용하여 상호작용할 수 있습니다. COMPUTER를 조사하십시오.",

    "확인되었습니다. 이제 제가 전달하는 접근 코드를 COMPUTER에 입력하십시오. 접근 코드: 4817",

    "코드가 확인되었습니다. DESK를 확인하십시오. 필요한 ACCESS KEY가 생성되었습니다.",

    "ACCESS KEY를 획득했습니다. 이것으로 다음 구역으로 이동할 수 있습니다. EXIT로 이동하여 E 키를 눌러보십시오."

];


function setEchoMessage(message) {{

    echoMessage.textContent =
        message;

}}


setEchoMessage(
    tutorialMessages[0]
);


/* =====================================================
   OBJECTS
   ===================================================== */

const objects = [

    {{

        id:
            "computer",

        name:
            "ECHO TERMINAL",

        x:
            42,

        y:
            13,

        width:
            16,

        height:
            14

    }},


    {{

        id:
            "desk",

        name:
            "RESEARCH DESK",

        x:
            35,

        y:
            62,

        width:
            30,

        height:
            12

    }},


    {{

        id:
            "exitDoor",

        name:
            "SECURITY DOOR",

        x:
            92,

        y:
            35,

        width:
            8,

        height:
            30

    }}

];


let nearbyObject =
    null;


/* =====================================================
   DISTANCE
   ===================================================== */

function distanceToObject(object) {{

    const centerX =
        object.x +
        object.width / 2;


    const centerY =
        object.y +
        object.height / 2;


    const dx =
        playerX -
        centerX;


    const dy =
        playerY -
        centerY;


    return Math.sqrt(
        dx * dx +
        dy * dy
    );

}}


/* =====================================================
   INTERACTION CHECK
   ===================================================== */

function checkInteraction() {{

    nearbyObject =
        null;


    let closestDistance =
        Infinity;


    objects.forEach(
        function(object) {{

            const distance =
                distanceToObject(
                    object
                );


            if (
                distance < 12 &&
                distance < closestDistance
            ) {{

                nearbyObject =
                    object;


                closestDistance =
                    distance;

            }}

        }}
    );


    if (
        nearbyObject &&
        !computerOpen &&
        !inventoryOpen &&
        !helpOpen
    ){{

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
   INTERACT
   ===================================================== */

function interact() {{

    if (
        paused ||
        computerOpen ||
        inventoryOpen ||
        helpOpen
    ){{

        return;

    }}


    if (!nearbyObject) {{

        return;

    }}


    /* =================================================
       STEP 0
       이동 전에 E를 누르면 차단
       ================================================= */

    if (
        tutorialStep === 0
    ){{

        inaccessible();

        return;

    }}


    /* =================================================
       STEP 1
       COMPUTER
       ================================================= */

    if (
        tutorialStep === 1
    ){{

        if (
            nearbyObject.id !==
            "computer"
        ){{

            inaccessible();

            return;

        }}


        tutorialStep =
            2;


        openComputer();


        setEchoMessage(
            tutorialMessages[2]
        );


        status.textContent =
            "ECHO SYSTEM // TERMINAL CONNECTED";


        return;

    }}


    /* =================================================
       STEP 2
       COMPUTER CODE
       ================================================= */

    if (
        tutorialStep === 2
    ){{

        if (
            nearbyObject.id !==
            "computer"
        ){{

            inaccessible();

            return;

        }}


        openComputer();


        return;

    }}


    /* =================================================
       STEP 3
       DESK
       ================================================= */

    if (
        tutorialStep === 3
    ){{

        if (
            nearbyObject.id !==
            "desk"
        ){{

            inaccessible();

            return;

        }}


        tutorialStep =
            4;


        accessKeyCreated =
            true;


        accessKey.classList.add(
            "visible"
        );


        setEchoMessage(
            tutorialMessages[4]
        );


        status.textContent =
            "DESK // ACCESS KEY GENERATED";


        return;

    }}


    /* =================================================
       STEP 4
       GET ACCESS KEY
       ================================================= */

    if (
        tutorialStep === 4
    ){{

        if (
            nearbyObject.id !==
            "desk"
        ){{

            inaccessible();

            return;

        }}


        accessKeyCreated =
            false;


        accessKey.classList.remove(
            "visible"
        );


        accessKeyCollected =
            true;


        inventory[0] = {{

            name:
                "ACCESS KEY",

            description:
                "ECHO TERMINAL에서 인증된 보안구역 접근 키입니다."

        }};


        renderInventory();


        tutorialStep =
            5;


        setEchoMessage(
            tutorialMessages[5]
        );


        status.textContent =
            "SYSTEM // ACCESS KEY ACQUIRED";


        return;

    }}


    /* =================================================
       STEP 5
       EXIT
       ================================================= */

    if (
        tutorialStep === 5
    ){{

        if (
            nearbyObject.id !==
            "exitDoor"
        ){{

            inaccessible();

            return;

        }}


        if (
            !accessKeyCollected
        ){{

            inaccessible();

            return;

        }}


        status.textContent =
            "SECURITY DOOR // ACCESS GRANTED";


        setEchoMessage(
            "튜토리얼 절차가 완료되었습니다. 다음 구역으로 이동할 준비가 되었습니다."
        );


        return;

    }}

}}


/* =====================================================
   COMPUTER
   ===================================================== */

function openComputer() {{

    if (
        tutorialStep !== 2
    ){{

        inaccessible();

        return;

    }}


    computerOpen =
        true;


    clearMovementKeys();


    interactionMessage.classList.remove(
        "visible"
    );


    computerOverlay.style.display =
        "flex";


    codeError.textContent =
        "";


    codeInput.value =
        "";


    setTimeout(
        function(){{

            codeInput.focus();

        }},
        50
    );

}}


function closeComputer() {{

    computerOpen =
        false;


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
    ){{

        tutorialStep =
            3;


        closeComputer();


        status.textContent =
            "ECHO TERMINAL // CODE VERIFIED";


        setEchoMessage(
            "코드가 확인되었습니다. 이제 DESK로 이동하십시오. 그곳에서 ACCESS KEY를 확인할 수 있습니다."
        );


    }} else {{

        codeError.textContent =
            "ACCESS DENIED // ECHO가 전달한 숫자를 그대로 입력하십시오.";


        codeInput.select();

    }}

}}


codeButton.addEventListener(
    "click",
    submitCode
);


codeInput.addEventListener(
    "keydown",
    function(event){{

        if (
            event.key ===
            "Enter"
        ){{

            submitCode();

            event.preventDefault();

        }}


        if (
            event.key ===
            "Escape"
        ){{

            closeComputer();

            event.preventDefault();

        }}

    }}
);


/* =====================================================
   INVENTORY
   ===================================================== */

inventorySlots.forEach(
    function(slot){{

        slot.addEventListener(
            "click",
            function(){{

                const index =
                    Number(
                        slot.dataset.slot
                    );


                inventorySlots.forEach(
                    function(other){{

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


                if (item){{

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
   INVENTORY OPEN
   ===================================================== */

function openInventory() {{

    if (
        paused ||
        computerOpen
    ){{

        return;

    }}


    helpOpen =
        false;


    helpOverlay.style.display =
        "none";


    inventoryOpen =
        true;


    inventoryOverlay.style.display =
        "flex";


    clearMovementKeys();

}}


/* =====================================================
   INVENTORY CLOSE
   ===================================================== */

function closeInventory() {{

    inventoryOpen =
        false;


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
        computerOpen
    ){{

        return;

    }}


    inventoryOpen =
        false;


    inventoryOverlay.style.display =
        "none";


    helpOpen =
        true;


    helpOverlay.style.display =
        "flex";


    clearMovementKeys();

}}


function closeHelp() {{

    helpOpen =
        false;


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
                preventScroll:
                    true
            }}
        );

    }} catch (error) {{

        gameRoot.focus();

    }}

}}


gameRoot.addEventListener(
    "pointerdown",
    function(){{

        if (
            !computerOpen
        ){{

            focusGame();

        }}

    }}
);


window.addEventListener(
    "load",
    function(){{

        focusGame();

    }}
);


window.addEventListener(
    "blur",
    function(){{

        clearMovementKeys();

    }}
);


/* =====================================================
   KEYBOARD
   ===================================================== */

document.addEventListener(
    "keydown",
    function(event){{

        const key =
            event.key.toLowerCase();


        /*
         * 컴퓨터 입력창에 커서가 있을 때는
         * 게임 조작 키를 가로채지 않는다.
         */

        if (
            document.activeElement ===
            codeInput
        ){{

            if (
                key ===
                "escape"
            ){{

                closeComputer();

                event.preventDefault();

            }}

            return;

        }}


        /* =================================================
           ESC
           ================================================= */

        if (
            key ===
            "escape"
        ){{

            if (
                computerOpen
            ){{

                closeComputer();

                event.preventDefault();

                return;

            }}


            if (
                helpOpen
            ){{

                closeHelp();

                event.preventDefault();

                return;

            }}


            if (
                inventoryOpen
            ){{

                closeInventory();

                event.preventDefault();

                return;

            }}

        }}


        /* =================================================
           H
           ================================================= */

        if (
            key ===
            "h"
        ){{

            if (
                computerOpen
            ){{

                return;

            }}


            if (
                helpOpen
            ){{

                closeHelp();

            }} else {{

                openHelp();

            }}


            event.preventDefault();

            return;

        }}


        /* =================================================
           I
           ================================================= */

        if (
            key ===
            "i"
        ){{

            if (
                computerOpen ||
                helpOpen
            ){{

                return;

            }}


            if (
                inventoryOpen
            ){{

                closeInventory();

            }} else {{

                openInventory();

            }}


            event.preventDefault();

            return;

        }}


        /* =================================================
           E
           ================================================= */

        if (
            key ===
            "e"
        ){{

            interact();

            event.preventDefault();

            return;

        }}


        /* =================================================
           WASD
           ================================================= */

        if (
            key === "w" ||
            key === "a" ||
            key === "s" ||
            key === "d"
        ){{

            if (
                !paused &&
                !helpOpen &&
                !inventoryOpen &&
                !computerOpen
            ){{

                keys[key] =
                    true;


                /*
                 * 첫 번째 단계:
                 * 이동을 시작하면 튜토리얼 진행
                 */

                if (
                    tutorialStep ===
                    0
                ){{

                    tutorialStep =
                        1;


                    setEchoMessage(
                        tutorialMessages[1]
                    );


                    status.textContent =
                        "TUTORIAL // MOVEMENT ENABLED";

                }}

            }}


            event.preventDefault();

        }}

    }}
);


/* =====================================================
   KEYBOARD RELEASE
   ===================================================== */

document.addEventListener(
    "keyup",
    function(event){{

        const key =
            event.key.toLowerCase();


        if (
            key === "w" ||
            key === "a" ||
            key === "s" ||
            key === "d"
        ){{

            keys[key] =
                false;


            event.preventDefault();

        }}

    }}
);


/* =====================================================
   MOBILE CONTROLS
   ===================================================== */

document
    .querySelectorAll(
        ".control-button"
    )
    .forEach(
        function(button){{

            const direction =
                button.dataset.direction;


            button.addEventListener(
                "pointerdown",
                function(event){{

                    event.preventDefault();


                    if (
                        !paused &&
                        !helpOpen &&
                        !inventoryOpen &&
                        !computerOpen
                    ){{

                        keys[direction] =
                            true;


                        if (
                            tutorialStep ===
                            0
                        ){{

                            tutorialStep =
                                1;


                            setEchoMessage(
                                tutorialMessages[1]
                            );


                            status.textContent =
                                "TUTORIAL // MOVEMENT ENABLED";

                        }}

                    }}

                }}
            );


            function release(event){{

                event.preventDefault();

                keys[direction] =
                    false;

            }}


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

        }}
    );


/* =====================================================
   MOVEMENT LOOP
   ===================================================== */

function updatePlayer(){{

    if (
        !paused &&
        !helpOpen &&
        !inventoryOpen &&
        !computerOpen
    ){{

        if (
            keys.w
        ){{

            playerY -=
                moveSpeed;

        }}


        if (
            keys.s
        ){{

            playerY +=
                moveSpeed;

        }}


        if (
            keys.a
        ){{

            playerX -=
                moveSpeed;

        }}


        if (
            keys.d
        ){{

            playerX +=
                moveSpeed;

        }}


        playerX =
            Math.max(
                2,
                Math.min(
                    98,
                    playerX
                )
            );


        playerY =
            Math.max(
                2,
                Math.min(
                    98,
                    playerY
                )
            );


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
   RESTART / TITLE
   ===================================================== */

document
    .getElementById(
        "restartButton"
    )
    .addEventListener(
        "click",
        function(){{

            /*
             * 기존 코드처럼
             * window.parent.location.href를
             * 읽어서 URL 객체를 만드는 방식을
             * 사용하지 않는다.
             *
             * 부모 Streamlit 페이지에
             * action=restart를 전달한다.
             */

            window.parent.location.href =
                "?action=restart";

        }}
    );


document
    .getElementById(
        "titleButton"
    )
    .addEventListener(
        "click",
        function(){{

            window.parent.location.href =
                "?action=title";

        }}
    );


/* =====================================================
   PAUSE STATE
   ===================================================== */

if (
    paused
){{

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
   INITIAL INTERACTION
   ===================================================== */

checkInteraction();


/* =====================================================
   FOCUS
   ===================================================== */

focusGame();


/* =====================================================
   START MOVEMENT LOOP
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
