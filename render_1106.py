from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path

ROOT = Path(__file__).parent
FONT = "/tmp/NotoSansKR-800.ttf"
OUT = ROOT / "assets"
CASE = OUT / "case" / "2026-11-06"

def F(size): return ImageFont.truetype(FONT, size)
def T(d, xy, s, size, fill="#151515", anchor=None): d.text(xy, s, font=F(size), fill=fill, anchor=anchor)
def R(d, box, radius, fill, outline=None, width=1): d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
def crop(path, size): return ImageOps.fit(Image.open(path).convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))

def make_og():
    im = Image.new("RGB", (1200, 630), "white"); d = ImageDraw.Draw(im); d.rectangle((0,0,1200,12), fill="#e6002d")
    T(d, (70,84), "addit+", 52, "#e6002d"); T(d, (1128,82), "2026.11.06 FRI", 24, "#151515", "ra"); d.line((70,120,1130,120), fill="#e6e6e6", width=2)
    T(d, (70,182), "ADDIT DAILY MARKETING BRIEF", 22, "#e6002d"); T(d, (70,270), "AI 마케팅의 다음 경쟁은", 48); T(d, (70,330), "생성이 아니라 연결이다", 48)
    R(d, (70,390,1130,510), 20, "#fff1f3", "#f1d7dc", 2); T(d, (105,440), "TODAY’S SIGNAL", 24, "#e6002d"); T(d, (105,478), "신뢰·전환·현장 경험을 하나의 운영 흐름으로 연결합니다.", 22)
    d.ellipse((1029,419,1091,481), fill="#e6002d"); T(d, (1060,450), "AI", 27, "white", "mm"); T(d, (70,580), "TODAY’S TREND, TOMORROW’S STRATEGY.", 18, "#777")
    im.save(OUT / "og-2026-11-06-v1.png", optimize=True)

def make_vertical():
    im = Image.new("RGB", (1080,1920), "white"); d = ImageDraw.Draw(im); d.rectangle((0,0,1080,14), fill="#e6002d")
    T(d,(60,90),"addit+",46,"#e6002d"); T(d,(1018,86),"2026.11.06 FRI",18,"#151515","ra"); d.line((60,120,1020,120),fill="#e6e6e6")
    T(d,(60,170),"ADDIT DAILY MARKETING BRIEF",18,"#e6002d"); T(d,(60,235),"AI 마케팅의 다음 경쟁은",36); T(d,(60,282),"생성이 아니라 연결이다",36)
    R(d,(60,355,1020,461),18,"#fff1f3","#f1d7dc",2); T(d,(88,400),"GOOD MORNING, ADDIT",18,"#e6002d"); T(d,(88,433),"신뢰·전환·현장 경험을 하나의 흐름으로 연결합니다.",17,"#555")
    T(d,(60,525),"오늘의 5대 트렌드",24,"#e6002d"); signals=["젠트리, K-콘텐츠 데이터와 상업용 생성 에셋을 결합","네이버 쇼핑 AI 에이전트, 대화형 구매 여정으로 확장","AI가 AI를 인용하는 오류, GEO 정본 관리 필요","블럭스·Vivun, 분석을 넘어 실행까지 자동화","팝업·세대별 타깃 설계로 브랜드 경험 구체화"]
    y=555
    for i,s in enumerate(signals,1):
        R(d,(60,y,1020,y+55),12,"#fafafa","#e6e6e6"); d.ellipse((73,y+10,107,y+44),fill="#e6002d"); T(d,(90,y+27),f"{i:02d}",14,"white","mm"); T(d,(125,y+35),s,18); y+=67
    T(d,(60,930),"CASE STUDY · 4 KR / 1 GLOBAL",24,"#e6002d")
    cards=[("gentry.png","01 · 통로이미지 젠트리","K-콘텐츠 데이터로 상업용 비주얼 현지화","지역성 · 권리 구조 · 사용 맥락"),("naver.png","02 · NAVER 쇼핑 AI","검색·추천·비교를 대화형 구매 여정으로","의도 해석 · 개인화 · 탐색"),("blox.jpg","03 · 블럭스 AI CRM","고객 분석부터 발송·증분 매출까지","보낼 이유 · 추가 매출"),("popup.png","04 · OpenAds 팝업 데이터","브랜드 세계관과 숏폼 확산을 연결","체험 · 공유 장면"),("vivun.jpg","05 · Vivun AI sales teammate","통화 중 실시간 이의 제기 코칭","대화 · 근거 · 다음 행동")]
    y=960
    for fn,title,desc,insight in cards:
        R(d,(60,y,1020,y+125),16,"white","#e6e6e6"); im.paste(crop(CASE/fn,(190,95)),(75,y+15)); T(d,(290,y+45),title,20); T(d,(290,y+80),desc,16,"#555"); T(d,(290,y+105),insight,14,"#e6002d"); y+=140
    R(d,(60,1710,1020,1805),16,"#fff1f3","#f1d7dc",2); T(d,(90,1750),"ADDIT ACTION CHECK",19,"#e6002d"); T(d,(90,1782),"정본 데이터 · 증분 매출 · 권한 · 공유 장면을 설계했는가?",17); T(d,(60,1875),"TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief",15,"#777")
    im.save(OUT / "brief-2026-11-06-1080x1920.png", optimize=True)

make_og(); make_vertical()
