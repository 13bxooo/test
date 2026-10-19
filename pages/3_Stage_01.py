import base64
from pathlib import Path
import re
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PROJECT : LOGIC // STAGE 01",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Stage 01 intentionally reuses page 2's original in-iframe stylesheet so the
# scene framing, room, player, ECHO bar, help and inventory panels stay consistent.
page_dir = Path(__file__).resolve().parent
project_root = page_dir.parent
font_data = ""
for candidate in (
    project_root / "neodgm.ttf",
    project_root / "neodgm(2).ttf",
    Path("neodgm.ttf"),
    Path("neodgm(2).ttf"),
):
    if candidate.exists():
        font_data = base64.b64encode(candidate.read_bytes()).decode("ascii")
        break

page2_source = (page_dir / "2_Game.py").read_text(encoding="utf-8")
page2_html_match = re.search(r'html\s*=\s*r"""(.*?)"""', page2_source, re.S)
if not page2_html_match:
    st.error("2페이지의 게임 템플릿을 찾지 못했습니다. pages/2_Game.py를 확인하세요.")
    st.stop()
style_match = re.search(r"<style>(.*?)</style>", page2_html_match.group(1), re.S)
if not style_match:
    st.error("2페이지의 스타일 템플릿을 읽지 못했습니다.")
    st.stop()
tutorial_css = style_match.group(1).replace("__FONT_BASE64__", font_data)

st.markdown(
    """
    <style>
    #MainMenu,header,footer,[data-testid="stSidebar"]{visibility:hidden;display:none}
    .stApp{background:#000!important;color:#fff!important}
    .block-container{padding:0!important;max-width:100%!important}
    iframe{border:0!important}
    </style>
    """,
    unsafe_allow_html=True,
)

html = r"""
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<style>
__TUTORIAL_CSS__
/* Stage-specific additions. Page 2's base scene styles are used above. */
.stage01-timer{position:absolute;top:28px;right:72px;z-index:22;color:#777;font-size:11px;letter-spacing:1px}
.stage01-pause{position:absolute;top:18px;right:18px;z-index:160;width:34px;height:34px;padding:0;border:0;background:#000;color:#fff;font-size:20px;line-height:1}
.stage01-pause:hover{background:#fff;color:#000}
.stage01-object{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;width:15%;height:10%;min-width:90px;padding:8px!important;background:#090909}
.stage01-object .main-label{font-size:12px;color:#ddd;line-height:1.4}
.stage01-object .sub-label{font-size:9px;color:#666;line-height:1.4}
.stage01-object.near{border-color:#eee;color:#fff;box-shadow:0 0 0 1px #ffffff22}
.stage01-a{left:11%;top:17%}
.stage01-b{left:42%;top:13%;width:16%;height:13%}
.stage01-c{right:12%;top:18%}
.stage01-archive{left:15%;bottom:17%;width:18%;height:10%}
.stage01-panel{right:13%;bottom:17%;width:18%;height:10%}
.stage01-object .object-label{bottom:-22px}
.stage01-window-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;align-items:center}
.stage01-window-actions button,.stage01-window-actions a{min-width:150px;text-align:center;justify-content:center}
.pause-actions{visibility:visible;pointer-events:auto}
.pause-actions button,.pause-actions a{min-width:150px;text-align:center;justify-content:center;text-decoration:none}
.computer-overlay.show{display:flex}
@media(max-width:700px){
 .stage01-timer{top:49px;right:56px;font-size:10px}
 .stage01-pause{top:10px;right:10px}
 .stage01-object{min-width:56px;padding:4px!important}
 .stage01-object .main-label{font-size:9px}
 .stage01-object .sub-label{font-size:8px}
 .stage01-a{left:3%;top:16%}
 .stage01-b{left:36%;top:13%;width:20%;height:12%}
 .stage01-c{right:3%;top:17%}
 .stage01-archive{left:3%;bottom:16%;width:22%;height:10%}
 .stage01-panel{right:3%;bottom:16%;width:22%;height:10%}
 .stage01-window-actions button,.stage01-window-actions a{min-width:120px}
}
</style></head><body>
<div class="game" id="gameRoot" tabindex="0">
  <div class="project-title">PROJECT : LOGIC</div>
  <div class="stage-title">STAGE 01 // ARCHIVE ACCESS</div>
  <div class="stage01-timer" id="timer">12:00</div>
  <button class="stage01-pause" id="pauseBtn" type="button" aria-label="Pause">Ⅱ</button>

  <div class="game-area" id="gameArea">
    <div class="mobile-controls" id="mobileControls">
      <button class="control-button control-up" data-direction="w" type="button">▲</button>
      <button class="control-button control-left" data-direction="a" type="button">◀</button>
      <button class="control-button control-right" data-direction="d" type="button">▶</button>
      <button class="control-button control-down" data-direction="s" type="button">▼</button>
    </div>

    <div class="room" id="room">
      <div class="room-line-horizontal"></div>
      <div class="room-line-vertical"></div>

      <div class="object stage01-object stage01-a" id="objectA" data-id="A"><span class="main-label">SECTOR A</span><span class="sub-label" id="stateA">DATA SEALED</span></div>
      <div class="object stage01-object stage01-b" id="objectB" data-id="B"><span class="main-label">COMPUTER / B</span><span class="sub-label" id="stateB">DATA SEALED</span></div>
      <div class="object stage01-object stage01-c" id="objectC" data-id="C"><span class="main-label">SECTOR C</span><span class="sub-label" id="stateC">DATA SEALED</span></div>
      <div class="object stage01-object stage01-archive" id="objectArchive" data-id="ARCHIVE"><span class="main-label">ARCHIVE NOTE</span><span class="sub-label" id="stateArchive">UNREAD</span></div>
      <div class="object stage01-object stage01-panel" id="objectPanel" data-id="PANEL"><span class="main-label">SECURITY PANEL</span><span class="sub-label" id="statePanel">LOCKED</span></div>

      <div class="exit-wall" id="exitDoor" data-id="EXIT"></div>
      <div class="exit-sign"><span class="exit-arrow">↓ ↑</span><br><span>[EXIT] ARCHIVE ACCESS</span></div>
      <div class="player" id="player"></div>
      <div class="interaction-message" id="interactionMessage">PRESS E</div>

      <div class="echo-bar">
        <div class="echo-name">ECHO // AI SYSTEM</div>
        <div class="echo-message" id="echoMessage"></div>
        <div class="echo-next" id="echoNext">SPACE // SKIP / NEXT</div>
      </div>
    </div>
  </div>

  <div class="status" id="status">ECHO SYSTEM // ONLINE</div>

  <div class="overlay" id="inventoryOverlay" style="display:none">
    <div class="inventory-panel">
      <div class="inventory-header"><div class="inventory-title">INVENTORY</div><div class="inventory-close">I / ESC TO CLOSE</div></div>
      <div class="inventory-grid">
        <div class="inventory-slot" data-slot="0"></div><div class="inventory-slot" data-slot="1"></div><div class="inventory-slot" data-slot="2"></div><div class="inventory-slot" data-slot="3"></div>
        <div class="inventory-slot" data-slot="4"></div><div class="inventory-slot" data-slot="5"></div><div class="inventory-slot" data-slot="6"></div><div class="inventory-slot" data-slot="7"></div>
      </div>
      <div class="item-description" id="itemDescription">ITEM DESCRIPTION<br><br>기록을 선택하면 내용이 표시됩니다.</div>
    </div>
  </div>

  <div class="overlay" id="helpOverlay" style="display:none">
    <div class="help-panel">
      <div class="help-header"><div class="help-title">HOW TO PLAY</div><div class="help-close">H / ESC TO CLOSE</div></div>
      <div class="help-row"><div class="help-number">01</div><div class="help-key">MOVEMENT<br>W A S D</div><div class="help-description">WASD 키로 시설 내부를 직접 이동합니다.</div></div>
      <div class="help-row"><div class="help-number">02</div><div class="help-key">INTERACTION<br>E</div><div class="help-description">가까이 있는 구역 기록, 보관 기록, 보안 패널을 조사합니다.</div></div>
      <div class="help-row"><div class="help-number">03</div><div class="help-key">INVENTORY<br>I</div><div class="help-description">획득한 기록을 확인합니다.</div></div>
      <div class="help-row"><div class="help-number">04</div><div class="help-key">SYSTEM<br>SPACE</div><div class="help-description">현재 대사를 완성하거나 다음 안내를 확인합니다.</div></div>
      <div class="help-row"><div class="help-number">05</div><div class="help-key">HELP<br>H</div><div class="help-description">조작 방법을 다시 확인합니다. ESC로 열린 창을 닫습니다.</div></div>
      <div style="margin-top:22px;padding:16px;background:#090909;border-left:2px solid #fff"><div style="margin-bottom:8px;font-size:13px">ARCHIVE ACCESS</div><div style="color:#888;font-size:11px;line-height:1.8">A·B·C 구역의 숫자와 ARCHIVE NOTE의 세 식을 대조해 무작위 세 자리 코드를 복원하십시오. 인증 후 EXIT에 접근할 수 있습니다.</div></div>
    </div>
  </div>

  <div class="computer-overlay" id="dataOverlay">
    <div class="computer-panel"><div class="computer-title" id="windowTitle">RECORD</div><div class="computer-sub" id="windowSub">ARCHIVE ACCESS // RECOVERED DATA</div><div id="windowBody"></div><button class="code-button" id="closeRecord" type="button">CLOSE / ESC</button></div>
  </div>

  <div class="computer-overlay" id="codeOverlay">
    <div class="computer-panel"><div class="computer-title">SECURITY PANEL</div><div class="computer-sub">AUTHENTICATION // THREE DIGITS</div><div class="access-sequence">ARCHIVE ACCESS CODE<div class="computer-sub">각 식에 A, B, C 기록값을 대입하십시오.</div></div><input class="code-input" id="codeInput" type="text" inputmode="numeric" autocomplete="off" maxlength="3" aria-label="3자리 접근 코드"><button class="code-button" id="verifyBtn" type="button">VERIFY</button><div class="code-error" id="codeError"></div><button class="code-button" id="closeCode" type="button">CLOSE / ESC</button></div>
  </div>

  <div class="pause-overlay" id="pauseOverlay">
    <div><div class="pause-title">GAME PAUSED</div><div class="pause-sub">PRESS Ⅱ TO CONTINUE</div><div class="pause-actions"><button class="code-button" id="resumeBtn" type="button">RESUME</button><button class="code-button" id="restartBtn" type="button">RESTART</button><a class="code-button" href="?action=title" target="_top" rel="noopener" style="display:flex;align-items:center;justify-content:center;box-sizing:border-box;text-decoration:none">TITLE</a></div></div>
  </div>
</div>

<script>
(function(){
'use strict';
const $=id=>document.getElementById(id);
const root=$('gameRoot'), room=$('room'), player=$('player'), interactionMessage=$('interactionMessage');
const inventoryOverlay=$('inventoryOverlay'), helpOverlay=$('helpOverlay'), dataOverlay=$('dataOverlay'), codeOverlay=$('codeOverlay'), pauseOverlay=$('pauseOverlay');
const echoMessage=$('echoMessage'), echoNext=$('echoNext'), status=$('status'), timerNode=$('timer');
let playerX=50, playerY=43, seconds=720, paused=false, finished=false, codeSolved=false, nearby=null;
let helpOpen=false, inventoryOpen=false, dataOpen=false, codeOpen=false, typingDone=false, typingTimer=null, echoIndex=0;
let timerLast=Date.now();
const keys={w:false,a:false,s:false,d:false};
const inventory=Array(8).fill(null);
const items=[];
const messages=[
 '연결이 확인되었습니다. 저는 ECHO입니다. 이 구역에서는 기록의 수집과 논리적 대조가 필요합니다.',
 'W A S D 키로 이동하고, 장치 가까이에서 E를 눌러 기록을 확보하십시오. 움직임과 기록 수집은 실시간으로 진행됩니다.',
 '각 구역의 숫자는 정답 자체가 아닙니다. A, B, C와 보관 기록을 함께 해석해야 합니다.',
 'H는 도움말, I는 인벤토리입니다. SPACE로 현재 대사를 완성하거나 다음 안내를 확인할 수 있습니다.',
 '제한 시간은 12분입니다. 보안 패널 인증을 마친 뒤 EXIT로 이동하십시오.'
];
const puzzleCandidates=[];
for(let a=2;a<=9;a++)for(let b=1;b<a;b++)for(let c=a+1;c<=Math.min(9,a+b-1);c++)puzzleCandidates.push({A:a,B:b,C:c});
let puzzle=puzzleCandidates[Math.floor(Math.random()*puzzleCandidates.length)];
let expectedCode=String(puzzle.A-puzzle.B)+String(puzzle.C-puzzle.A)+String(puzzle.A+puzzle.B-puzzle.C);
const found={A:false,B:false,C:false,ARCHIVE:false};
const clues={};
function rebuildClues(){
 clues.A={title:'SECTOR A // ACCESS LOG',body:`출입 기록 04-A\n\n“A의 기록값은 ${puzzle.A}이다. 이 값을 그대로 코드에 입력하지 말 것.”\n\nRECOVERED VALUE: ${puzzle.A}`};
 clues.B={title:'COMPUTER / SECTOR B',body:`시스템 진단 로그\n\n“B의 기록값은 ${puzzle.B}이다. 다른 구역의 기록과 함께 계산할 것.”\n\nRECOVERED VALUE: ${puzzle.B}`};
 clues.C={title:'SECTOR C // MAINTENANCE',body:`정비 기록 17-C\n\n“C의 기록값은 ${puzzle.C}이다. 보관 기록의 세 번째 식에도 사용된다.”\n\nRECOVERED VALUE: ${puzzle.C}`};
}
rebuildClues();
const objects=[
 {id:'A',name:'SECTOR A',x:11,y:17,w:15,h:10,el:$('objectA')},
 {id:'B',name:'COMPUTER / SECTOR B',x:42,y:13,w:16,h:13,el:$('objectB')},
 {id:'C',name:'SECTOR C',x:77,y:18,w:15,h:10,el:$('objectC')},
 {id:'ARCHIVE',name:'ARCHIVE NOTE',x:15,y:73,w:18,h:10,el:$('objectArchive')},
 {id:'PANEL',name:'SECURITY PANEL',x:69,y:73,w:18,h:10,el:$('objectPanel')},
 {id:'EXIT',name:'EXIT',x:92,y:35,w:8,h:30,el:$('exitDoor')}
];
const obstacles=objects.map(o=>({x:o.x,y:o.y,w:o.w,h:o.h}));
function say(t){status.textContent=t}
function updateTimer(){const m=Math.floor(seconds/60),s=seconds%60;timerNode.textContent=String(m).padStart(2,'0')+':'+String(s).padStart(2,'0')}
function clearKeys(){Object.keys(keys).forEach(k=>keys[k]=false)}
function isOverlayOpen(){return helpOpen||inventoryOpen||dataOpen||codeOpen||finished}
function showRecord(title,body){helpOpen=false;inventoryOpen=false;codeOpen=false;helpOverlay.style.display='none';inventoryOverlay.style.display='none';codeOverlay.style.display='none';$('closeRecord').style.display='inline-block';$('windowTitle').textContent=title;$('windowSub').textContent='ARCHIVE ACCESS // RECOVERED DATA';$('windowBody').innerHTML='<div style="margin:10px 0;color:#aaa;line-height:1.9;white-space:pre-line">'+body.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')+'</div>';dataOpen=true;dataOverlay.style.display='flex';clearKeys()}
function closeRecord(){if(finished)return;dataOpen=false;dataOverlay.style.display='none';root.focus()}
function showCode(){if(!['A','B','C','ARCHIVE'].every(k=>found[k])){showRecord('SECURITY PANEL // LOCKED','ACCESS DENIED\n\nA·B·C 구역 기록과 ARCHIVE NOTE를 모두 확보해야 합니다.');return}codeOpen=true;codeOverlay.style.display='flex';$('codeInput').value='';$('codeError').textContent='';clearKeys();setTimeout(()=>$('codeInput').focus(),30)}
function closeCode(){codeOpen=false;codeOverlay.style.display='none';root.focus()}
function renderInventory(){document.querySelectorAll('.inventory-slot').forEach((slot,i)=>{const item=inventory[i];slot.innerHTML=item?`<div class="slot-number">${String(i+1).padStart(2,'0')}</div><div class="item-name">${item.name}</div>`:`<div class="slot-number">${String(i+1).padStart(2,'0')}</div><div class="empty-text">EMPTY</div>`;slot.classList.remove('selected')})}
function openInventory(){if(dataOpen||codeOpen||paused||finished)return;if(inventoryOpen){inventoryOpen=false;inventoryOverlay.style.display='none';root.focus();return}helpOpen=false;helpOverlay.style.display='none';inventoryOpen=true;inventoryOverlay.style.display='flex';$('itemDescription').innerHTML='ITEM DESCRIPTION<br><br>기록을 선택하면 설명이 표시됩니다.';renderInventory();clearKeys()}
function openHelp(){if(dataOpen||codeOpen||paused||finished)return;if(helpOpen){helpOpen=false;helpOverlay.style.display='none';root.focus();return}inventoryOpen=false;inventoryOverlay.style.display='none';helpOpen=true;helpOverlay.style.display='flex';clearKeys()}
function addItem(id){if(items.some(item=>item.id===id))return;let item;if(id==='ARCHIVE'){item={id,name:'ARCHIVE NOTE',body:'첫째 자리 = A − B.\n둘째 자리 = C − A.\n셋째 자리 = A + B − C.'}}else item={id,name:clues[id].title,body:clues[id].body};items.push(item);const slot=items.length-1;if(slot<inventory.length)inventory[slot]=item;renderInventory()}
function interact(){if(paused||finished||isOverlayOpen())return;if(!nearby){say('NO TARGET // 가까운 장치로 이동하십시오.');return}const id=nearby.id;if(clues[id]){if(!found[id]){found[id]=true;addItem(id);$('state'+id).textContent='DATA FOUND';say(id+' 기록을 확보했습니다. INVENTORY에서 다시 확인할 수 있습니다.')}showRecord(clues[id].title,clues[id].body);return}if(id==='ARCHIVE'){found.ARCHIVE=true;$('stateArchive').textContent='READ';addItem('ARCHIVE');say('ARCHIVE NOTE 확보 // 세 식을 각각 계산하십시오.');showRecord('ARCHIVE NOTE // FRAGMENT 04','첫째 자리 = A − B.\n둘째 자리 = C − A.\n셋째 자리 = A + B − C.\n\n기록의 숫자를 각 식에 대입하고, 순서대로 이어 붙이십시오.');return}if(id==='PANEL'){showCode();return}if(id==='EXIT'){if(!codeSolved){say('EXIT SEALED // SECURITY PANEL 인증이 필요합니다.');return}finishStage();return}}
function verify(){const input=$('codeInput').value.trim();if(input===expectedCode){codeSolved=true;$('statePanel').textContent='UNLOCKED';$('codeError').textContent='ACCESS GRANTED // 출구로 이동하십시오.';say('인증 완료. EXIT로 이동해 스테이지를 마무리하십시오.');setTimeout(()=>{if(codeOpen)closeCode()},900)}else{$('codeError').textContent='INVALID CODE // 기록의 규칙을 다시 확인하십시오.';say('인증 실패 // 기록과 계산 순서를 다시 대조하십시오.')}}
function addRestartAndTitleButtons(title,sub,copy){helpOpen=false;inventoryOpen=false;dataOpen=true;codeOpen=false;helpOverlay.style.display='none';inventoryOverlay.style.display='none';codeOverlay.style.display='none';pauseOverlay.style.display='none';$('closeRecord').style.display='none';$('windowTitle').textContent=title;$('windowSub').textContent=sub;$('windowBody').innerHTML=copy+'<div class="stage01-window-actions"><button class="code-button" id="clearRestart" type="button">RESTART</button><a class="code-button" href="?action=title" target="_top" rel="noopener" style="display:inline-flex;align-items:center;text-decoration:none">TITLE</a></div>';const b=$('clearRestart');if(b)b.onclick=restartStage;dataOpen=true;dataOverlay.style.display='flex'}
function finishStage(){finished=true;clearKeys();pauseOverlay.style.display='none';addRestartAndTitleButtons('STAGE 01 CLEAR','ARCHIVE ACCESS // COMPLETE','<p>ACCESS GRANTED</p><p>ARCHIVE ACCESS가 완료되었습니다.</p>');say('STAGE 01 CLEAR // 다음 구역의 신호가 감지되었습니다.')}
function expireGame(){if(finished)return;finished=true;clearKeys();addRestartAndTitleButtons('TIME EXPIRED','SYSTEM LOCKDOWN','<p>제한 시간이 종료되었습니다.</p>');say('TIME EXPIRED // RESTART를 선택하십시오.')}
function syncTimer(){const now=Date.now();if(!paused&&!finished){const elapsed=(now-timerLast)/1000;if(elapsed>=1){const spent=Math.floor(elapsed);seconds=Math.max(0,seconds-spent);timerLast+=spent*1000;updateTimer();if(seconds===0)expireGame()}}else timerLast=now}
function getDistance(obj){return Math.hypot(playerX-(obj.x+obj.w/2),playerY-(obj.y+obj.h/2))}
function checkInteraction(){nearby=null;let best=Infinity;objects.forEach(obj=>{const d=getDistance(obj);obj.el.classList.remove('near');if(d<12&&d<best){best=d;nearby=obj}});if(nearby&&!paused&&!isOverlayOpen()){nearby.el.classList.add('near');interactionMessage.textContent='E  //  '+nearby.name;interactionMessage.classList.add('visible')}else interactionMessage.classList.remove('visible')}
function circleHitsRect(cx,cy,r,o){const dx=Math.max(o.x,Math.min(cx,o.x+o.w));const dy=Math.max(o.y,Math.min(cy,o.y+o.h));return Math.hypot(cx-dx,cy-dy)<r}
function blocked(x,y){if(x<3||x>97||y<3||y>96)return true;return obstacles.some(o=>circleHitsRect(x,y,1.3,o))}
function updateMovement(){if(paused||isOverlayOpen())return;let dx=(keys.d?1:0)-(keys.a?1:0),dy=(keys.s?1:0)-(keys.w?1:0);if(!dx&&!dy)return;const len=Math.hypot(dx,dy);dx=dx/len*.48;dy=dy/len*.48;if(!blocked(playerX+dx,playerY))playerX+=dx;if(!blocked(playerX,playerY+dy))playerY+=dy;player.style.left=playerX+'%';player.style.top=playerY+'%';checkInteraction()}
function typeEcho(index){echoIndex=index;clearTimeout(typingTimer);const text=messages[index]||'';echoMessage.textContent='';typingDone=false;echoNext.classList.remove('ready');let i=0;function tick(){if(i<text.length){echoMessage.textContent+=text[i++];typingTimer=setTimeout(tick,24)}else{typingDone=true;echoNext.classList.add('ready')}}tick()}
function nextEcho(){if(!typingDone){clearTimeout(typingTimer);echoMessage.textContent=messages[echoIndex]||'';typingDone=true;echoNext.classList.add('ready');return}if(echoIndex<messages.length-1)typeEcho(echoIndex+1)}
function restartStage(){paused=false;finished=false;codeSolved=false;seconds=720;timerLast=Date.now();playerX=50;playerY=43;nearby=null;helpOpen=inventoryOpen=dataOpen=codeOpen=false;[inventoryOverlay,helpOverlay,dataOverlay,codeOverlay,pauseOverlay].forEach(el=>el.style.display='none');Object.keys(found).forEach(k=>found[k]=false);items.length=0;inventory.fill(null);$('stateA').textContent=$('stateB').textContent=$('stateC').textContent='DATA SEALED';$('stateArchive').textContent='UNREAD';$('statePanel').textContent='LOCKED';puzzle=puzzleCandidates[Math.floor(Math.random()*puzzleCandidates.length)];expectedCode=String(puzzle.A-puzzle.B)+String(puzzle.C-puzzle.A)+String(puzzle.A+puzzle.B-puzzle.C);rebuildClues();renderInventory();updateTimer();player.style.left=playerX+'%';player.style.top=playerY+'%';echoIndex=0;typeEcho(0);say('SYSTEM READY // 접근 가능한 장치 가까이 이동하십시오.');clearKeys();checkInteraction();root.focus()}
function resume(){paused=false;pauseOverlay.style.display='none';timerLast=Date.now();root.focus();clearKeys()}
function focusGame(){try{root.focus({preventScroll:true})}catch(e){root.focus()}}

$('pauseBtn').addEventListener('click',()=>{if(finished)return;if(!paused&&(helpOpen||inventoryOpen||dataOpen||codeOpen))return;paused=!paused;timerLast=Date.now();pauseOverlay.style.display=paused?'flex':'none';clearKeys();if(!paused)focusGame()});
$('resumeBtn').addEventListener('click',resume);$('restartBtn').addEventListener('click',restartStage);
$('closeRecord').addEventListener('click',closeRecord);$('closeCode').addEventListener('click',closeCode);$('verifyBtn').addEventListener('click',verify);
$('codeInput').addEventListener('input',e=>{e.target.value=e.target.value.replace(/\D/g,'').slice(0,3)});$('codeInput').addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();verify()}if(e.key==='Escape'){e.preventDefault();closeCode()}});
document.querySelectorAll('[data-direction]').forEach(btn=>{const k=btn.dataset.direction;const down=e=>{e.preventDefault();keys[k]=true;focusGame()};const up=e=>{e.preventDefault();keys[k]=false};btn.addEventListener('pointerdown',down);['pointerup','pointercancel','lostpointercapture'].forEach(ev=>btn.addEventListener(ev,up))});
document.querySelectorAll('.inventory-slot').forEach((slot,i)=>slot.addEventListener('click',()=>{document.querySelectorAll('.inventory-slot').forEach(s=>s.classList.remove('selected'));slot.classList.add('selected');const item=inventory[i];$('itemDescription').innerHTML=item?`<strong>${item.name}</strong><br><br>${item.body.replace(/\n/g,'<br>')}`:'ITEM DESCRIPTION<br><br>비어 있는 슬롯입니다.'}));
document.addEventListener('keydown',e=>{const key=e.key.toLowerCase();if(document.activeElement===$('codeInput')){if(key==='escape'){e.preventDefault();closeCode()}return}if(e.repeat&&['e','h','i','escape'].includes(key))return;if(e.code==='Space'){e.preventDefault();if(!paused&&!isOverlayOpen())nextEcho();return}if(key==='escape'){if(codeOpen){closeCode();return}if(dataOpen){closeRecord();return}if(helpOpen){openHelp();return}if(inventoryOpen){openInventory();return}if(paused){resume();return}return}if(key==='h'){e.preventDefault();openHelp();return}if(key==='i'){e.preventDefault();openInventory();return}if(key==='e'){e.preventDefault();interact();return}if(['w','a','s','d'].includes(key)&&!paused&&!isOverlayOpen()){keys[key]=true;e.preventDefault()}});
document.addEventListener('keyup',e=>{const key=e.key.toLowerCase();if(key in keys){keys[key]=false;e.preventDefault()}});window.addEventListener('blur',clearKeys);root.addEventListener('pointerdown',focusGame);
function loop(){updateMovement();checkInteraction();requestAnimationFrame(loop)}
player.style.left=playerX+'%';player.style.top=playerY+'%';renderInventory();updateTimer();typeEcho(0);checkInteraction();focusGame();setInterval(syncTimer,250);requestAnimationFrame(loop);
})();
</script></body></html>
"""

html = html.replace("__TUTORIAL_CSS__", tutorial_css)
components.html(html, height=1000, scrolling=False)
