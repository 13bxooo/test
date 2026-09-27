import streamlit as st

st.set_page_config(
    page_title="PROJECT : ECHO",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------
# 기본 설정
# -------------------------
st.markdown("""
<style>
    /* Streamlit 기본 여백 제거 */
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    header {
        visibility: hidden;
    }

    /* 전체 배경 */
    .stApp {
        background: #111820;
    }

    /* 게임 화면 */
    .game-screen {
        position: relative;
        width: 100%;
        height: 100vh;
        overflow: hidden;
        background:
            linear-gradient(
                rgba(20, 35, 48, 0.92),
                rgba(20, 35, 48, 0.92)
            ),
            repeating-linear-gradient(
                0deg,
                transparent,
                transparent 31px,
                rgba(255,255,255,0.025) 32px
            ),
            repeating-linear-gradient(
                90deg,
                transparent,
                transparent 31px,
                rgba(255,255,255,0.025) 32px
            );
    }

    /* -------------------------
       상단 좌측 타이틀
       ------------------------- */
    .game-title {
        position: absolute;
        top: 24px;
        left: 28px;

        padding: 10px 16px;

        background: rgba(10, 18, 26, 0.9);
        border: 2px solid #6d879d;

        color: #ffffff;
        font-family: monospace;
        font-size: 18px;
        font-weight: bold;

        letter-spacing: 2px;
    }

    /* -------------------------
       상단 우측 타이머
       ------------------------- */
    .timer {
        position: absolute;
        top: 24px;
        right: 28px;

        padding: 10px 16px;

        background: rgba(10, 18, 26, 0.9);
        border: 2px solid #6d879d;

        color: #ffffff;
        font-family: monospace;
        font-size: 17px;

        letter-spacing: 1px;
    }

    /* -------------------------
       중앙 연구시설
       ------------------------- */
    .room {
        position: absolute;

        left: 7%;
        right: 7%;
        top: 100px;
        bottom: 155px;

        border: 3px solid #526b7d;

        background:
            repeating-linear-gradient(
                0deg,
                #1b2934 0px,
                #1b2934 39px,
                #1e2d38 40px
            );

        box-shadow:
            inset 0 0 0 2px #101820,
            0 0 30px rgba(0,0,0,0.4);
    }

    /* 바닥 중앙 표시 */
    .room-center {
        position: absolute;

        left: 50%;
        top: 45%;

        transform: translate(-50%, -50%);

        width: 220px;
        height: 120px;

        border: 2px solid #405766;

        display: flex;
        justify-content: center;
        align-items: center;

        color: #71899a;
        font-family: monospace;
        font-size: 14px;

        text-align: center;
    }

    /* -------------------------
       하단 시스템 메시지
       ------------------------- */
    .message-box {
        position: absolute;

        left: 7%;
        right: 7%;
        bottom: 28px;

        min-height: 92px;

        background: #f1f1f1;

        border: 3px solid #526b7d;

        display: flex;
        align-items: center;

        padding: 14px 20px;

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
        flex: 1;

        color: #111820;
        font-family: monospace;
        font-size: 15px;

        line-height: 1.6;
    }

    /* -------------------------
       중앙 ECHO 표시
       ------------------------- */
    .echo {
        position: absolute;

        left: 50%;
        top: 24%;

        transform: translateX(-50%);

        color: #9bb2c4;
        font-family: monospace;

        font-size: 13px;
        letter-spacing: 5px;
    }

</style>
""", unsafe_allow_html=True)


# -------------------------
# 게임 화면
# -------------------------

st.markdown("""
<div class="game-screen">

    <!-- 타이틀 -->
    <div class="game-title">
        ☰ PROJECT : ECHO
    </div>

    <!-- 타이머 -->
    <div class="timer">
        TIME  59:59
    </div>

    <!-- 방 -->
    <div class="room">

        <div class="echo">
            E C H O
        </div>

        <div class="room-center">
            RESEARCH FACILITY<br>
            CONTROL ROOM
        </div>

    </div>

    <!-- 시스템 메시지 -->
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
