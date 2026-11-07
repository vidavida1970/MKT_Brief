from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path

ROOT=Path(__file__).parent; FONT=str(ROOT/"assets"/"NotoSansKR-800.ttf"); OUT=ROOT/"assets"; CASE=OUT/"case"/"2026-11-07"
def F(n): return ImageFont.truetype(FONT,n)
def T(d,xy,s,n,fill="#151515",anchor=None): d.text(xy,s,font=F(n),fill=fill,anchor=anchor)
def R(d,box,rad,fill,outline=None,width=1): d.rounded_rectangle(box,radius=rad,fill=fill,outline=outline,width=width)
def crop(p,size): return ImageOps.fit(Image.open(p).convert("RGB"),size,method=Image.Resampling.LANCZOS,centering=(.5,.5))
def make_og():
 im=Image.new("RGB",(1200,630),"white"); d=ImageDraw.Draw(im); d.rectangle((0,0,1200,12),fill="#e6002d")
 T(d,(70,84),"addit+",52,"#e6002d"); T(d,(1128,82),"2026.11.07 SAT",24,"#151515","ra"); d.line((70,120,1130,120),fill="#e6e6e6",width=2)
 T(d,(70,182),"ADDIT DAILY MARKETING BRIEF",22,"#e6002d"); T(d,(70,265),"AI 경쟁의 다음 단계는 답변이 아니라",43); T(d,(70,325),"계속 실행되는 업무다",50)
 R(d,(70,390,1130,510),20,"#fff1f3","#f1d7dc",2); T(d,(105,440),"TODAY’S SIGNAL",24,"#e6002d"); T(d,(105,478),"AI가 콘텐츠와 업무를 계속 실행하는 흐름으로 이동합니다.",22)
 d.ellipse((1029,419,1091,481),fill="#e6002d"); T(d,(1060,450),"AI",27,"white","mm"); T(d,(70,580),"TODAY’S TREND, TOMORROW’S STRATEGY.",18,"#777"); im.save(OUT/"og-2026-11-07-v1.png",optimize=True)
def make_vertical():
 im=Image.new("RGB",(1080,1920),"white"); d=ImageDraw.Draw(im); d.rectangle((0,0,1080,14),fill="#e6002d")
 T(d,(60,90),"addit+",46,"#e6002d"); T(d,(1018,86),"2026.11.07 SAT",18,"#151515","ra"); d.line((60,120,1020,120),fill="#e6e6e6")
 T(d,(60,170),"ADDIT DAILY MARKETING BRIEF",18,"#e6002d"); T(d,(60,235),"AI 경쟁의 다음 단계는",36); T(d,(60,282),"답변이 아니라 계속 실행되는",36); T(d,(60,329),"업무다",36)
 R(d,(60,370,1020,476),18,"#fff1f3","#f1d7dc",2); T(d,(88,415),"GOOD MORNING, ADDIT",18,"#e6002d"); T(d,(88,448),"콘텐츠와 업무를 계속 실행하는 흐름을 점검합니다.",17,"#555")
 T(d,(60,535),"오늘의 5대 트렌드",24,"#e6002d"); sig=["Google Vids, 15초 AI 영상 제작을 무료·저비용으로 확장","네이버애즈, 광고 성과 진단에서 개선안 제안까지","경리나라 MCP, 회계 데이터를 쓰던 AI에서 분석","Meta Muse, 목적별 업무 공간을 대화로 생성","Perplexity Teammates, 상시 프로젝트로 전환"]
 y=565
 for i,s in enumerate(sig,1):
  R(d,(60,y,1020,y+55),12,"#fafafa","#e6e6e6"); d.ellipse((73,y+10,107,y+44),fill="#e6002d"); T(d,(90,y+27),f"{i:02d}",14,"white","mm"); T(d,(125,y+35),s,18); y+=67
 T(d,(60,940),"CASE STUDY · 3 KR / 2 GLOBAL",24,"#e6002d")
 cards=[("google-video.jpg","01 · Google Vids × Gemini","짧은 영상 제작을 무료·저비용 흐름으로","아이디어 → 시안"),("naver-ad.jpg","02 · 네이버애즈","성과 진단을 다음 액션 제안으로","진단 → 개선"),("finance-ai.png","03 · 웹케시 MCP","회계 데이터를 익숙한 AI로 연결","데이터 → 분석"),("muse.png","04 · Meta Muse Spaces","목적별 앱 화면을 대화로 생성","목적 → 공간"),("perplexity.png","05 · Perplexity Teammates","일회성 명령을 상시 프로젝트로","명령 → 지속 실행")]
 y=970
 for fn,title,desc,ins in cards:
  R(d,(60,y,1020,y+125),16,"white","#e6e6e6"); im.paste(crop(CASE/fn,(190,95)),(75,y+15)); T(d,(290,y+45),title,20); T(d,(290,y+80),desc,16,"#555"); T(d,(290,y+105),ins,14,"#e6002d"); y+=140
 R(d,(60,1710,1020,1805),16,"#fff1f3","#f1d7dc",2); T(d,(90,1750),"ADDIT ACTION CHECK",19,"#e6002d"); T(d,(90,1782),"권한 · 비용 · 승인 지점 · 사람 개입 기준을 정했는가?",17); T(d,(60,1875),"TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief",15,"#777"); im.save(OUT/"brief-2026-11-07-1080x1920.png",optimize=True)
make_og(); make_vertical()
