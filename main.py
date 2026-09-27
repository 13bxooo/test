import streamlit as st

st.set_page_config(
    page_title="PROJECT : ECHO",
    page_icon="◈",
    layout="wide"
)

# -------------------------
# CSS
# -------------------------
st.markdown("""
<style>

html, body, [data-testid="stAppViewContainer"] {
    background-color: #111820 !important;
}

[data-testid="stHeader"] {
    display: none;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* 전체 게임 화면 */
.game-screen {
    width: 100%;
    height: 100vh;

    background:
        repeating-linear-gradient(
            0deg,
            #182631 0px,
            #182631 39px,
            #1c2c38 40px
        );

    position: relative;
    overflow: hidden;
}

/* 제목 */
.game-title {
    position: absolute;
    top: 25px;
    left: 30px;

    padding: 10px 16px;

    background: #101820;
    border: 2px solid #71889a;

    color: white;

    font-family: monospace;
    font-size: 18px;
    font-weight: bold;

    letter-spacing: 2px;
}

/* 타이머 */
.timer {
    position: absolute;
    top: 25px;
    right: 30px;

    padding: 10px 16px;

    background: #101820;
    border: 2px solid #71889a;

    color: white;

    font-family: monospace;
    font-size: 17px;
}

/* 연구실 */
.room {
    position: absolute;

    left: 7%;
    right: 7%;
    top: 100px;
    bottom: 150px;

    background:
        repeating-linear-gradient(
            0deg,
            #1b2a35 0px,
            #1b2a35 39px,
            #20313d 40px
        );

    border: 3px solid #536b7c;

    box-shadow:
        inset 0 0 0 2px #0d151c,
        0 0 30px rgba(0,0,0,0.4);
}

/* ECHO */
.echo {
    position: absolute;

    top: 20%;
    left: 50%;

    transform: translateX(-50%);

    color: #9db3c4;

    font-family: monospace;
    font-size: 14px;

    letter-spacing: 6px;
}

/* 중앙 표시 */
.room-center {
    position: absolute;

    top: 45%;
    left: 50%;

    transform: translate(-50%, -50%);

    width: 230px;
    height: 120px;

    display: flex;
    justify-content: center;
    align-items: center;

    text-align: center;

    border: 2px solid #405766;

    color: #8097a8;

    font-family: monospace;
    font-size: 14px;

    line-height: 1.7;
}

/* 하단 메시지 */
.message-box {
    position: absolute;

    left: 7%;
    right: 7%;
    bottom: 25px;

    min-height: 90px;

    background: #f1f1f1;

    border: 3px solid #536b7c;

    display: flex;
    align-items: center;

    padding: 15px 20px;

    box-sizing: border-box;
}

.message-label {
    width: 130px;

    color: #243746;

    font-family: monospace;
    font-size: 13px;
    font-weight: bold;

    letter-spacing: 1px;
}

.message-text {
    color: #111820;

    font-family: monospace;
    font-size: 15px;

    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)


# -------------------------
# 게임 화면
# -------------------------

st.markdown("""
<div class="game-screen">

    <div class="game-title">
        ☰ PROJECT : ECHO
    </div>

    <div class="timer">
        TIME&nbsp;&nbsp;59:59
    </div>

    <div class="room">

        <div class="echo">
            E C H O
        </div>

        <div class="room-center">
            RESEARCH FACILITY<br>
            CONTROL ROOM
        </div>

    </div>

    <div class="message-box">

        <div class="message-label">
            SYSTEM
        </div>

        <div class="message-text">
            시스템이 초기화되었습니다.<br>
            <b>ECHO</b> 연결을 확인하고 있습니다...
        </div>

    </div>

</div>
""", unsafe_allow_html=True)
