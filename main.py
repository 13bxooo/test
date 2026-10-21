import base64
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="PROJECT : LOGIC",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).resolve().parent
ASSET_DIR = ROOT / "assets"
BACKGROUND_PATH = ASSET_DIR / "title_background.jpeg"
FONT_CANDIDATES = (ROOT / "neodgm.ttf", ROOT / "neodgm(2).ttf")

# The title reference image is used as the actual background. Its original
# embedded menu is covered by the custom two-button menu below.
if not BACKGROUND_PATH.exists():
    BACKGROUND_PATH = ROOT / "title_background.jpeg"
if not BACKGROUND_PATH.exists():
    raise FileNotFoundError("title_background.jpeg 파일을 assets/ 또는 프로젝트 루트에 넣어 주세요.")
background_data = base64.b64encode(BACKGROUND_PATH.read_bytes()).decode("ascii")
font_data = ""
for candidate in FONT_CANDIDATES:
    if candidate.exists():
        font_data = base64.b64encode(candidate.read_bytes()).decode("ascii")
        break

# Resolve navigation requests before rendering the title page.
action = st.query_params.get("action", "")
if action:
    st.query_params.clear()
    if action == "title":
        st.session_state.game_paused = False
        st.session_state.start_open = False
        st.session_state.error_popup = False
        st.session_state.warning_popup = False
        st.rerun()
    elif action == "stage01":
        st.session_state.stage01_started = True
        st.session_state.game_started = True
        st.session_state.game_paused = False
        st.switch_page("pages/3_Stage_01.py")
    elif action == "tutorial":
        st.session_state.game_started = True
        st.session_state.game_paused = False
        st.session_state.tutorial_complete = False
        st.session_state.stage01_started = False
        st.session_state.stage02_started = False
        st.switch_page("pages/2_Game.py")

# Defaults used by the title screen. These flags are shared with the game pages.
defaults = {
    "start_open": False,
    "game_started": False,
    "game_paused": False,
    "game_finished": False,
    "tutorial_complete": False,
    "stage01_started": False,
    "stage02_started": False,
    "remaining_seconds": 15 * 60,
    "error_popup": False,
    "warning_popup": False,
    "settings_open": False,
    "sound_enabled": True,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Progress is inferred from the state maintained by the existing game pages.
# The pages' own localStorage saves are cleared when the reset flags below are consumed.
def has_saved_progress() -> bool:
    return bool(
        st.session_state.get("game_started", False)
        or st.session_state.get("tutorial_complete", False)
        or st.session_state.get("stage01_started", False)
        or st.session_state.get("stage02_started", False)
        or st.session_state.get("game_finished", False)
        or st.session_state.get("tutorial_step", 0)
        or st.session_state.get("s1_progress")
    )

st.markdown(
    f"""
<style>
@font-face {{
  font-family: NeoDungGeunMo;
  src: url(data:font/ttf;base64,{font_data}) format('truetype');
  font-weight: normal;
  font-style: normal;
}}
:root {{ color-scheme: dark; }}
#MainMenu, header, footer, [data-testid="stSidebar"] {{ display:none !important; visibility:hidden !important; }}
.stApp {{
