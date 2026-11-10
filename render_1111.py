from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path

ROOT = Path(__file__).parent
FONT = str(ROOT / "assets" / "NotoSansKR-800.ttf")
OUT = ROOT / "assets"
CASE = OUT / "case" / "2026-11-11"

def F(n): return ImageFont.truetype(FONT, n)
def T(d, xy, s, n, fill="#151515", anchor=None): d.text(xy, s, font=F(n), fill=fill, anchor=anchor)
def R(d, box, rad, fill, outline=None, width=1): d.rounded_rectangle(box, radius=rad, fill=fill, outline=outline, width=width)
def crop(p, size): return ImageOps.fit(Image.open(p).convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(.5, .5))

def make_og():
    im = Image.new("RGB", (1200, 630), "white"); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1200, 12), fill="#e6002d")
    T(d, (70, 84), "addit+", 52, "#e6002d"); T(d, (1128, 82), "2026.11.11 WED", 24, anchor="ra")
    d.line((70, 120, 1130, 120), fill="#e6e6e6", width=2)
    T(d, (70, 182), "ADDIT DAILY MARKETING BRIEF", 22, "#e6002d")
    T(d, (70, 265), "AI 확장은 빨라도,", 46)
    T(d, (70, 325), "데이터 경계와 책임 설계가 먼저다", 40)
    R(d, (70, 390, 1130, 510), 20, "#fff1f3", "#f1d7dc", 2)
    T(d, (105, 440), "TODAY’S SIGNAL", 24, "#e6002d")
    T(d, (105, 478), "더 많이 쓰는 AI일수록 권한·승인·검수 기준이 필요합니다.", 21)
    d.ellipse((1029, 419, 1091, 481), fill="#e6002d"); T(d, (1060, 450), "AI", 27, "white", "mm")
    T(d, (70, 580), "TODAY’S TREND, TOMORROW’S STRATEGY.", 18, "#777")
    im.save(OUT / "og-2026-11-11-v1.png", optimize=True)

def make_vertical():
    im = Image.new("RGB", (1080, 1920), "white"); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1080, 14), fill="#e6002d")
    T(d, (60, 90), "addit+", 46, "#e6002d"); T(d, (1018, 86), "2026.11.11 WED", 18, anchor="ra")
    d.line((60, 120, 1020, 120), fill="#e6e6e6")
    T(d, (60, 170), "ADDIT DAILY MARKETING BRIEF", 18, "#e6002d")
    T(d, (60, 235), "AI 확장은 빨라도,", 36); T(d, (60, 282), "데이터 경계와 책임 설계가 먼저다", 32)
    R(d, (60, 335, 1020, 441), 18, "#fff1f3", "#f1d7dc", 2)
    T(d, (88, 380), "GOOD MORNING, ADDIT", 18, "#e6002d"); T(d, (88, 413), "권한·승인·검수 기준을 함께 설계합니다.", 17, "#555")
    T(d, (60, 500), "오늘의 5대 트렌드", 24, "#e6002d")
    sig = [
        "클로드 국내 계정 유출 신고, 기업 AI의 데이터 경계 재점검",
        "클로드 국내 앱 사용자 500만, 실험에서 업무 기본값으로",
        "제미나이 Carbon·Robotics 2.5, 화면 밖 현실로 확장",
        "클로드 오피스 공개, AI 경쟁이 업무 소프트웨어로 이동",
        "평가위원 사진 유출·미국 소송, AI 책임 기준이 쟁점으로",
    ]
    y = 530
    for i, s in enumerate(sig, 1):
        R(d, (60, y, 1020, y + 55), 12, "#fafafa", "#e6e6e6")
        d.ellipse((73, y + 10, 107, y + 44), fill="#e6002d"); T(d, (90, y + 27), f"{i:02d}", 14, "white", "mm")
        T(d, (125, y + 35), s, 18); y += 67
    T(d, (60, 900), "CASE STUDY · 3 KR / 2 GLOBAL", 24, "#e6002d")
    cards = [
        ("ddaily_privacy.png", "01 · 조달청 AI 개발", "평가위원 189명 얼굴사진 유출", "데이터 → 통제"),
        ("donga_claude.jpg", "02 · 국내 Claude 확산", "앱 사용자 500만, 1년 새 10배", "사용 → 표준"),
        ("hankyung_bubble.jpg", "03 · AI 버블 경고", "닷컴버블보다 큰 충격 가능성", "투자 → 시나리오"),
        ("google_carbon.jpg", "04 · Google AI", "Carbon과 Robotics 2.5 동시 확장", "모델 → 현실"),
        ("sbs_openai.jpg", "05 · OpenAI 소송", "8개 주정부, 청소년 안전 쟁점", "안전 → 책임"),
    ]
    y = 930
    for fn, title, desc, ins in cards:
        R(d, (60, y, 1020, y + 125), 16, "white", "#e6e6e6"); im.paste(crop(CASE / fn, (190, 95)), (75, y + 15))
        T(d, (290, y + 45), title, 20); T(d, (290, y + 80), desc, 16, "#555"); T(d, (290, y + 105), ins, 14, "#e6002d"); y += 140
    R(d, (60, 1680, 1020, 1775), 16, "#fff1f3", "#f1d7dc", 2)
    T(d, (90, 1720), "ADDIT ACTION CHECK", 19, "#e6002d"); T(d, (90, 1752), "데이터 경계 · 승인 지점 · 책임 주체 · 비용 시나리오를 정했는가?", 16)
    T(d, (60, 1875), "TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief", 15, "#777")
    im.save(OUT / "brief-2026-11-11-1080x1920.png", optimize=True)

make_og(); make_vertical()
