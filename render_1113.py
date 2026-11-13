from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path

ROOT = Path(__file__).parent
FONT = str(ROOT / "assets" / "NotoSansKR-800.ttf")
OUT = ROOT / "assets"
CASE = OUT / "case" / "2026-11-13"

def F(n): return ImageFont.truetype(FONT, n)
def T(d, xy, s, n, fill="#151515", anchor=None): d.text(xy, s, font=F(n), fill=fill, anchor=anchor)
def R(d, box, rad, fill, outline=None, width=1): d.rounded_rectangle(box, radius=rad, fill=fill, outline=outline, width=width)
def crop(p, size): return ImageOps.fit(Image.open(p).convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(.5, .5))

def make_og():
    im = Image.new("RGB", (1200, 630), "white"); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1200, 12), fill="#e6002d")
    T(d, (70, 84), "addit+", 52, "#e6002d"); T(d, (1128, 82), "2026.11.13 FRI", 24, anchor="ra")
    d.line((70, 120, 1130, 120), fill="#e6e6e6", width=2)
    T(d, (70, 182), "ADDIT DAILY MARKETING BRIEF", 22, "#e6002d")
    T(d, (70, 265), "AI가 일을 대신할수록,", 43)
    T(d, (70, 325), "맥락과 승인선이 중요하다", 43)
    R(d, (70, 390, 1130, 510), 20, "#fff1f3", "#f1d7dc", 2)
    T(d, (105, 440), "TODAY’S SIGNAL", 24, "#e6002d")
    T(d, (105, 478), "제조·반도체·안경·음성으로 넓어진 AI, 자동 실행의 경계를 설계합니다.", 20)
    d.ellipse((1029, 419, 1091, 481), fill="#e6002d"); T(d, (1060, 450), "AI", 27, "white", "mm")
    T(d, (70, 580), "TODAY’S TREND, TOMORROW’S STRATEGY.", 18, "#777")
    im.save(OUT / "og-2026-11-13-v1.png", optimize=True)

def make_vertical():
    im = Image.new("RGB", (1080, 1920), "white"); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1080, 14), fill="#e6002d")
    T(d, (60, 90), "addit+", 46, "#e6002d"); T(d, (1018, 86), "2026.11.13 FRI", 18, anchor="ra")
    d.line((60, 120, 1020, 120), fill="#e6e6e6")
    T(d, (60, 170), "ADDIT DAILY MARKETING BRIEF", 18, "#e6002d")
    T(d, (60, 235), "AI가 일을 대신할수록,", 35); T(d, (60, 282), "맥락과 승인선이 중요하다", 33)
    R(d, (60, 335, 1020, 441), 18, "#fff1f3", "#f1d7dc", 2)
    T(d, (88, 380), "GOOD MORNING, ADDIT", 18, "#e6002d"); T(d, (88, 413), "자동 실행의 경계와 사람의 판단을 함께 설계합니다.", 17, "#555")
    T(d, (60, 500), "오늘의 5대 트렌드", 24, "#e6002d")
    sig = [
        "클로드 코드 설정파일에서 3만여 개 비밀정보 확인, 자동 승인 경계 점검",
        "Claude for Manufacturing, 견적·품질·설비 진단을 검토선까지 연결",
        "Gemini Decision 1, 최대 1,000개 판단을 병렬 처리",
        "삼성 AI 안경과 Gemini, 기기·일상으로 확장되며 프라이버시 기준 필요",
        "SK하이닉스 기업용 ChatGPT 파일럿, 핵심기술 보호와 도입의 균형",
    ]
    y = 530
    for i, s in enumerate(sig, 1):
        R(d, (60, y, 1020, y + 55), 12, "#fafafa", "#e6e6e6")
        d.ellipse((73, y + 10, 107, y + 44), fill="#e6002d"); T(d, (90, y + 27), f"{i:02d}", 14, "white", "mm")
        T(d, (125, y + 35), s, 16); y += 67
    T(d, (60, 900), "CASE STUDY · 3 KR / 2 GLOBAL", 24, "#e6002d")
    cards = [
        ("skh_chatgpt.jpg", "01 · SK hynix", "반도체 개발에 기업용 ChatGPT 파일럿", "보안 → 단계적 확장"),
        ("samsung_ai_glasses.jpg", "02 · Samsung AI Eyewear", "Gemini 탑재 AI 안경 30종 공개", "기기 → 맥락"),
        ("openai_voice.jpg", "03 · OpenAI Voice", "Advanced·Standard 음성 12월 11일 종료", "기능 → 일관성"),
        ("claude_manufacturing.jpg", "04 · Anthropic", "Claude for Manufacturing 출시", "자동화 → 검토"),
        ("gemini_decisions.jpg", "05 · Google AI", "Gemini Decision 1, 1,000개 판단 병렬화", "생성 → 선택"),
    ]
    y = 930
    for fn, title, desc, ins in cards:
        R(d, (60, y, 1020, y + 125), 16, "white", "#e6e6e6"); im.paste(crop(CASE / fn, (190, 95)), (75, y + 15))
        T(d, (290, y + 45), title, 20); T(d, (290, y + 80), desc, 16, "#555"); T(d, (290, y + 105), ins, 14, "#e6002d"); y += 140
    R(d, (60, 1680, 1020, 1775), 16, "#fff1f3", "#f1d7dc", 2)
    T(d, (90, 1720), "ADDIT ACTION CHECK", 19, "#e6002d"); T(d, (90, 1752), "비밀정보 · 자동 승인 · 사람 검토 · 기기 프라이버시를 확인했는가?", 16)
    T(d, (60, 1875), "TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief", 15, "#777")
    im.save(OUT / "brief-2026-11-13-1080x1920.png", optimize=True)

make_og(); make_vertical()
