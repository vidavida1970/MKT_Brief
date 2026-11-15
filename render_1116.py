from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path

ROOT=Path(__file__).parent; FONT=str(ROOT/'assets'/'NotoSansKR-800.ttf'); OUT=ROOT/'assets'; CASE=OUT/'case'/'2026-11-16'
def F(n): return ImageFont.truetype(FONT,n)
def T(d,xy,s,n,fill='#151515',anchor=None): d.text(xy,s,font=F(n),fill=fill,anchor=anchor)
def R(d,box,rad,fill,outline=None,width=1): d.rounded_rectangle(box,radius=rad,fill=fill,outline=outline,width=width)
def crop(p,size): return ImageOps.fit(Image.open(p).convert('RGB'),size,method=Image.Resampling.LANCZOS,centering=(.5,.5))
def make_og():
 im=Image.new('RGB',(1200,630),'white'); d=ImageDraw.Draw(im); d.rectangle((0,0,1200,12),fill='#e6002d')
 T(d,(70,84),'addit+',52,'#e6002d'); T(d,(1128,82),'2026.11.16 MON',24,anchor='ra'); d.line((70,120,1130,120),fill='#e6e6e6',width=2)
 T(d,(70,182),'ADDIT DAILY MARKETING BRIEF',22,'#e6002d'); T(d,(70,265),'AI에 권한을 줄수록,',43); T(d,(70,325),'검수와 공급망이 중요하다',43)
 R(d,(70,390,1130,510),20,'#fff1f3','#f1d7dc',2); T(d,(105,440),'TODAY’S SIGNAL',24,'#e6002d'); T(d,(105,478),'업무·거래·시험으로 넓어진 AI, 권한·인증정보·검수선을 함께 설계합니다.',20)
 d.ellipse((1029,419,1091,481),fill='#e6002d'); T(d,(1060,450),'AI',27,'white','mm'); T(d,(70,580),'TODAY’S TREND, TOMORROW’S STRATEGY.',18,'#777'); im.save(OUT/'og-2026-11-16-v1.png',optimize=True)
def make_vertical():
 im=Image.new('RGB',(1080,1920),'white'); d=ImageDraw.Draw(im); d.rectangle((0,0,1080,14),fill='#e6002d')
 T(d,(60,90),'addit+',46,'#e6002d'); T(d,(1018,86),'2026.11.16 MON',18,anchor='ra'); d.line((60,120,1020,120),fill='#e6e6e6')
 T(d,(60,170),'ADDIT DAILY MARKETING BRIEF',18,'#e6002d'); T(d,(60,235),'AI에 권한을 줄수록,',35); T(d,(60,282),'검수와 공급망이 중요하다',33)
 R(d,(60,335,1020,441),18,'#fff1f3','#f1d7dc',2); T(d,(88,380),'GOOD MORNING, ADDIT',18,'#e6002d'); T(d,(88,413),'AI 권한의 범위와 사람의 검수선을 함께 설계합니다.',17,'#555')
 T(d,(60,500),'오늘의 5대 트렌드',24,'#e6002d')
 sig=['시험장까지 들어온 생성형 AI, 자격검정의 기기·검수 체계 재설계','Cursor 침해, 협력사 키 노출이 악성 확장 배포로 이어진 공급망 경고','Fable 5.2, 1,000개 에이전트로 Lean 형식화 실험','SKT AX 챌린지, 자료 수집은 AI·판단과 승인은 사람으로 분리','AI 쇼핑·닷츠 확산, 추천에서 거래·실행으로 권한 이동']
 y=530
 for i,s in enumerate(sig,1):
  R(d,(60,y,1020,y+55),12,'#fafafa','#e6e6e6'); d.ellipse((73,y+10,107,y+44),fill='#e6002d'); T(d,(90,y+27),f'{i:02d}',14,'white','mm'); T(d,(125,y+35),s,16); y+=67
 T(d,(60,900),'CASE STUDY · 4 KR / 1 GLOBAL',24,'#e6002d')
 cards=[('tax_ai_cheating.jpg','01 · KR','세무사 시험 AI 부정행위 자수','시험 → 검수'),('skt_ax_challenge.jpg','02 · KR','SKT AX 챌린지, 업무를 AI에 맡겨보니','업무 → 분업'),('hyundai_chatgpt_shopping.jpg','03 · KR','더현대 하이, 앱스 인 챗GPT 입점','추천 → 거래'),('dots_ai_assistant.jpg','04 · KR','GPT 기반 AI 비서 닷츠의 권한 설계','비서 → 권한'),('cursor_security.jpg','05 · GLOBAL','Cursor 협력사 키 노출과 악성 확장','키 → 공급망')]
 y=930
 for fn,title,desc,ins in cards:
  R(d,(60,y,1020,y+125),16,'white','#e6e6e6'); im.paste(crop(CASE/fn,(190,95)),(75,y+15)); T(d,(290,y+45),title,20); T(d,(290,y+80),desc,16,'#555'); T(d,(290,y+105),ins,14,'#e6002d'); y+=140
 R(d,(60,1680,1020,1775),16,'#fff1f3','#f1d7dc',2); T(d,(90,1720),'ADDIT ACTION CHECK',19,'#e6002d'); T(d,(90,1752),'권한 · 인증정보 · 공급망 · 사람 검수선을 확인했는가?',16); T(d,(60,1875),'TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief',15,'#777'); im.save(OUT/'brief-2026-11-16-1080x1920.png',optimize=True)
make_og(); make_vertical()
