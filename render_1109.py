from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path

ROOT=Path(__file__).parent; FONT=str(ROOT/"assets"/"NotoSansKR-800.ttf"); OUT=ROOT/"assets"; CASE=OUT/"case"/"2026-11-09"
def F(n): return ImageFont.truetype(FONT,n)
def T(d,xy,s,n,fill="#151515",anchor=None): d.text(xy,s,font=F(n),fill=fill,anchor=anchor)
def R(d,box,rad,fill,outline=None,width=1): d.rounded_rectangle(box,radius=rad,fill=fill,outline=outline,width=width)
def crop(p,size): return ImageOps.fit(Image.open(p).convert("RGB"),size,method=Image.Resampling.LANCZOS,centering=(.5,.5))

def make_og():
    im=Image.new("RGB",(1200,630),"white"); d=ImageDraw.Draw(im); d.rectangle((0,0,1200,12),fill="#e6002d")
    T(d,(70,84),"addit+",52,"#e6002d"); T(d,(1128,82),"2026.11.09 MON",24,"#151515","ra"); d.line((70,120,1130,120),fill="#e6e6e6",width=2)
    T(d,(70,182),"ADDIT DAILY MARKETING BRIEF",22,"#e6002d"); T(d,(70,265),"AI의 다음 경쟁은 답변이 아니라",43); T(d,(70,325),"권한을 가진 실행이다",50)
    R(d,(70,390,1130,510),20,"#fff1f3","#f1d7dc",2); T(d,(105,440),"TODAY’S SIGNAL",24,"#e6002d"); T(d,(105,478),"권한·비용·검수 기준을 갖춘 실행을 설계합니다.",22)
    d.ellipse((1029,419,1091,481),fill="#e6002d"); T(d,(1060,450),"AI",27,"white","mm"); T(d,(70,580),"TODAY’S TREND, TOMORROW’S STRATEGY.",18,"#777"); im.save(OUT/"og-2026-11-09-v1.png",optimize=True)

def make_vertical():
    im=Image.new("RGB",(1080,1920),"white"); d=ImageDraw.Draw(im); d.rectangle((0,0,1080,14),fill="#e6002d")
    T(d,(60,90),"addit+",46,"#e6002d"); T(d,(1018,86),"2026.11.09 MON",18,"#151515","ra"); d.line((60,120,1020,120),fill="#e6e6e6")
    T(d,(60,170),"ADDIT DAILY MARKETING BRIEF",18,"#e6002d"); T(d,(60,235),"AI의 다음 경쟁은",36); T(d,(60,282),"답변이 아니라 권한을 가진",36); T(d,(60,329),"실행이다",36)
    R(d,(60,370,1020,476),18,"#fff1f3","#f1d7dc",2); T(d,(88,415),"GOOD MORNING, ADDIT",18,"#e6002d"); T(d,(88,448),"권한·비용·검수 기준을 점검합니다.",17,"#555")
    T(d,(60,535),"오늘의 5대 트렌드",24,"#e6002d"); sig=["개인재무·화면 조작, 답변에서 권한 있는 실행으로","국내 챗GPT 1,876만·클로드 1년 새 15배 성장","구독보다 토큰·업무량 중심의 AI 비용 관리","데이터센터 유치, 전력·수익성·수용성이 관건","반복 추천 학습이 편향과 오류를 키울 수 있어"]; y=565
    for i,s in enumerate(sig,1):
        R(d,(60,y,1020,y+55),12,"#fafafa","#e6e6e6"); d.ellipse((73,y+10,107,y+44),fill="#e6002d"); T(d,(90,y+27),f"{i:02d}",14,"white","mm"); T(d,(125,y+35),s,18); y+=67
    T(d,(60,940),"CASE STUDY · 4 KR / 1 GLOBAL",24,"#e6002d")
    cards=[("finance.png","01 · Claude Finance","은행·카드 데이터를 질문형 대시보드로","권한 → 신뢰"),("users.jpg","02 · 국내 AI 앱 확산","사용량과 체류시간이 경쟁 지표로","사용 → 습관"),("token.jpg","03 · KT 토큰 요금제","업무량에 맞춰 모델·비용을 선택","호출 → 비용"),("datacenter.jpg","04 · AI 데이터센터","기회보다 전력·수익성 조건을 먼저","인프라 → 검증"),("bias.png","05 · UNIST EchoTrace","반복 추천의 편향과 오류를 추적","추천 → 검수")]; y=970
    for fn,title,desc,ins in cards:
        R(d,(60,y,1020,y+125),16,"white","#e6e6e6"); im.paste(crop(CASE/fn,(190,95)),(75,y+15)); T(d,(290,y+45),title,20); T(d,(290,y+80),desc,16,"#555"); T(d,(290,y+105),ins,14,"#e6002d"); y+=140
    R(d,(60,1710,1020,1805),16,"#fff1f3","#f1d7dc",2); T(d,(90,1750),"ADDIT ACTION CHECK",19,"#e6002d"); T(d,(90,1782),"권한 · 비용 · 승인 지점 · 편향 지표를 정했는가?",17); T(d,(60,1875),"TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief",15,"#777"); im.save(OUT/"brief-2026-11-09-1080x1920.png",optimize=True)

make_og(); make_vertical()
