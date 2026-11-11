from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path

ROOT = Path(__file__).parent
FONT = str(ROOT / "assets" / "NotoSansKR-800.ttf")
OUT = ROOT / "assets"
CASE = OUT / "case" / "2026-11-12"

def F(n): return ImageFont.truetype(FONT, n)
def T(d, xy, s, n, fill="#151515", anchor=None): d.text(xy, s, font=F(n), fill=fill, anchor=anchor)
def R(d, box, rad, fill, outline=None, width=1): d.rounded_rectangle(box, radius=rad, fill=fill, outline=outline, width=width)
def crop(p, size): return ImageOps.fit(Image.open(p).convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(.5, .5))

def make_og():
    im = Image.new("RGB", (1200, 630), "white"); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1200, 12), fill="#e6002d")
    T(d, (70, 84), "addit+", 52, "#e6002d"); T(d, (1128, 82), "2026.11.12 THU", 24, anchor="ra")
    d.line((70, 120, 1130, 120), fill="#e6e6e6", width=2)
    T(d, (70, 182), "ADDIT DAILY MARKETING BRIEF", 22, "#e6002d")
    T(d, (70, 265), "AI가 업무 플랫폼이 될수록,", 43)
    T(d, (70, 325), "연결 보안이 경쟁력이 된다", 43)
    R(d, (70, 390, 1130, 510), 20, "#fff1f3", "#f1d7dc", 2)
    T(d, (105, 440), "TODAY’S SIGNAL", 24, "#e6002d")
    T(d, (105, 478), "업무 확장 속도만큼 권한·노출·데이터 주권을 설계해야 합니다.", 20)
    d.ellipse((1029, 419, 1091, 481), fill="#e6002d"); T(d, (1060, 450), "AI", 27, "white", "mm")
    T(d, (70, 580), "TODAY’S TREND, TOMORROW’S STRATEGY.", 18, "#777")
    im.save(OUT / "og-2026-11-12-v1.png", optimize=True)

def make_vertical():
    im = Image.new("RGB", (1080, 1920), "white"); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1080, 14), fill="#e6002d")
    T(d, (60, 90), "addit+", 46, "#e6002d"); T(d, (1018, 86), "2026.11.12 THU", 18, anchor="ra")
    d.line((60, 120, 1020, 120), fill="#e6e6e6")
    T(d, (60, 170), "ADDIT DAILY MARKETING BRIEF", 18, "#e6002d")
    T(d, (60, 235), "AI가 업무 플랫폼이 될수록,", 35); T(d, (60, 282), "연결 보안이 경쟁력이 된다", 33)
    R(d, (60, 335, 1020, 441), 18, "#fff1f3", "#f1d7dc", 2)
    T(d, (88, 380), "GOOD MORNING, ADDIT", 18, "#e6002d"); T(d, (88, 413), "업무 확장과 데이터 경계를 함께 설계합니다.", 17, "#555")
    T(d, (60, 500), "오늘의 5대 트렌드", 24, "#e6002d")
    sig = [
        "클로드 화이트보드·시트 출시, AI가 구조화된 업무로 이동",
        "비즈니스 인 챗GPT, 기업이 상품·회사 정보를 직접 관리",
        "제미나이 Carbon 공개·Hydrogen 테스트, 라인업 경쟁 심화",
        "업무용 AI 연결 서버 8,000여 개 노출, 커넥터가 새 공격면",
        "한국 디지털·AI 경쟁력 10위, 온디바이스 AI도 부상",
    ]
    y = 530
    for i, s in enumerate(sig, 1):
        R(d, (60, y, 1020, y + 55), 12, "#fafafa", "#e6e6e6")
        d.ellipse((73, y + 10, 107, y + 44), fill="#e6002d"); T(d, (90, y + 27), f"{i:02d}", 14, "white", "mm")
        T(d, (125, y + 35), s, 17); y += 67
    T(d, (60, 900), "CASE STUDY · 4 KR / 1 GLOBAL", 24, "#e6002d")
    cards = [
        ("openai_business.jpg", "01 · OpenAI 비즈니스", "기업이 챗GPT 상품정보 직접 관리", "검색 → 정본 데이터"),
        ("donga_exposed.jpg", "02 · 업무 연결 보안", "AI 관련 시스템 8,030개 인터넷 노출", "연결 → 공격면"),
        ("korea_rank.jpg", "03 · 한국 경쟁력", "디지털·AI 경쟁력 세계 10위", "정책 → 실행력"),
        ("korea_startup.jpg", "04 · AI 스타트업 정책", "2030년 AI 유니콘 20개 육성", "생태계 → 자본"),
        ("qualcomm_ondevice.jpg", "05 · Qualcomm·KORA", "인터넷 없이 쓰는 AI 네이티브 OS", "클라우드 → 로컬"),
    ]
    y = 930
    for fn, title, desc, ins in cards:
        R(d, (60, y, 1020, y + 125), 16, "white", "#e6e6e6"); im.paste(crop(CASE / fn, (190, 95)), (75, y + 15))
        T(d, (290, y + 45), title, 20); T(d, (290, y + 80), desc, 16, "#555"); T(d, (290, y + 105), ins, 14, "#e6002d"); y += 140
    R(d, (60, 1680, 1020, 1775), 16, "#fff1f3", "#f1d7dc", 2)
    T(d, (90, 1720), "ADDIT ACTION CHECK", 19, "#e6002d"); T(d, (90, 1752), "정본 데이터 · 연결 권한 · 노출면 · 로컬 처리 범위를 정했는가?", 16)
    T(d, (60, 1875), "TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief", 15, "#777")
    im.save(OUT / "brief-2026-11-12-1080x1920.png", optimize=True)

make_og(); make_vertical()
