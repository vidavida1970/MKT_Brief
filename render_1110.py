from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path

ROOT = Path(__file__).parent
FONT = str(ROOT / "assets" / "NotoSansKR-800.ttf")
OUT = ROOT / "assets"
CASE = OUT / "case" / "2026-11-10"

def F(n):
    return ImageFont.truetype(FONT, n)

def T(d, xy, s, n, fill="#151515", anchor=None):
    d.text(xy, s, font=F(n), fill=fill, anchor=anchor)

def R(d, box, rad, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=rad, fill=fill, outline=outline, width=width)

def crop(p, size):
    return ImageOps.fit(Image.open(p).convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(.5, .5))

def make_og():
    im = Image.new("RGB", (1200, 630), "white")
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1200, 12), fill="#e6002d")
    T(d, (70, 84), "addit+", 52, "#e6002d")
    T(d, (1128, 82), "2026.11.10 TUE", 24, "#151515", "ra")
    d.line((70, 120, 1130, 120), fill="#e6e6e6", width=2)
    T(d, (70, 182), "ADDIT DAILY MARKETING BRIEF", 22, "#e6002d")
    T(d, (70, 265), "AI의 진짜 경쟁력은", 43)
    T(d, (70, 325), "모델이 아니라 운영 조건이다", 48)
    R(d, (70, 390, 1130, 510), 20, "#fff1f3", "#f1d7dc", 2)
    T(d, (105, 440), "TODAY’S SIGNAL", 24, "#e6002d")
    T(d, (105, 478), "보안·권한·인프라·규제까지 설계한 AI가 살아남습니다.", 22)
    d.ellipse((1029, 419, 1091, 481), fill="#e6002d")
    T(d, (1060, 450), "AI", 27, "white", "mm")
    T(d, (70, 580), "TODAY’S TREND, TOMORROW’S STRATEGY.", 18, "#777")
    im.save(OUT / "og-2026-11-10-v1.png", optimize=True)

def make_vertical():
    im = Image.new("RGB", (1080, 1920), "white")
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1080, 14), fill="#e6002d")
    T(d, (60, 90), "addit+", 46, "#e6002d")
    T(d, (1018, 86), "2026.11.10 TUE", 18, "#151515", "ra")
    d.line((60, 120, 1020, 120), fill="#e6e6e6")
    T(d, (60, 170), "ADDIT DAILY MARKETING BRIEF", 18, "#e6002d")
    T(d, (60, 235), "AI의 진짜 경쟁력은", 36)
    T(d, (60, 282), "모델이 아니라 운영 조건이다", 36)
    R(d, (60, 335, 1020, 441), 18, "#fff1f3", "#f1d7dc", 2)
    T(d, (88, 380), "GOOD MORNING, ADDIT", 18, "#e6002d")
    T(d, (88, 413), "보안·권한·인프라·규제를 함께 점검합니다.", 17, "#555")
    T(d, (60, 500), "오늘의 5대 트렌드", 24, "#e6002d")
    sig = [
        "클로드 국내 계정 유출 신고, 기업 AI의 경계선 재점검",
        "Fable·Mythos와 신형 TPU, 모델·인프라 경쟁 동시 가속",
        "골드만삭스의 Claude Code 제한, 직무별 권한 분리 신호",
        "구미 데이터센터 임차 불발, 앵커 고객과 수익성의 현실",
        "AI 규제·음성 사기, 기술 도입의 안전 비용을 키워",
    ]
    y = 530
    for i, s in enumerate(sig, 1):
        R(d, (60, y, 1020, y + 55), 12, "#fafafa", "#e6e6e6")
        d.ellipse((73, y + 10, 107, y + 44), fill="#e6002d")
        T(d, (90, y + 27), f"{i:02d}", 14, "white", "mm")
        T(d, (125, y + 35), s, 18)
        y += 67
    T(d, (60, 900), "CASE STUDY · 4 KR / 1 GLOBAL", 24, "#e6002d")
    cards = [
        ("yna_privacy.jpg", "01 · Claude 계정 보안", "국내 기업 계정 100여개 유출 신고", "데이터 → 경계"),
        ("joongang_tpu.jpg", "02 · Google TPU", "에이전트 시대 작업량을 겨냥한 칩", "인프라 → 처리량"),
        ("hankyung_gumi.jpg", "03 · 구미 데이터센터", "큰손 임차 불발이 드러낸 수익성", "계약 → 검증"),
        ("kbs_chip.jpg", "04 · 반도체 시장", "규제·금리 우려가 만든 투자 변동성", "규제 → 리스크"),
        ("safetimes_voice.jpg", "05 · 음성 사기", "CEO 목소리 복제, 기업 송금 통제 필요", "신뢰 → 승인"),
    ]
    y = 930
    for fn, title, desc, ins in cards:
        R(d, (60, y, 1020, y + 125), 16, "white", "#e6e6e6")
        im.paste(crop(CASE / fn, (190, 95)), (75, y + 15))
        T(d, (290, y + 45), title, 20)
        T(d, (290, y + 80), desc, 16, "#555")
        T(d, (290, y + 105), ins, 14, "#e6002d")
        y += 140
    R(d, (60, 1680, 1020, 1775), 16, "#fff1f3", "#f1d7dc", 2)
    T(d, (90, 1720), "ADDIT ACTION CHECK", 19, "#e6002d")
    T(d, (90, 1752), "권한 · 앵커 고객 · 승인 지점 · 규제 시나리오를 정했는가?", 17)
    T(d, (60, 1875), "TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief", 15, "#777")
    im.save(OUT / "brief-2026-11-10-1080x1920.png", optimize=True)

make_og()
make_vertical()
