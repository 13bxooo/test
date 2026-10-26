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

    st.query_params.clear()
    for _key in list(st.session_state.keys()):
        if _key.startswith(("s1_", "tutorial_", "stage01_")):
            del st.session_state[_key]
    st.session_state.tutorial_reset_save = True
    st.session_state.game_started = True
    st.session_state.game_paused = False
    st.session_state.game_finished = False
    st.session_state.tutorial_complete = False
    st.session_state.stage01_started = False
    st.session_state.remaining_seconds = 15 * 60
    st.switch_page("pages/2_Game.py")


elif action == "title":

    st.session_state.game_paused = False
    st.session_state.show_title_warning = True
    st.query_params.clear()
    st.switch_page("main.py")

elif action == "stage01":

    st.session_state.game_paused = False
    st.session_state.game_started = True
    st.session_state.stage01_started = True
    st.session_state.start_open = False
    st.query_params.clear()
    st.switch_page("pages/3_Stage_01.py")


# =========================================================
# SESSION STATE
# =========================================================

if "game_paused" not in st.session_state:

    st.session_state.game_paused = False

# The tutorial page represents an active run, so CONTINUE can return here.
st.session_state.game_started = True


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


.st-key-tutorial_restart_native,
.st-key-tutorial_title_native {{
    position: fixed !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 170px !important;
    height: 42px !important;
    z-index: 1000001 !important;
    margin: 0 !important;
    padding: 0 !important;
}}
.st-key-tutorial_restart_native {{ top: calc(50vh + 58px) !important; }}
.st-key-tutorial_title_native {{ top: calc(50vh + 106px) !important; }}
.st-key-tutorial_restart_native button,
.st-key-tutorial_title_native button {{
    width: 170px !important;
    height: 42px !important;
    border: 0 !important;
    border-radius: 0 !important;
    background: #000 !important;
    color: #fff !important;
    font-family: 'NeoDungGeunMo', monospace !important;
    font-size: 15px !important;
}}
.st-key-tutorial_restart_native button:hover,
.st-key-tutorial_title_native button:hover {{
    background: #fff !important;
    color: #000 !important;
}}

.st-key-pause_game_button button {{

    width: 45px !important;
    height: 45px !important;

    padding: 0 !important;
    margin: 0 !important;

    border: none !important;
    border-radius: 0 !important;

    background: #000000 !important;
    color: #ffffff !important;

    font-family:
        'NeoDungGeunMo',
        monospace !important;

    font-size: 0 !important;
    position: relative !important;
}}
.st-key-pause_game_button button::before {{
    content: '';
    position: absolute;
    width: 4px;
    height: 15px;
    left: calc(50% - 5px);
    top: 50%;
    transform: translateY(-50%);
    background: #7cecff;
    box-shadow: 7px 0 0 #7cecff;
}}
.st-key-pause_game_button button:hover::before {{
    background: #000;
    box-shadow: 7px 0 0 #000;
}}

.st-key-pause_game_button button:hover {{

    background: #ffffff !important;
    color: #000000 !important;

}}


@media (max-width: 700px) {{

    .st-key-pause_game_button {{

        top: 12px !important;
        right: 12px !important;

        width: 40px !important;
        height: 40px !important;

    }}


    .st-key-pause_game_button button {{

        width: 40px !important;
        height: 40px !important;

        font-size: 20px !important;

    }}

}}


/* White-led inventory skin: preserve existing inventory behavior and card artwork. */
.inventory-panel{{background:#f4f7f8!important;color:#101820!important;border:2px solid #111!important;box-shadow:0 0 0 2px #d7e3e8,8px 8px 0 #000!important}}
.inventory-header{{border-bottom:2px solid #17232a!important}}
.inventory-title{{color:#101820!important;text-shadow:none!important}}
.inventory-close{{color:#52616b!important}}
.inventory-slot{{background:#fff!important;color:#111!important;border:2px solid #a9b8bf!important;box-shadow:inset 0 0 0 1px #edf2f4!important}}
.inventory-slot:hover,.inventory-slot.selected{{background:#dffaff!important;color:#06151a!important;border-color:#00a9c7!important;box-shadow:0 0 0 2px #7cecff!important}}
.slot-number{{color:#647780!important}}
.item-name{{color:#15252c!important}}
.empty-text{{color:#a3b0b6!important}}
.item-description{{background:#fff!important;color:#24343c!important;border-top:2px solid #a9b8bf!important;box-shadow:inset 0 0 0 1px #edf2f4!important}}
.item-description strong{{color:#006b80!important}}
.pixel-card-item{{background:#f4fcff!important;border:2px solid #008eaf!important;box-shadow:2px 0 #005a70,-2px 0 #005a70,0 2px #005a70,0 -2px #005a70,0 0 0 2px #d6faff!important}}
.pixel-card-chip{{background:#00bcd7!important;border:1px solid #004b5a!important}}
.pixel-card-mark{{color:#006b80!important}}
.pixel-card-lines{{border-color:#008eaf!important}}
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
    else "Ⅱ",
    key="pause_game_button",
)


if pause_clicked:

    st.session_state.game_paused = (
        not st.session_state.game_paused
    )

    st.rerun()


paused = st.session_state.game_paused

# RESTART / TITLE are native Streamlit buttons, not links inside components.html.
# Their fixed positions match the original pause-menu button positions.
if paused:
    restart_clicked = st.button("RESTART", key="tutorial_restart_native")
    title_clicked = st.button("TITLE", key="tutorial_title_native")

    if restart_clicked:
        for _key in list(st.session_state.keys()):
            if _key.startswith(("s1_", "tutorial_", "stage01_")):
                del st.session_state[_key]
        st.session_state.tutorial_reset_save = True
        st.session_state.game_started = True
        st.session_state.game_paused = False
        st.session_state.game_finished = False
        st.session_state.tutorial_complete = False
        st.session_state.stage01_started = False
        st.session_state.remaining_seconds = 15 * 60
        st.switch_page("pages/2_Game.py")

    if title_clicked:
        st.session_state.game_paused = False
        st.session_state.show_title_warning = True
        st.switch_page("main.py")


# =========================================================
# GAME HTML
# =========================================================

html = r"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">


<style>

/* =====================================================
   FONT
   ===================================================== */

@font-face {

    font-family:
        'NeoDungGeunMo';

    src:
        url(data:font/ttf;base64,__FONT_BASE64__)
        format('truetype');

}


/* =====================================================
   GLOBAL
   ===================================================== */

* {

    box-sizing:
        border-box;

    user-select:
        none;

    -webkit-user-select:
        none;

}


html,
body {

    margin:
        0;

    padding:
        0;

    width:
        100%;

    height:
        100%;

    overflow:
        hidden;

    background:
        #000000;

    color:
        #ffffff;

    font-family:
        'NeoDungGeunMo',
        monospace;

}


button,
input {

    font-family:
        'NeoDungGeunMo',
        monospace;

}


/* =====================================================
   GAME
   ===================================================== */

.game {

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

}


/* =====================================================
   TOP
   ===================================================== */

.project-title {

    position: absolute;
    top: 24px;
    left: 28px;
    font-size: 18px;
    letter-spacing: 1px;
    z-index: 20;
    color: #f4f4f4;
    text-shadow: none;

}


.stage-title {

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

}


/* =====================================================
   GAME AREA
   ===================================================== */

.game-area {

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

}


/* =====================================================
   ROOM
   ===================================================== */

.room {

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

}


/* =====================================================
   ROOM LINES
   ===================================================== */

.room-line-horizontal {

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

}


.room-line-vertical {

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

}


/* =====================================================
   OBJECT
   ===================================================== */

.object {

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

    z-index:
        5;

}


/* =====================================================
   MONITOR
   ===================================================== */

.monitor {

    left:
        43.5%;

    top:
        9%;

    width:
        13%;

    height:
        7%;

    background:
        #050505;

}


.monitor::after {

    content:
        "";

    position:
        absolute;

    left:
        10%;

    right:
        10%;

    bottom:
        -10px;

    height:
        10px;

    border:
        1px solid #333333;

    background:
        #080808;

}


/* =====================================================
   COMPUTER
   ===================================================== */

.computer {

    left:
        42%;

    top:
        13%;

    width:
        16%;

    height:
        14%;

}


/* =====================================================
   DESK
   ===================================================== */

.desk {

    left:
        35%;

    top:
        62%;

    width:
        30%;

    height:
        12%;

    align-items:
        flex-start;

    padding-top:
        10px;

}


.desk::after {

    content:
        "";

    position:
        absolute;

    left:
        8%;

    right:
        8%;

    bottom:
        -10px;

    height:
        10px;

    border:
        1px solid #222222;

    background:
        #070707;

}


/* =====================================================
   EXIT WALL
   ===================================================== */

.exit-wall {

    position:
        absolute;

    right:
        0;

    top:
        35%;

    width:
        8%;

    height:
        30%;

    background:
        #090909;

    border-left:
        1px solid #444444;

    z-index:
        5;

}


.exit-wall::before,
.exit-wall::after {

    content:
        "";

    position:
        absolute;

    left:
        0;

    right:
        0;

    height:
        1px;

    background:
        #333333;

}


.exit-wall::before {

    top:
        20%;

}


.exit-wall::after {

    bottom:
        20%;

}


/* =====================================================
   EXIT SIGN
   ===================================================== */

.exit-sign {

    position:
        absolute;

    right:
        9%;

    top:
        45%;

    transform:
        translateY(-50%);

    font-size:
        12px;

    letter-spacing:
        1px;

    color:
        #666666;

    text-align:
        right;

    line-height:
        1.8;

    z-index:
        6;

    white-space:
        nowrap;

}


.exit-arrow {

    display:
        inline-block;

    animation:
        exitPulse 1.1s ease-in-out infinite;

}


@keyframes exitPulse {

    0%,
    100% {

        transform:
            translateY(-3px);

        opacity:
            0.45;

    }

    50% {

        transform:
            translateY(3px);

        opacity:
            1;

    }

}


/* =====================================================
   OBJECT LABEL
   ===================================================== */

.object-label {

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

}


/* =====================================================
   ACCESS KEY
   ===================================================== */

.access-key {

    position:
        absolute;

    width:
        34px;

    height:
        15px;

    left:
        50%;

    top:
        45%;

    transform:
        translate(-50%, -50%);

    background:
        #ffffff;

    border:
        1px solid #000000;

    display:
        none;

    z-index:
        8;

    box-shadow:
        0 0 8px
        rgba(255,255,255,0.18);

}


.access-key::before {

    content:
        "";

    position:
        absolute;

    right:
        -12px;

    top:
        3px;

    width:
        12px;

    height:
        7px;

    background:
        #ffffff;

    border:
        1px solid #000000;

}


.access-key::after {

    content:
        "";

    position:
        absolute;

    left:
        4px;

    top:
        3px;

    width:
        7px;

    height:
        7px;

    border:
        2px solid #000000;

    border-radius:
        50%;

}


.access-key.visible {

    display:
        block;

    animation:
        keyAppear 0.35s steps(4);

}


@keyframes keyAppear {

    0% {

        opacity:
            0;

        transform:
            translate(-50%,-50%)
            scale(0.6);

    }

    100% {

        opacity:
            1;

        transform:
            translate(-50%,-50%)
            scale(1);

    }

}


/* =====================================================
   PLAYER
   ===================================================== */

.player {

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

}


.player::after {

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

}


/* =====================================================
   INTERACTION
   ===================================================== */

.interaction-message {

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

    z-index:
        40;

    white-space:
        nowrap;

}


.interaction-message.visible {

    opacity:
        1;

}


/* =====================================================
   ECHO CHAT
   ===================================================== */

.echo-bar {

    position:
        absolute;

    left:
        50%;

    bottom:
        3%;

    transform:
        translateX(-50%);

    width:
        min(760px,82%);

    min-height:
        78px;

    padding:
        13px 18px 20px;

    background:
        #050505;

    border:
        1px solid #3a3a3a;

    z-index:
        35;

}


.echo-name {

    font-size:
        11px;

    color:
        #ffffff;

    letter-spacing:
        1px;

    margin-bottom:
        8px;

}


.echo-message {

    font-size:
        12px;

    color:
        #aaaaaa;

    line-height:
        1.7;

    min-height:
        38px;

    white-space:
        pre-wrap;

}


.echo-next {

    position:
        absolute;

    right:
        12px;

    bottom:
        7px;

    font-size:
        9px;

    color:
        #555555;

}


.echo-next.ready {

    color:
        #ffffff;

    animation:
        blink 0.8s steps(2) infinite;

}


@keyframes blink {

    50% {

        opacity:
            0.35;

    }

}


/* =====================================================
   STATUS
   ===================================================== */

.status {

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

}


/* =====================================================
   COMMON OVERLAY
   ===================================================== */

.overlay {

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
        rgba(0,0,0,0.92);

}


/* =====================================================
   INVENTORY
   ===================================================== */

.inventory-panel {
    position: relative;
    width: min(820px, 88vw);
    padding: 24px 26px 26px;
    background: #02070c;
    color: #d8faff;
    border: 1px solid #48dfff;
    box-shadow: 0 0 0 1px #123c4d, 0 0 16px #00cfff22;
}


.inventory-header {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    min-height: 28px;
    padding: 0 0 8px 8px;
    margin: 0 0 14px;
    border-bottom: 1px solid #2587a7;
}


.inventory-title {
    color: #72eaff;
    font-size: 17px;
    letter-spacing: 1px;
    text-shadow: 0 0 5px #00cfff77;
}


.inventory-close {
    margin-left: auto;
    color: #4b8da0;
    font-size: 9px;
}


.inventory-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    grid-template-rows: repeat(3, minmax(0, 1fr));
    gap: 10px;
}


.inventory-slot {
    position: relative;
    aspect-ratio: 1 / 1;
    background: #01060b;
    border: 1px solid #28546a;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: inset 0 0 0 1px #06131d;
    color: #baf6ff;
}


.inventory-slot:hover,
.inventory-slot.selected {
    background: #03121b;
    color: #d8faff;
    border-color: #7cecff;
    box-shadow: 0 0 0 1px #1683a4, 0 0 9px #00cfff33;
}


.slot-number {

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

}


.item-name {

    font-size:
        13px;

    text-align:
        center;

}


.empty-text {

    color:
        #444444;

    font-size:
        11px;

}


.item-description {

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

}


/* =====================================================
   HELP
   ===================================================== */

.help-panel {

    width:
        min(760px,86vw);

    max-height:
        82vh;

    overflow-y:
        auto;

    background:
        #050505;

    padding:
        36px 40px;

}


.help-header {

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

}


.help-title {

    font-size:
        24px;

}


.help-close {

    font-size:
        12px;

    color:
        #666666;

}


.help-row {

    display:
        flex;

    gap:
        20px;

    padding:
        14px 0;

    border-bottom:
        1px solid #1f1f1f;

}


.help-number {

    width:
        30px;

    color:
        #555555;

}


.help-key {

    width:
        145px;

    font-size:
        14px;

}


.help-description {

    color:
        #888888;

    font-size:
        12px;

    line-height:
        1.7;

}


/* =====================================================
   COMPUTER
   ===================================================== */

.computer-overlay {

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

}


.computer-panel {

    width:
        min(540px,86vw);

    background:
        #050505;

    border:
        1px solid #333333;

    padding:
        28px;

}


.computer-title {

    font-size:
        20px;

    margin-bottom:
        8px;

}


.computer-sub {

    color:
        #666666;

    font-size:
        11px;

    margin-bottom:
        18px;

}


.access-sequence {

    padding:
        15px;

    margin-bottom:
        16px;

    border:
        1px solid #292929;

    text-align:
        center;

    color:
        #777777;

    font-size:
        11px;

}


.access-number {

    font-size:
        34px;

    color:
        #ffffff;

    letter-spacing:
        8px;

    margin-top:
        8px;

}


.code-input {

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

    font-size:
        22px;

    text-align:
        center;

    letter-spacing:
        6px;

    outline:
        none;

}


.code-input:focus {

    border-color:
        #ffffff;

}


.code-button {

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

    font-size:
        13px;

    cursor:
        pointer;

    padding:
        0 18px;

}


.code-button:hover {

    background:
        #bbbbbb;

}


.code-error {

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

}


/* Pixel-art access card shared by the draggable reader item and inventory icon */
.pixel-card-item{position:relative;width:42px;height:28px;margin:7px auto 5px;background:#073b58;border:2px solid #54eaff;box-shadow:2px 0 #bafaff,-2px 0 #bafaff,0 2px #bafaff,0 -2px #bafaff,0 0 8px #00dfff66;image-rendering:pixelated;transform:rotate(-8deg)}
.pixel-card-chip{position:absolute;left:5px;top:6px;width:8px;height:7px;background:#36e8ff;border:1px solid #b8fbff}
.pixel-card-mark{position:absolute;right:5px;top:2px;color:#9af7ff;font:bold 12px monospace}
.pixel-card-lines{position:absolute;left:5px;right:5px;bottom:4px;height:3px;border-top:1px solid #55eaff;border-bottom:1px solid #55eaff}
.card{background:#073b58!important;border:2px solid #54eaff!important;box-shadow:2px 0 #bafaff,-2px 0 #bafaff,0 2px #bafaff,0 -2px #bafaff,0 0 12px #00dfff66!important;image-rendering:pixelated!important}
.card-chip{background:#36e8ff!important;border:1px solid #b8fbff!important}
.card:after{content:"A";position:absolute;right:12px;top:12px;color:#9af7ff;font:bold 20px monospace;text-shadow:0 0 5px #00dfff}

/* =====================================================
   CARD ACCESS
   ===================================================== */

.card-overlay {

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

}


.card-panel {

    width:
        min(620px,90vw);

    background:
        #050505;

    border:
        1px solid #333333;

    padding:
        24px;

}


.card-header {

    display:
        flex;

    justify-content:
        space-between;

    border-bottom:
        1px solid #292929;

    padding-bottom:
        14px;

    margin-bottom:
        18px;

}


.card-title {

    font-size:
        18px;

}


.card-help {

    font-size:
        10px;

    color:
        #666666;

}


.card-stage {

    position:
        relative;

    height:
        260px;

    border:
        1px solid #242424;

    background:

        repeating-linear-gradient(
            0deg,
            transparent 0 31px,
            rgba(255,255,255,0.025) 32px
        ),

        repeating-linear-gradient(
            90deg,
            transparent 0 31px,
            rgba(255,255,255,0.025) 32px
        );

    overflow:
        hidden;

}


.reader {

    position:
        absolute;

    right:
        12%;

    top:
        50%;

    transform:
        translateY(-50%);

    width:
        120px;

    height:
        70px;

    border:
        1px solid #555555;

    background:
        #0b0b0b;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    color:
        #777777;

    font-size:
        10px;

}


.reader-light {
    position: absolute;
    top: 8px;
    right: 8px;
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: #ff3333;
    box-shadow: 0 0 8px #ff3333;
}
.reader-light.green {
    background: #36ff76;
    box-shadow: 0 0 12px #36ff76;
}
.fade-screen {
    position: absolute;
    inset: 0;
    z-index: 300;
    background: #000;
    opacity: 0;
    pointer-events: none;
    transition: opacity 1.5s linear;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.fade-screen.active { opacity: 1; pointer-events: auto; }
.fade-message {
    color: #e8e8e8;
    font-family: 'NeoDungGeunMo', monospace;
    letter-spacing: 3px;
    text-align: center;
    padding: 0 18px;
    opacity: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    text-shadow: none;
}
.fade-stage {
    font-size: clamp(22px, 3vw, 34px);
    text-shadow: 0 0 4px #fff, 0 0 12px #777;
}
.fade-room {
    font-size: clamp(12px, 1.4vw, 17px);
    letter-spacing: 2px;
    text-shadow: none;
}
.fade-screen.active .fade-message {
    opacity: 1;
}
.fade-screen.active .fade-stage {
    animation: blackoutText 1.5s steps(1, end) forwards;
}
@keyframes blackoutText {
    0% { opacity: 0; }
    18% { opacity: .95; }
    24% { opacity: .2; }
    31% { opacity: 1; }
    42% { opacity: .45; }
    50%, 100% { opacity: 1; }
}
@media (prefers-reduced-motion: reduce) {
    .fade-screen { transition: none; }
    .fade-screen.active .fade-message, .fade-screen.active .fade-stage { animation: none; opacity: 1; }
}

.reader-slot {

    position:
        absolute;

    left:
        10%;

    right:
        10%;

    top:
        50%;

    height:
        3px;

    background:
        #ffffff;

    box-shadow:
        0 0 8px
        rgba(255,255,255,0.3);

}


.card {

    position:
        absolute;

    left:
        12%;

    top:
        50%;

    width:
        130px;

    height:
        78px;

    transform:
        translateY(-50%);

    border:
        1px solid #ffffff;

    background:
        #111111;

    cursor:
        grab;

    touch-action:
        none;

    z-index:
        3;

    padding:
        12px;

    color:
        #ffffff;

    font-size:
        11px;

}


.card:active {

    cursor:
        grabbing;

}


.card-chip {

    width:
        22px;

    height:
        15px;

    border:
        1px solid #aaaaaa;

    margin-bottom:
        8px;

}


.card-status {

    margin-top:
        14px;

    min-height:
        18px;

    text-align:
        center;

    color:
        #777777;

    font-size:
        11px;

}


.card-arrow {

    position:
        absolute;

    left:
        41%;

    top:
        50%;

    transform:
        translate(-50%,-50%);

    font-size:
        22px;

    color:
        #555555;

    animation:
        slideArrow 1s ease-in-out infinite;

}


@keyframes slideArrow {

    0%,
    100% {

        opacity:
            0.25;

        transform:
            translate(-70%,-50%);

    }

    50% {

        opacity:
            1;

        transform:
            translate(-30%,-50%);

    }

}


/* =====================================================
   PAUSE
   ===================================================== */

.pause-overlay {

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

}


.pause-title {

    font-size:
        28px;

    text-align:
        center;

    margin-bottom:
        14px;

}


.pause-sub {

    color:
        #777777;

    font-size:
        13px;

    text-align:
        center;

}


.pause-actions {

    visibility: hidden;
    pointer-events: none;

    margin-top:
        24px;

    display:
        flex;

    flex-direction:
        column;

    gap:
        8px;

    align-items:
        center;

}



/* Reference-matched stage and item-acquired overlays */
.tutorial-transition{position:fixed;inset:0;z-index:1000000;display:none;align-items:center;justify-content:center;background:#000;opacity:1;transition:opacity .45s steps(6,end);pointer-events:auto}
.tutorial-transition.show{display:flex}.tutorial-transition.hide{opacity:0;pointer-events:none}
.tutorial-transition-card{position:relative;width:min(350px,78vw);min-height:145px;display:flex;flex-direction:column;align-items:center;justify-content:center;border:1px solid #57dfff;color:#f5fbff;box-shadow:0 0 0 1px #143d4c,0 0 14px #00cfff22;letter-spacing:2px}
.tutorial-transition-card:before,.tutorial-transition-card:after{content:'';position:absolute;width:18px;height:18px;border-color:#78ecff;border-style:solid}
.tutorial-transition-card:before{top:-2px;left:-2px;border-width:2px 0 0 2px}.tutorial-transition-card:after{right:-2px;bottom:-2px;border-width:0 2px 2px 0}
.tutorial-transition-stage{font-size:clamp(25px,4vw,36px);line-height:1.6;text-shadow:0 0 5px #fff}.tutorial-transition-room{font-size:clamp(14px,2vw,20px);color:#a8f2ff;letter-spacing:1px}
.item-acquired-notice{position:fixed;left:50%;bottom:5%;transform:translateX(-50%);z-index:500;display:none;grid-template-columns:minmax(120px,.78fr) minmax(240px,1.45fr);gap:14px;width:min(720px,92vw);padding:14px;background:#02070c;border:1px solid #48dfff;box-shadow:0 0 0 1px #123c4d,0 0 16px #00cfff22;cursor:pointer}
.item-acquired-notice.show{display:grid}.item-acquired-art{display:flex;align-items:center;justify-content:center;min-height:120px;position:relative}
.item-acquired-art .pixel-card-item{width:94px;height:62px;transform:rotate(-10deg) scale(1.05);margin:0;box-shadow:3px 0 #bafaff,-3px 0 #bafaff,0 3px #bafaff,0 -3px #bafaff,0 0 16px #00dfff88}
.item-acquired-dialog{border:1px solid #2587a7;padding:12px 14px;min-height:120px;position:relative}.item-acquired-tag{display:inline-block;background:#087aa1;color:#e8fbff;padding:4px 10px;font-size:12px;margin-bottom:10px}
.item-acquired-text{font-size:clamp(12px,1.5vw,16px);line-height:1.8;color:#d9faff;white-space:pre-line}.item-acquired-close{position:absolute;right:10px;bottom:8px;color:#54dfff;font-size:9px}
@media(max-width:560px){.item-acquired-notice{grid-template-columns:88px minmax(0,1fr);gap:8px;padding:9px}.item-acquired-art{min-height:105px}.item-acquired-art .pixel-card-item{width:60px;height:40px}.item-acquired-dialog{padding:9px;min-height:105px}.item-acquired-text{font-size:11px}}


.pause-overlay{background:rgba(0,0,0,.72)}
.pause-overlay>div{width:min(320px,82vw);padding:20px 22px;background:#02070c;border:1px solid #54dfff;box-shadow:0 0 0 1px #123c4d,0 0 18px #00cfff22}
.pause-title,.pause-sub{display:none}
.pause-actions{visibility:visible;pointer-events:auto;margin:0;display:flex;flex-direction:column;gap:9px;align-items:stretch}
.pause-actions .pause-row{display:flex;align-items:center;gap:12px;width:100%}
.pause-actions .pause-icon{width:22px;height:22px;flex:0 0 22px;display:inline-flex;align-items:center;justify-content:center;border:1px solid #58dfff;border-radius:50%;color:#82eaff;font-size:10px}
.pause-actions .pause-nav-link,.pause-actions .pause-menu-button{flex:1;display:flex;align-items:center;min-height:24px;padding:2px 0;border:0!important;background:transparent!important;color:#d8faff!important;font-size:14px;text-decoration:none;text-align:left;cursor:pointer}
.pause-actions .pause-nav-link:hover,.pause-actions .pause-menu-button:hover{color:#fff!important;text-shadow:0 0 6px #54dfff}

/* =====================================================
   MOBILE CONTROLS
   ===================================================== */

.mobile-controls {

    display:
        none;

    position:
        absolute;

    right:
        18px;

    bottom:
        18px;

    width:
        138px;

    height:
        138px;

    z-index:
        150;

    pointer-events:
        none;

}


.control-button {

    position:
        absolute;

    width:
        44px;

    height:
        44px;

    padding:
        0;

    border:
        1px solid #777777;

    background:
        rgba(0,0,0,0.92);

    color:
        #ffffff;

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

    pointer-events:
        auto;

    -webkit-tap-highlight-color:
        transparent;

}


.control-button:active {

    background:
        #ffffff;

    color:
        #000000;

}


.control-up {

    top:
        0;

    left:
        47px;

}


.control-left {

    top:
        47px;

    left:
        0;

}


.control-right {

    top:
        47px;

    right:
        0;

}


.control-down {

    bottom:
        0;

    left:
        47px;

}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width:700px) {

    .project-title {

        top:
            16px;

        left:
            16px;

        font-size:
            14px;

    }


    .stage-title {

        top:
            38px;

        left:
            16px;

        font-size:
            10px;

    }


    .game-area {

        top:
            66px;

        left:
            10px;

        right:
            10px;

        bottom:
            55px;

        background-size:
            30px 30px;

    }


    .status {

        left:
            12px;

        bottom:
            14px;

        font-size:
            10px;

    }


    .echo-bar {

        width:
            92%;

        bottom:
            2%;

        min-height:
            82px;

        padding:
            11px 13px 20px;

    }


    .echo-message {

        font-size:
            11px;

    }


    .interaction-message {

        bottom:
            22%;

        font-size:
            10px;

    }


    .mobile-controls {

        display:
            block;

    }


    .computer-panel {

        padding:
            20px;

    }


    .access-number {

        font-size:
            27px;

    }


    .card-stage {

        height:
            220px;

    }


    .exit-sign {

        right:
            10%;

        font-size:
            9px;

    }

}

</style>

</head>


<body>


<div
    class="game"
    id="gameRoot"
    tabindex="0"
>


<div class="project-title">
    PROJECT : LOGIC
</div>


<div class="stage-title">
    STAGE 00 // TUTORIAL
</div>


<div class="game-area">


<!-- =====================================================
     MOBILE CONTROLS
     ===================================================== -->

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


<!-- =====================================================
     ROOM
     ===================================================== -->

<div class="room">


<div class="room-line-horizontal"></div>

<div class="room-line-vertical"></div>


<!-- MONITOR -->

<div
    class="object monitor"
    id="monitor"
>
</div>


<!-- COMPUTER -->

<div
    class="object computer"
    id="computer"
>

    COMPUTER

    <div class="object-label">
        ECHO TERMINAL
    </div>

</div>


<!-- DESK -->

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


<!-- EXIT -->

<div
    class="exit-wall"
    id="exitDoor"
>
</div>


<div class="exit-sign">

    <span class="exit-arrow">
        ↓ ↑
    </span>

    <br>

    <span>
        [EXIT] SECURITY ROOM
    </span>

</div>


<!-- PLAYER -->

<div
    class="player"
    id="player"
></div>


<!-- INTERACTION -->

<div
    class="interaction-message"
    id="interactionMessage"
>
    PRESS E
</div>


<!-- ECHO -->

<div class="echo-bar">

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
        SPACE // SKIP / NEXT
    </div>

</div>


</div>


<!-- =====================================================
     INVENTORY
     ===================================================== -->

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

<div class="inventory-slot" data-slot="8"></div>
<div class="inventory-slot" data-slot="9"></div>
<div class="inventory-slot" data-slot="10"></div>
<div class="inventory-slot" data-slot="11"></div>

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


<!-- =====================================================
     HELP
     ===================================================== -->

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
        가까운 물체를 조사하거나 아이템을 획득합니다.
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
        ECHO의 채팅을 끝까지 표시하거나 다음 채팅으로 넘어갑니다.
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

        시설 내부의 물체와 기록을 자세히 조사하세요.<br>

        ECHO가 제공하는 모든 정보가 사실이라고 가정해서는 안 됩니다.<br>

        서로 모순되는 단서가 발견될 수도 있습니다.

    </div>

</div>


</div>

</div>


<!-- =====================================================
     COMPUTER
     ===================================================== -->

<div
    class="computer-overlay"
    id="computerOverlay"
>

<div class="computer-panel">


<div class="computer-title">
    ECHO TERMINAL
</div>


<div class="computer-sub">
    ACCESS SEQUENCE // ECHO GENERATED
</div>


<div class="access-sequence">

    ACCESS SEQUENCE

    <div
        class="access-number"
        id="accessNumber"
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


<!-- =====================================================
     CARD ACCESS
     ===================================================== -->

<div
    class="card-overlay"
    id="cardOverlay"
>

<div class="card-panel">


<div class="card-header">

    <div class="card-title">
        SECURITY ROOM // ACCESS
    </div>

    <div class="card-help">
        DRAG CARD TO READER
    </div>

</div>


<div
    class="card-stage"
    id="cardStage"
>


<div class="reader" id="cardReader">

    <div class="reader-light" id="readerLight"></div>
    <div class="reader-slot"></div>

    CARD READER

</div>


<div class="card-arrow">
    →
</div>


<div
    class="card"
    id="dragCard"
>

    <div class="card-chip"></div>

    ACCESS KEY

    <br>

    <span style="color:#666">
        SECURITY AUTHORIZATION
    </span>

</div>


</div>


<div
    class="card-status"
    id="cardStatus"
>
    카드를 리더기까지 끌어다 놓으십시오.
</div>


</div>

</div>


<!-- =====================================================
     PAUSE
     ===================================================== -->

<div class="item-acquired-notice" id="itemAcquiredNotice" role="button" tabindex="0" aria-label="아이템 획득 알림을 닫으려면 클릭"><div class="item-acquired-art"><div class="pixel-card-item"><span class="pixel-card-chip"></span><span class="pixel-card-mark">A</span><span class="pixel-card-lines"></span></div></div><div class="item-acquired-dialog"><div class="item-acquired-tag">ECHO</div><div class="item-acquired-text">카드가 인벤토리에 추가되었습니다.
이 카드는 특정 장비를 작동시키거나 인증할 때 사용됩니다.</div><div class="item-acquired-close">CLICK TO CLOSE</div></div></div>
<div class="tutorial-transition" id="tutorialTransition" aria-hidden="true"><div class="tutorial-transition-card"><div class="tutorial-transition-stage">STAGE 00</div><div class="tutorial-transition-room">:TUTORIAL</div></div></div>
<div class="pause-overlay" id="pauseOverlay"><div class="pause-menu-panel"><div class="pause-actions"><div class="pause-row"><span class="pause-icon">Ⅱ</span><a class="pause-nav-link" id="resumeButton" href="?action=resume" target="_top" rel="noopener">RESUME</a></div><div class="pause-row"><span class="pause-icon">↻</span><a class="pause-nav-link" id="restartButton" href="?action=restart" target="_top" rel="noopener">RESTART</a></div><div class="pause-row"><span class="pause-icon">⌂</span><a class="pause-nav-link" id="titleButton" href="?action=title" target="_top" rel="noopener">TITLE</a></div></div></div></div>

<div
    class="status"
    id="status"
>
    ECHO SYSTEM // ONLINE
</div>


</div>

<div class="fade-screen" id="fadeScreen" aria-hidden="true"><div class="fade-message" id="fadeMessage"><span class="fade-stage">STAGE 01</span><span class="fade-room">:ARCHIVE ACCESS</span></div></div>

<script>

(function () {

"use strict";


/* =====================================================
   GAME STATE
   ===================================================== */

const paused =
    __PAUSED__;


/*
 * 방이 시작될 때마다 새로운 4자리 암호 생성
 */

let ACCESS_CODE =
    String(
        Math.floor(
            1000 +
            Math.random() * 9000
        )
    );


let tutorialStep =
    0;


let inventoryOpen =
    false;


let helpOpen =
    false;


let computerOpen =
    false;


let cardOpen =
    false;


let keyCollected =
    false;

let cardConsumed = false;


let echoIndex =
    0;


let typingTimer =
    null;


let typingDone =
    false;


let cardDragging =
    false;


let cardOffsetX =
    0;


let cardOffsetY =
    0;


/* =====================================================
   ELEMENTS
   ===================================================== */

const root =
    document.getElementById(
        "gameRoot"
    );


const room =
    document.querySelector(
        ".room"
    );


const player =
    document.getElementById(
        "player"
    );


const echoMessage =
    document.getElementById(
        "echoMessage"
    );


const echoNext =
    document.getElementById(
        "echoNext"
    );


const interactionMessage =
    document.getElementById(
        "interactionMessage"
    );


const status =
    document.getElementById(
        "status"
    );


const accessKey =
    document.getElementById(
        "accessKey"
    );


const computerOverlay =
    document.getElementById(
        "computerOverlay"
    );


const accessNumber =
    document.getElementById(
        "accessNumber"
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


const inventoryOverlay =
    document.getElementById(
        "inventoryOverlay"
    );


const helpOverlay =
    document.getElementById(
        "helpOverlay"
    );


const cardOverlay =
    document.getElementById(
        "cardOverlay"
    );


const cardStage =
    document.getElementById(
        "cardStage"
    );


const dragCard =
    document.getElementById(
        "dragCard"
    );


const cardStatus =
    document.getElementById(
        "cardStatus"
    );

const readerLight = document.getElementById("readerLight");
const fadeScreen = document.getElementById("fadeScreen");


const pauseOverlay =
    document.getElementById(
        "pauseOverlay"
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


const playerRadius =
    1.3;


const moveSpeed =
    0.55;


const keys = {

    w: false,
    a: false,
    s: false,
    d: false

};


function clearKeys() {

    keys.w = false;

    keys.a = false;

    keys.s = false;

    keys.d = false;

}


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


function renderInventory() {

    inventory.forEach(
        function (item, index) {

            const slot =
                inventorySlots[index];


            if (item) {

                slot.innerHTML =
                    `
                    <div class="slot-number">${String(index + 1).padStart(2, "0")}</div>
                    ${item.name === "ACCESS KEY" ? '<div class="pixel-card-item"><span class="pixel-card-chip"></span><span class="pixel-card-mark">A</span><span class="pixel-card-lines"></span></div>' : ''}
                    <div class="item-name">${item.name}</div>
                    `;

            }

            else {

                slot.innerHTML =
                    `
                    <div class="slot-number">
                        ${String(index + 1).padStart(2, "0")}
                    </div>

                    <div class="empty-text">
                        EMPTY
                    </div>
                    `;

            }

        }
    );

}


renderInventory();


/* =====================================================
   ECHO CHAT
   ===================================================== */

const messages = [

    "연결이 확인되었습니다. 저는 ECHO입니다. 이 시설에서의 첫 번째 절차를 안내하겠습니다.",

    "먼저 이동 방법을 익혀야 합니다. W A S D 키를 사용하여 시설 내부를 이동해 보세요. 중앙의 COMPUTER로 이동하십시오.",

    "좋습니다. COMPUTER에 접근했습니다. 가까운 물체에서는 E 키를 사용하여 상호작용할 수 있습니다. COMPUTER를 조사하십시오.",

    "확인되었습니다. 이제 COMPUTER 화면에 표시된 접근 코드를 입력하십시오.",

    "코드가 확인되었습니다. 책상 위에 ACCESS KEY가 생성되었습니다. 책상으로 이동하여 키를 획득하십시오.",

    "ACCESS KEY를 획득했습니다. 이제 EXIT SECURITY ROOM으로 이동하십시오. 출구에서 E를 누르면 보안 인증이 시작됩니다."

];


function typeEcho(index) {

    echoIndex =
        index;


    clearTimeout(
        typingTimer
    );


    const text =
        messages[index] || "";


    echoMessage.textContent =
        "";


    typingDone =
        false;


    echoNext.classList.remove(
        "ready"
    );


    let i =
        0;


    function tick() {

        if (i < text.length) {

            echoMessage.textContent +=
                text[i];

            i += 1;


            typingTimer =
                setTimeout(
                    tick,
                    25
                );

        }

        else {

            typingDone =
                true;

            echoNext.classList.add(
                "ready"
            );
            saveTutorialState();

        }

    }


    tick();

}


/*
 * SPACE
 *
 * 1회:
 * 타이핑 중이면 전체 문장 표시
 *
 * 2회:
 * 다음 채팅
 */

function nextEcho() {
    // 첫 SPACE는 타이핑을 완료하고, 두 번째 SPACE는 첫 이동 안내를 연다.
    if (!typingDone) {
        clearTimeout(typingTimer);
        echoMessage.textContent = messages[echoIndex] || "";
        typingDone = true;
        echoNext.classList.add("ready");
        saveTutorialState();
        return;
    }

    if (echoIndex === 0 && tutorialStep === 0) {
        typeEcho(1);
        status.textContent = "TUTORIAL // W A S D TO MOVE";
        saveTutorialState();
        return;
    }

    // 이후 대사는 이동·조사 등 실제 행동을 완료했을 때만 바뀐다.
    status.textContent = "ECHO SYSTEM // 안내된 행동을 먼저 완료하십시오.";
    saveTutorialState();
}

const TUTORIAL_SAVE_KEY = "project_logic_tutorial_save_v3";
if (__RESET_TUTORIAL_SAVE__) { try { localStorage.removeItem(TUTORIAL_SAVE_KEY); } catch (e) {} }
function saveTutorialState() {
    try {
        localStorage.setItem(TUTORIAL_SAVE_KEY, JSON.stringify({
            tutorialStep, echoIndex, echoText: echoMessage.textContent,
            typingDone, playerX, playerY, keyCollected, cardConsumed,
            accessCode: ACCESS_CODE, inventory: Array.from(inventorySlots).map(el => el.classList.contains("has-item"))
        }));
    } catch (e) {}
}
function restoreTutorialState() {
    try {
        const saved = JSON.parse(localStorage.getItem(TUTORIAL_SAVE_KEY) || "null");
        if (!saved) return false;
        if (Number.isFinite(saved.tutorialStep)) tutorialStep = saved.tutorialStep;
        if (Number.isFinite(saved.echoIndex)) echoIndex = Math.max(0, Math.min(messages.length - 1, saved.echoIndex));
        if (Number.isFinite(saved.playerX)) playerX = saved.playerX;
        if (Number.isFinite(saved.playerY)) playerY = saved.playerY;
        keyCollected = !!saved.keyCollected;
        cardConsumed = !!saved.cardConsumed;
        if (typeof saved.accessCode === "string" && /^\d{4}$/.test(saved.accessCode)) ACCESS_CODE = saved.accessCode;
        player.style.left = playerX + "%";
        player.style.top = playerY + "%";
        echoMessage.textContent = typeof saved.echoText === "string" ? saved.echoText : (messages[echoIndex] || "");
        typingDone = true; // iframe 재생성 후에는 현재 문장을 보존하고 타이핑 완료 상태로 복구
        echoNext.classList.add("ready");
        return true;
    } catch (e) { return false; }
}

const tutorialWasRestored = restoreTutorialState();
const tutorialTransition = document.getElementById("tutorialTransition");
if (!tutorialWasRestored && tutorialTransition) {
    tutorialTransition.classList.add("show");
    window.setTimeout(() => tutorialTransition.classList.add("hide"), 2550);
    window.setTimeout(() => tutorialTransition.remove(), 3050);
}
if (!tutorialWasRestored) typeEcho(0);
setInterval(saveTutorialState, 250);
window.addEventListener("beforeunload", saveTutorialState);


/* =====================================================
   OBJECTS
   ===================================================== */

const obstacles = [

    {
        id: "monitor",
        x: 43.5,
        y: 9,
        w: 13,
        h: 7
    },

    {
        id: "computer",
        x: 42,
        y: 13,
        w: 16,
        h: 14
    },

    {
        id: "desk",
        x: 35,
        y: 62,
        w: 30,
        h: 12
    },

    {
        id: "exit",
        x: 92,
        y: 35,
        w: 8,
        h: 30
    }

];


const interactables = [

    {
        id: "computer",
        name: "ECHO TERMINAL",
        x: 42,
        y: 13,
        w: 16,
        h: 14
    },

    {
        id: "desk",
        name: "RESEARCH DESK",
        x: 35,
        y: 62,
        w: 30,
        h: 12
    },

    {
        id: "exit",
        name: "SECURITY ROOM",
        x: 92,
        y: 35,
        w: 8,
        h: 30
    }

];


let nearby =
    null;


/* =====================================================
   COLLISION
   ===================================================== */

function circleHitsRect(
    cx,
    cy,
    radius,
    object
) {

    const roomWidth =
        room.clientWidth;


    const roomHeight =
        room.clientHeight;


    const left =
        object.x / 100 *
        roomWidth;


    const top =
        object.y / 100 *
        roomHeight;


    const right =
        (object.x + object.w) /
        100 *
        roomWidth;


    const bottom =
        (object.y + object.h) /
        100 *
        roomHeight;


    const px =
        cx / 100 *
        roomWidth;


    const py =
        cy / 100 *
        roomHeight;


    const closestX =
        Math.max(
            left,
            Math.min(
                px,
                right
            )
        );


    const closestY =
        Math.max(
            top,
            Math.min(
                py,
                bottom
            )
        );


    const dx =
        px -
        closestX;


    const dy =
        py -
        closestY;


    const actualRadius =
        radius / 100 *
        roomWidth;


    return (
        dx * dx +
        dy * dy
    ) <
    (
        actualRadius *
        actualRadius
    );

}


function blocked(
    x,
    y
) {

    if (
        x < 3 ||
        x > 97 ||
        y < 3 ||
        y > 97
    ) {

        return true;

    }


    return obstacles.some(
        function (object) {

            return circleHitsRect(
                x,
                y,
                playerRadius,
                object
            );

        }
    );

}


/* =====================================================
   DISTANCE
   ===================================================== */

function distanceToObject(
    object
) {

    const centerX =
        object.x +
        object.w / 2;


    const centerY =
        object.y +
        object.h / 2;


    return Math.hypot(
        playerX - centerX,
        playerY - centerY
    );

}


/* =====================================================
   INTERACTION CHECK
   ===================================================== */

function checkInteraction() {

    nearby =
        null;


    let closest =
        Infinity;


    interactables.forEach(
        function (object) {

            const distance =
                distanceToObject(
                    object
                );


            if (
                distance < 12 &&
                distance < closest
            ) {

                nearby =
                    object;


                closest =
                    distance;

            }

        }
    );


    if (
        nearby &&
        !computerOpen &&
        !inventoryOpen &&
        !helpOpen &&
        !cardOpen
    ) {

        interactionMessage.textContent =
            "E  //  " +
            nearby.name;


        interactionMessage.classList.add(
            "visible"
        );

    }

    else {

        interactionMessage.classList.remove(
            "visible"
        );

    }

}


/* =====================================================
   INACCESSIBLE
   ===================================================== */

function inaccessible() {

    status.textContent =
        "SYSTEM // 접근할 수 없는 과정입니다.";

}


/* =====================================================
   MOVEMENT
   ===================================================== */

function updateMovement() {

    if (
        paused ||
        inventoryOpen ||
        helpOpen ||
        computerOpen ||
        cardOpen
    ) {

        return;

    }


    let dx =
        0;


    let dy =
        0;


    if (keys.w) {

        dy -= 1;

    }


    if (keys.s) {

        dy += 1;

    }


    if (keys.a) {

        dx -= 1;

    }


    if (keys.d) {

        dx += 1;

    }


    if (
        dx === 0 &&
        dy === 0
    ) {

        return;

    }


    const length =
        Math.hypot(
            dx,
            dy
        );


    dx =
        dx /
        length *
        moveSpeed;


    dy =
        dy /
        length *
        moveSpeed;


    /*
     * X/Y를 따로 검사해서
     * 벽이나 물체에 비스듬히 끼지 않도록 함
     */

    if (
        !blocked(
            playerX + dx,
            playerY
        )
    ) {

        playerX +=
            dx;

    }


    if (
        !blocked(
            playerX,
            playerY + dy
        )
    ) {

        playerY +=
            dy;

    }


    player.style.left =
        playerX + "%";


    player.style.top =
        playerY + "%";


    /*
     * 첫 이동
     */

    if (
        tutorialStep === 0
    ) {

        tutorialStep =
            1;


        typeEcho(1);


        status.textContent =
            "TUTORIAL // MOVEMENT ENABLED";

    }


    checkInteraction();

}


/* =====================================================
   COMPUTER
   ===================================================== */

function openComputer() {

    if (
        tutorialStep !== 2
    ) {

        inaccessible();

        return;

    }


    computerOpen =
        true;


    clearKeys();


    interactionMessage.classList.remove(
        "visible"
    );


    accessNumber.textContent =
        ACCESS_CODE;


    computerOverlay.style.display =
        "flex";


    codeInput.value =
        "";


    codeError.textContent =
        "";


    setTimeout(
        function () {

            codeInput.focus();

        },
        50
    );

}


function closeComputer() {

    computerOpen =
        false;


    computerOverlay.style.display =
        "none";


    codeInput.blur();


    root.focus();

}


/* =====================================================
   CODE
   ===================================================== */

function submitCode() {

    const entered =
        codeInput.value.trim();


    if (
        entered ===
        ACCESS_CODE
    ) {

        closeComputer();


        /*
         * 암호 입력 성공 즉시
         * 책상 위에 ACCESS KEY 생성
         */

        accessKey.classList.add(
            "visible"
        );


        tutorialStep =
            3;


        typeEcho(4);


        status.textContent =
            "ECHO TERMINAL // CODE VERIFIED // ACCESS KEY GENERATED";

    }

    else {

        codeError.textContent =
            "ACCESS DENIED // 화면의 4자리 숫자를 입력하십시오.";

    }

}


codeButton.addEventListener(
    "click",
    submitCode
);


codeInput.addEventListener(
    "input",
    function () {

        codeInput.value =
            codeInput.value
                .replace(
                    /\D/g,
                    ""
                )
                .slice(
                    0,
                    4
                );

    }
);


codeInput.addEventListener(
    "keydown",
    function (event) {

        if (
            event.key ===
            "Enter"
        ) {

            event.preventDefault();

            submitCode();

        }


        if (
            event.key ===
            "Escape"
        ) {

            event.preventDefault();

            closeComputer();

        }

    }
);


/* =====================================================
   INTERACTION
   ===================================================== */

function interact() {

    if (
        paused ||
        computerOpen ||
        inventoryOpen ||
        helpOpen ||
        cardOpen
    ) {

        return;

    }


    if (!nearby) {

        return;

    }


    /*
     * 이동 전
     */

    if (
        tutorialStep === 0
    ) {

        inaccessible();

        return;

    }


    /*
     * COMPUTER
     */

    if (
        tutorialStep === 1
    ) {

        if (
            nearby.id !==
            "computer"
        ) {

            inaccessible();

            return;

        }


        tutorialStep =
            2;


        typeEcho(3);


        status.textContent =
            "ECHO SYSTEM // TERMINAL CONNECTED";


        openComputer();


        return;

    }


    /*
     * COMPUTER CODE 단계
     */

    if (
        tutorialStep === 2
    ) {

        if (
            nearby.id !==
            "computer"
        ) {

            inaccessible();

            return;

        }


        openComputer();

        return;

    }


    /*
     * ACCESS KEY
     */

    if (
        tutorialStep === 3
    ) {

        if (
            nearby.id !==
            "desk"
        ) {

            inaccessible();

            return;

        }


        if (
            !accessKey.classList.contains(
                "visible"
            )
        ) {

            inaccessible();

            return;

        }


        accessKey.classList.remove(
            "visible"
        );


        inventory[0] = {

            name:
                "ACCESS KEY",

            description:
                "ECHO TERMINAL에서 인증된 보안구역 접근 키입니다."

        };


        keyCollected =
            true;


        tutorialStep =
            5;


        renderInventory();
        const itemNotice = document.getElementById("itemAcquiredNotice");
        if (itemNotice) {
            itemNotice.classList.add("show");
            const dismissItemNotice = () => itemNotice.classList.remove("show");
            itemNotice.onclick = dismissItemNotice;
            itemNotice.onkeydown = (event) => { if (event.key === "Enter" || event.key === " ") dismissItemNotice(); };
            window.setTimeout(dismissItemNotice, 6500);
        }


        typeEcho(5);


        status.textContent =
            "SYSTEM // ACCESS KEY ACQUIRED";


        return;

    }


    /*
     * EXIT
     */

    if (
        tutorialStep === 5
    ) {

        if (
            nearby.id !==
            "exit"
        ) {

            inaccessible();

            return;

        }


        if (
            !keyCollected
        ) {

            inaccessible();

            return;

        }


        openCardAccess();

    }

}


/* =====================================================
   INVENTORY
   ===================================================== */

function openInventory() {

    if (
        paused ||
        computerOpen ||
        cardOpen
    ) {

        return;

    }


    helpOpen =
        false;


    helpOverlay.style.display =
        "none";


    inventoryOpen =
        true;


    inventoryOverlay.style.display =
        "flex";


    clearKeys();


    renderInventory();

}


function closeInventory() {

    inventoryOpen =
        false;


    inventoryOverlay.style.display =
        "none";


    root.focus();

}


inventorySlots.forEach(
    function (slot) {

        slot.addEventListener(
            "click",
            function () {

                inventorySlots.forEach(
                    function (other) {

                        other.classList.remove(
                            "selected"
                        );

                    }
                );


                slot.classList.add(
                    "selected"
                );


                const item =
                    inventory[
                        Number(
                            slot.dataset.slot
                        )
                    ];


                if (item) {

                    itemDescription.innerHTML =
                        item.name +
                        "<br><br>" +
                        item.description;

                }

                else {

                    itemDescription.innerHTML =
                        "ITEM DESCRIPTION<br><br>비어 있는 슬롯입니다.";

                }

            }
        );

    }
);


/* =====================================================
   HELP
   ===================================================== */

function openHelp() {

    if (
        paused ||
        computerOpen ||
        cardOpen
    ) {

        return;

    }


    inventoryOpen =
        false;


    inventoryOverlay.style.display =
        "none";


    helpOpen =
        true;


    helpOverlay.style.display =
        "flex";


    clearKeys();

}


function closeHelp() {

    helpOpen =
        false;


    helpOverlay.style.display =
        "none";


    root.focus();

}


/* =====================================================
   KEYBOARD
   ===================================================== */

document.addEventListener(
    "keydown",
    function (event) {

        /*
         * 암호 입력 중
         */

        if (
            document.activeElement ===
            codeInput
        ) {

            return;

        }


        /*
         * SPACE
         */

        if (
            event.code ===
            "Space"
        ) {

            event.preventDefault();


            if (
                !paused &&
                !computerOpen &&
                !cardOpen &&
                !inventoryOpen &&
                !helpOpen
            ) {

                nextEcho();

            }


            return;

        }


        const key =
            event.key.toLowerCase();


        /*
         * ESC
         */

        if (
            key ===
            "escape"
        ) {

            if (
                computerOpen
            ) {

                closeComputer();

                return;

            }


            if (
                cardOpen
            ) {

                closeCardAccess();

                return;

            }


            if (
                helpOpen
            ) {

                closeHelp();

                return;

            }


            if (
                inventoryOpen
            ) {

                closeInventory();

                return;

            }

        }


        /*
         * E
         */

        if (
            key ===
            "e"
        ) {

            event.preventDefault();

            interact();

            return;

        }


        /*
         * H
         */

        if (
            key ===
            "h"
        ) {

            event.preventDefault();


            if (helpOpen) {

                closeHelp();

            }

            else {

                openHelp();

            }


            return;

        }


        /*
         * I
         */

        if (
            key ===
            "i"
        ) {

            event.preventDefault();


            if (inventoryOpen) {

                closeInventory();

            }

            else {

                openInventory();

            }


            return;

        }


        /*
         * WASD
         */

        if (
            key === "w" ||
            key === "a" ||
            key === "s" ||
            key === "d"
        ) {

            if (
                !paused &&
                !computerOpen &&
                !cardOpen &&
                !helpOpen &&
                !inventoryOpen
            ) {

                keys[key] =
                    true;

                event.preventDefault();

            }

        }

    }
);


/* =====================================================
   KEYBOARD RELEASE
   ===================================================== */

document.addEventListener(
    "keyup",
    function (event) {

        const key =
            event.key.toLowerCase();


        if (
            key === "w" ||
            key === "a" ||
            key === "s" ||
            key === "d"
        ) {

            keys[key] =
                false;


            event.preventDefault();

        }

    }
);


/* =====================================================
   MOBILE CONTROLS
   ===================================================== */

document
    .querySelectorAll(
        ".control-button"
    )
    .forEach(
        function (button) {

            const direction =
                button.dataset.direction;


            function press(
                event
            ) {

                event.preventDefault();


                if (
                    !paused &&
                    !computerOpen &&
                    !cardOpen &&
                    !helpOpen &&
                    !inventoryOpen
                ) {

                    keys[direction] =
                        true;


                    try {

                        button.setPointerCapture(
                            event.pointerId
                        );

                    }

                    catch (error) {}

                }

            }


            function release(
                event
            ) {

                event.preventDefault();

                keys[direction] =
                    false;

            }


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
                "lostpointercapture",
                release
            );

        }
    );


/* =====================================================
   CARD ACCESS
   ===================================================== */

function openCardAccess() {

    if (
        !keyCollected || cardConsumed
    ) {

        inaccessible();

        return;

    }


    cardOpen =
        true;


    clearKeys();


    interactionMessage.classList.remove(
        "visible"
    );


    cardOverlay.style.display =
        "flex";


    resetCard();

}


function closeCardAccess() {

    cardOpen =
        false;


    cardOverlay.style.display =
        "none";


    resetCard();


    root.focus();

}


function resetCard() {

    dragCard.style.left =
        "12%";


    dragCard.style.top =
        "50%";


    dragCard.style.transform =
        "translateY(-50%)";


    cardDragging =
        false;


    cardStatus.textContent =
        "카드를 리더기까지 끌어다 놓으십시오.";

}


function getCardStagePoint(
    event
) {

    const rect =
        cardStage.getBoundingClientRect();


    return {

        x:
            event.clientX -
            rect.left,

        y:
            event.clientY -
            rect.top

    };

}


function startCardDrag(
    event
) {

    if (
        !cardOpen
    ) {

        return;

    }


    event.preventDefault();


    const rect =
        dragCard.getBoundingClientRect();


    cardOffsetX =
        event.clientX -
        rect.left;


    cardOffsetY =
        event.clientY -
        rect.top;


    cardDragging =
        true;


    try {

        dragCard.setPointerCapture(
            event.pointerId
        );

    }

    catch (error) {}

}


function dragCardMove(
    event
) {

    if (
        !cardDragging
    ) {

        return;

    }


    event.preventDefault();


    const point =
        getCardStagePoint(
            event
        );


    const stage =
        cardStage.getBoundingClientRect();


    let x =
        point.x -
        cardOffsetX;


    let y =
        point.y -
        cardOffsetY;


    x =
        Math.max(
            0,
            Math.min(
                stage.width -
                dragCard.offsetWidth,
                x
            )
        );


    y =
        Math.max(
            0,
            Math.min(
                stage.height -
                dragCard.offsetHeight,
                y
            )
        );


    dragCard.style.left =
        x + "px";


    dragCard.style.top =
        y + "px";


    dragCard.style.transform =
        "none";

}


function finishCardDrag(
    event
) {

    if (
        !cardDragging
    ) {

        return;

    }


    cardDragging =
        false;


    const cardRect =
        dragCard.getBoundingClientRect();


    const reader =
        document.querySelector(
            ".reader"
        );


    const readerRect =
        reader.getBoundingClientRect();


    const correctPosition =
        cardRect.right >
        readerRect.left + 25 &&

        cardRect.left <
        readerRect.right - 25 &&

        cardRect.bottom >
        readerRect.top + 18 &&

        cardRect.top <
        readerRect.bottom - 18;


    if (
        correctPosition
    ) {

        dragCard.style.left =
            "72%";


        dragCard.style.top =
            "50%";


        cardStatus.textContent =
            "SECURITY ACCESS // VERIFIED";

        status.textContent =
            "SECURITY ROOM // ACCESS GRANTED";

        // 카드키는 일회용: 인벤토리에서 제거하고 리더기를 녹색으로 변경한다.
        inventory[0] = null;
        keyCollected = false;
        cardConsumed = true;
        renderInventory();
        if (readerLight) readerLight.classList.add("green");
        cardStatus.textContent = "ACCESS GRANTED // CARD CONSUMED";

        // 짧은 문 개방 효과음(Web Audio, 별도 파일 불필요)
        try {
            const AudioContextClass = window.AudioContext || window.webkitAudioContext;
            if (AudioContextClass) {
                const audio = new AudioContextClass();
                const now = audio.currentTime;
                [440, 660, 880].forEach((frequency, index) => {
                    const oscillator = audio.createOscillator();
                    const gain = audio.createGain();
                    oscillator.type = "square";
                    oscillator.frequency.value = frequency;
                    gain.gain.setValueAtTime(0.0001, now + index * 0.12);
                    gain.gain.exponentialRampToValueAtTime(0.08, now + index * 0.12 + 0.02);
                    gain.gain.exponentialRampToValueAtTime(0.0001, now + index * 0.12 + 0.18);
                    oscillator.connect(gain);
                    gain.connect(audio.destination);
                    oscillator.start(now + index * 0.12);
                    oscillator.stop(now + index * 0.12 + 0.2);
                });
                setTimeout(() => audio.close(), 900);
            }
        } catch (error) {}

        setTimeout(function () {
            closeCardAccess();
            clearTimeout(typingTimer);
            echoMessage.textContent = "이제 다음 스테이지로 넘어가도록 합시다.";
            typingDone = true;
            echoNext.classList.add("ready");
            setTimeout(function () {
                const fadeMessage = document.getElementById("fadeMessage");
                if (fadeMessage) fadeMessage.innerHTML = '<span class="fade-stage">STAGE 01</span><span class="fade-room">:ARCHIVE ACCESS</span>';
                if (fadeScreen) fadeScreen.classList.add("active");
                // Leave the black screen and flickering stage sign visible for 3 seconds.
                setTimeout(function () { parentAction("stage01"); }, 3000);
            }, 1000);
        }, 700);

    }

    else {

        cardStatus.textContent =
            "CARD NOT DETECTED // READER에 정확히 맞춰주세요.";

    }

}


dragCard.addEventListener(
    "pointerdown",
    startCardDrag
);


dragCard.addEventListener(
    "pointermove",
    dragCardMove
);


dragCard.addEventListener(
    "pointerup",
    finishCardDrag
);


dragCard.addEventListener(
    "pointercancel",
    finishCardDrag
);


/* =====================================================
   RESTART / TITLE
   ===================================================== */

function parentAction(action) {
    // components.html is sandboxed: top-level navigation can be rejected after a timer.
    // If same-origin access is available, update the Streamlit page URL and reload it;
    // the page's Python action handler then performs st.switch_page().
    try {
        const parentWindow = window.parent;
        const targetUrl = new URL(parentWindow.location.href);
        targetUrl.search = "";
        targetUrl.hash = "";
        targetUrl.searchParams.set("action", action);
        parentWindow.history.replaceState({}, "", targetUrl.toString());
        parentWindow.location.reload();
        return;
    } catch (error) {}

    // User-triggered pause actions are also real target=_top links, so this fallback
    // is only reached if the timed transition is blocked by the iframe sandbox.
    const statusNode = document.getElementById("status");
    if (statusNode) {
        statusNode.textContent = "NAVIGATION BLOCKED // browser sandbox prevented automatic transition.";
    }
}


// RESTART and TITLE are target=_top links so their user-activated navigation
// does not depend on JavaScript being allowed to navigate the sandbox's parent.


/* =====================================================
   FOCUS
   ===================================================== */

function focusGame() {

    try {

        root.focus(
            {
                preventScroll:
                    true
            }
        );

    }

    catch (error) {

        root.focus();

    }

}


root.addEventListener(
    "pointerdown",
    function () {

        if (
            !computerOpen &&
            !cardOpen
        ) {

            focusGame();

        }

    }
);


window.addEventListener(
    "blur",
    clearKeys
);


/* =====================================================
   PAUSE INITIAL STATE
   ===================================================== */

if (paused) {

    pauseOverlay.style.display =
        "flex";

}


/* =====================================================
   GAME LOOP
   ===================================================== */

function gameLoop() {

    updateMovement();

    requestAnimationFrame(
        gameLoop
    );

}


player.style.left =
    playerX + "%";


player.style.top =
    playerY + "%";


checkInteraction();

focusGame();

gameLoop();


})();

</script>


</body>

</html>
"""


# =========================================================
# SAFE PLACEHOLDER REPLACEMENT
# =========================================================

html = html.replace(
    "__FONT_BASE64__",
    font_base64,
)


html = html.replace(
    "__PAUSED__",
    "true"
    if paused
    else "false",
)

html = html.replace("__RESET_TUTORIAL_SAVE__", "true" if st.session_state.pop("tutorial_reset_save", False) else "false")


# =========================================================
# RENDER
# =========================================================

components.html(
    html,
    height=1000,
    scrolling=False,
)

