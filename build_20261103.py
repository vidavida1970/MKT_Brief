from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import html, json, re, shutil

BASE = Path('/workspace/scratch/ca3169652574')
ROOT = Path('/workspace/scratch/ca3169652574/mkt-repo-20261102')
CASE_DIR = ROOT / 'assets' / 'case' / '2026-11-03'
RAW = ROOT
FONT = '/tmp/NotoSansCJKkr-Bold.otf'
RED, INK, MUTED, LINE, PINK = '#E6002D', '#151515', '#5B5B5B', '#E6E6E6', '#FFF1F3'
TITLE = 'AI 도입의 다음 단계는 모델보다 운영 구조를 설계하는 일이다'
SUBTITLE = '오늘의 뉴스는 AI가 모델 내부를 고치고 현장 업무를 분류하며 전력망과 기업 네트워크까지 바꾸는 만큼, 실험을 운영 가능한 흐름으로 연결해야 한다는 점을 보여줍니다.'
PAGE_URL = 'https://vidavida1970.github.io/MKT_Brief/archive/2026-11-03/index.html'
SHARE_URL = PAGE_URL + '?kakao=20261103-ko-v1'
OG_URL = 'https://vidavida1970.github.io/MKT_Brief/assets/og-2026-11-03-v1.png'

CASES = [
    dict(no='01', region='KR', name='슈퍼브에이아이 × LH', strategy='비정형 사진을 현장 업무의 공통 분류 체계로 바꾸다',
         facts='슈퍼브에이아이는 LH의 하자 사진 자동분류 1차 사업을 완료했다고 밝혔다. VLM 한 모델이 사진 한 장에서 공간·부위자재·하자유형·공종·공사유형 5개 항목을 동시에 분류하며, 1만 8천여 가지 조합과 월 약 30만 장 규모를 처리하는 구조다.',
         insight='AI 도입의 첫 성과는 답변 생성보다 현장 데이터를 일관된 업무 언어로 바꾸는 데서 나온다.',
         source='https://blog-ko.superb-ai.com/superb-ai-delivers-vlm-based-defect-auto-classification-to-lh-18-000-categories-from-a-single-photo/', image_source='https://storage.ghost.io/c/73/74/73741b5e-0bdf-4e6f-9161-743bc6f76d78/content/images/2026/10/lh-img1-photo.jpg', image='superb-lh.jpg', alt='슈퍼브에이아이와 LH의 현장 하자 자동분류 사례 이미지'),
    dict(no='02', region='KR', name='한컴 노마디안', strategy='에이전트를 개인 비서가 아니라 역할별 AI 팀으로 설계하다',
         facts='한컴은 영업·마케팅·고객지원·계약·채용 등 12개 직무별 AI 팀원이 역할과 책임을 나누는 노마디안을 소개했다. 사용자는 에이전트 오너로서 최종 결정을 내리고, 시스템은 보고서·시트·슬라이드 형태의 결과물을 만드는 구조로 설명됐다.',
         insight='에이전트 도입은 사람을 줄이는 문제가 아니라 역할·승인·산출물의 경계를 다시 그리는 일이다.',
         source='https://www.hancomgroup.com/posts/3?menuId=46&parentId=22', image_source='https://www.hancomgroup.com/images/common/meta_img.jpg', image='hancom-nomadian.jpg', alt='한컴 노마디안 공식 페이지 이미지'),
    dict(no='03', region='KR', name='AI 정부 실험실', strategy='공무원의 실험을 조직의 운영 자산으로 전환하다',
         facts='행정안전부는 공무원이 AI로 현장 문제를 직접 해결하고, 검증된 결과를 조직이 책임지고 확산하는 정책을 추진한다고 밝혔다. 2030년까지 AI 챔피언 2만 명을 양성하고, 보안·개인정보 점검 기준과 산출물 관리 지침을 마련하는 방향을 제시했다.',
         insight='공공 AI는 개인의 빠른 실험과 기관의 보안·품질·운영 책임을 한 흐름으로 묶어야 확산된다.',
         source='https://m.korea.kr/briefing/pressReleaseView.do?newsId=156780691&pWise=ministryNews&repCode=A00031&repCodeType=%EC%A0%95%EB%B6%80%EB%B6%80%EC%B2%98', image_source='https://www.korea.kr/images/event/korea_logo_2024.jpg', image='gov-ai-lab.jpg', alt='대한민국 정책브리핑 AI 정부 실험실 공식 이미지'),
    dict(no='04', region='GLOBAL', name='MIT Weight-Space Programming', strategy='AI가 다른 모델의 가중치를 읽고 고치는 실험',
         facts='MIT 연구진은 GPT-6 Astra가 Qwen3.5-0.8B의 내부 가중치를 읽고 수정해 반복 응답과 게임 정책의 실패를 줄인 실험을 공개했다. 새로 학습해 모델을 키운 것이 아니라, 계산을 결정하는 수치 일부를 직접 편집한 초기 연구라는 점이 핵심이다.',
         insight='모델 성능 개선도 이제 재학습 일변도에서 내부 구조를 관찰·수정하는 운영 과제로 확장될 수 있다.',
         source='https://rikiyat.github.io/blog/weight-space-programming/', image_source='https://rikiyat.github.io/images/blog/weight-space-programming.png', image='mit-weight-space.png', alt='MIT 연구진의 AI 가중치 직접 수정 실험 도식'),
    dict(no='05', region='GLOBAL', name='OpenAI Grid Protectors Program', strategy='AI 데이터센터를 전력망의 운영 파트너로 설계하다',
         facts='OpenAI는 미래 컴퓨트 캠퍼스가 전력망 안정성과 소비자 전기요금 보호에 기여하도록 전력회사와 협력하는 프로그램을 소개했다. 조지아주 관련 계약에서는 필요할 때 최대 1,000MW 수요를 줄이는 구조와 기반시설 비용 부담 조건이 함께 공개됐다.',
         insight='AI 인프라 투자는 서버 확보만이 아니라 전력망·지역사회·비용 부담을 함께 설계하는 프로젝트가 된다.',
         source='https://openai.com/index/grid-protectors-program', image_source='https://images.ctfassets.net/kftzwdyauwt9/0147SbQFof5ozkgFJTdG0j/1daae8bb107fb504ef83be52e10e550f/introducing-the-grid-protectors-program-social.png?w=1600&h=900&fit=fill', image='openai-grid.jpg', alt='OpenAI Grid Protectors Program 공식 이미지'),
]

SIGNALS = [
    'AI가 답하는 단계를 넘어, 다른 모델의 가중치까지 직접 수정한다.',
    '이미지·영상 API가 업무 시스템에 들어오며 멀티모달 운영이 기본이 된다.',
    'LH 하자 분류처럼 현장 데이터의 표준화가 AI 도입의 첫 성과가 된다.',
    '에이전트는 개인 비서에서 역할·승인·산출물을 나누는 팀 구조로 이동한다.',
    'AI 인프라는 네트워크와 전력망까지 포함한 운영 프로젝트가 된다.',
]

SOURCE_ITEMS = [
    ('MIT Weight-Space Programming', 'GPT-6 Astra가 Qwen 가중치를 직접 읽고 수정한 실험', 'https://rikiyat.github.io/blog/weight-space-programming/'),
    ('LongCat 2.5 API', '이미지·영상 입력을 지원하는 API 제공 시작', 'https://longcat.chat/platform/docs/change-log'),
    ('LongCat 시각 이해', '이미지·영상 입력 규격과 활용 범위', 'https://longcat.chat/platform/docs/image-video-understanding'),
    ('Superb AI × LH', 'VLM 기반 하자 자동분류 1차 구축 완료', 'https://blog-ko.superb-ai.com/superb-ai-delivers-vlm-based-defect-auto-classification-to-lh-18-000-categories-from-a-single-photo/'),
    ('한컴 노마디안', '직무별 AI 팀 12명으로 미국 시장 진출 계획', 'https://www.hancomgroup.com/posts/3?menuId=46&parentId=22'),
    ('AI 정부 실험실', '공무원 직접개발과 보안·품질 관리 기준', 'https://m.korea.kr/briefing/pressReleaseView.do?newsId=156780691&pWise=ministryNews&repCode=A00031&repCodeType=%EC%A0%95%EB%B6%80%EB%B6%80%EC%B2%98'),
    ('OpenAI Grid Protectors', 'AI 컴퓨트 캠퍼스와 전력망 협력 프로그램', 'https://openai.com/index/grid-protectors-program'),
    ('Georgia Power × OpenAI', '최대 1,000MW 수요 조절과 비용 부담 조건', 'https://www.georgiapower.com/news-hub/press-releases/georgia-power-to-serve-openai-project-in-effingham-county.html'),
    ('Microsoft × Lumen', 'AI용 기업 네트워크 공동 판매 확대', 'https://news.microsoft.com/source/2026/11/02/lumen-and-microsoft-expand-collaboration-to-co-sell-enterprise-ai-ready-networks/'),
    ('Lumen Alkira', '멀티클라우드 네트워크 제어면 공식 안내', 'https://www.lumen.com/en-us/alkira-unified-cloud-networking-control-plane.htm.html'),
]

def font(size): return ImageFont.truetype(FONT, size)
def wrap(draw, text, ft, width):
    lines, line = [], ''
    for para in text.split('\n'):
        for ch in para:
            if draw.textbbox((0, 0), line + ch, font=ft)[2] <= width: line += ch
            else:
                if line: lines.append(line)
                line = ch
        if line: lines.append(line); line = ''
    return lines
def draw_wrap(draw, xy, text, ft, fill=INK, width=900, gap=7):
    x, y = xy
    for line in wrap(draw, text, ft, width):
        draw.text((x, y), line, font=ft, fill=fill); y += ft.size + gap
    return y
def rounded(draw, box, radius=18, fill='white', outline=LINE, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
def header(draw, width):
    margin = 70 if width == 1200 else 48
    draw.rectangle((0, 0, width, 14), fill=RED)
    draw.text((margin, 48 if width == 1200 else 42), 'addit+', font=font(42 if width == 1200 else 55), fill=RED)
    draw.text((950 if width == 1200 else width-275, 62), '2026.11.03 TUE', font=font(21 if width == 1200 else 22), fill=INK)
    draw.line((margin, 125, width-margin, 125), fill=LINE, width=2)

def create_images():
    ROOT.joinpath('assets').mkdir(parents=True, exist_ok=True)
    im = Image.new('RGB', (1200, 630), 'white'); d = ImageDraw.Draw(im); header(d, 1200)
    d.text((70, 160), 'ADDIT DAILY MARKETING BRIEF', font=font(22), fill=RED)
    y = draw_wrap(d, (70, 205), TITLE, font(43), width=1080, gap=4)
    draw_wrap(d, (70, y+18), SUBTITLE, font(20), fill=MUTED, width=1080, gap=3)
    d.rounded_rectangle((70, 535, 1130, 585), radius=25, fill=PINK)
    d.text((95, 547), "TODAY'S TREND, TOMORROW'S STRATEGY.", font=font(20), fill=RED)
    im.save(ROOT / 'assets/og-2026-11-03-v1.png')

    W, H, m = 1080, 1920, 48
    im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im); header(d, W)
    d.text((m, 160), 'ADDIT DAILY MARKETING BRIEF', font=font(19), fill=RED)
    y = draw_wrap(d, (m, 205), TITLE, font(35), width=W-2*m, gap=4)
    draw_wrap(d, (m, y+10), SUBTITLE, font(18), fill=MUTED, width=W-2*m, gap=2); y += 105
    rounded(d, (m, y, W-m, y+104), fill='#FAFAFA'); d.text((m+24, y+18), 'GOOD MORNING, ADDIT', font=font(22), fill=RED)
    draw_wrap(d, (m+24, y+56), '오늘은 AI의 실험을 현장과 운영 구조로 연결하는 방법을 살펴봅니다.', font(19), fill=MUTED, width=W-2*m-48, gap=2); y += 140
    d.text((m, y), "TODAY'S 5 SIGNALS", font=font(20), fill=RED); y += 40
    for i, s in enumerate(SIGNALS, 1):
        by = y + (i-1)*62; rounded(d, (m, by, W-m, by+51), radius=14); d.ellipse((m+12, by+7, m+48, by+43), fill=RED); d.text((m+20, by+13), f'{i:02d}', font=font(14), fill='white'); d.text((m+64, by+13), s, font=font(16), fill=INK)
    y += 5*62 + 24; d.text((m, y), 'CASE STUDY · 3 KR / 2 GLOBAL', font=font(20), fill=RED); y += 42
    for c in CASES:
        bh = 136; rounded(d, (m, y, W-m, y+bh), radius=18); src = Image.open(CASE_DIR / c['image']).convert('RGB'); crop = ImageOps.fit(src, (250, 98), method=Image.Resampling.LANCZOS); im.paste(crop, (m+16, y+19)); d.rounded_rectangle((m+16, y+19, m+266, y+117), radius=12, outline=LINE, width=1)
        d.ellipse((m+292, y+17, m+338, y+63), fill=RED); d.text((m+305, y+25), c['no'], font=font(15), fill='white'); d.text((m+362, y+21), c['name'], font=font(17), fill=INK); draw_wrap(d, (m+292, y+66), c['strategy'], font(13), fill=MUTED, width=650, gap=2); y += bh + 8
    y += 12; rounded(d, (m, y, W-m, y+170), radius=18, fill=PINK, outline='#F1D7DC'); d.text((m+24, y+15), 'ADDIT ACTION CHECK', font=font(20), fill=RED)
    actions = ['사용량을 업무 단위로 관리하는가?', '원문 근거와 검수자를 남겼는가?', '권한과 중단 조건을 정했는가?', '공식 도구·데이터 경로를 제공했는가?', '오프라인 처리와 보안 책임을 점검했는가?']
    for i, a in enumerate(actions): d.text((m+28, y+50+i*22), '□  '+a, font=font(15), fill=INK)
    y += 194; d.line((m, y, W-m, y), fill=LINE, width=2); d.text((m, y+17), 'AI를 잘 쓰는 조직은,', font=font(20), fill=MUTED); d.text((m, y+51), '더 좋은 모델보다 더 좋은 운영 구조를 만든다.', font=font(22), fill=INK)
    im.save(ROOT / 'assets/brief-2026-11-03-1080x1920.png')

def esc(value): return html.escape(value, quote=True)
def slug(value): return re.sub(r'[^a-z0-9가-힣]+', '-', value.lower()).strip('-')
def case_html(c):
    ident = slug(c['name'])
    return f'''<article class="case"><a data-case-study="{esc(ident)}" href="{esc(c['source'])}" target="_blank" rel="noopener noreferrer"><img data-source-image="{esc(c['image_source'])}" src="../../assets/case/2026-11-03/{esc(c['image'])}" alt="{esc(c['alt'])}"></a><div><div class="num">{c['no']} · {c['region']}</div><h3>{esc(c['name'])}</h3><p class="strategy">{esc(c['strategy'])}</p><p class="facts">{esc(c['facts'])}</p><a class="source" data-case-study="{ident}-source" href="{esc(c['source'])}" target="_blank" rel="noopener noreferrer">원문 보기 ↗</a></div><div class="insight"><strong>ADDIT INSIGHT</strong><p>{esc(c['insight'])}</p></div></article>'''

def create_html():
    watch_html = ''.join(f'<a href="{u}" target="_blank" rel="noopener noreferrer"><b>{esc(n)}</b><span>{esc(d)}</span></a>' for n,d,u in SOURCE_ITEMS)
    css_source = ROOT / 'archive' / '2026-10-30' / 'index.html'
    css = re.search(r'<style>(.*?)</style>', css_source.read_text(encoding='utf-8'), re.S).group(1)
    signals_html = ''.join(f'<div class="signal"><b>{i:02d}</b><p>{esc(s)}</p></div>' for i,s in enumerate(SIGNALS, 1))
    cards_html = '\n'.join(case_html(c) for c in CASES)
    html_doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(TITLE)} | Addit Daily Marketing Brief</title><meta name="description" content="{esc(SUBTITLE)}"><link rel="canonical" href="{PAGE_URL}"><link rel="image_src" href="{OG_URL}"><meta name="thumbnail" content="{OG_URL}"><meta property="og:type" content="article"><meta property="og:locale" content="ko_KR"><meta property="og:title" content="{esc(TITLE)}"><meta property="og:description" content="{esc(SUBTITLE)}"><meta property="og:url" content="{SHARE_URL}"><meta property="og:image" content="{OG_URL}"><meta property="og:image:url" content="{OG_URL}"><meta property="og:image:secure_url" content="{OG_URL}"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{esc(TITLE)}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(TITLE)}"><meta name="twitter:image" content="{OG_URL}"><style>{css}</style></head><body><main class="page"><div class="top"></div><div class="wrap"><header class="mast"><div class="brand">addit+</div><div class="date">2026.11.03 TUE</div></header><div class="hero"><div class="eyebrow">ADDIT DAILY MARKETING BRIEF</div><h1>AI 도입의 다음 단계는<br>모델보다 운영 구조를 설계하는 일이다</h1><p>{esc(SUBTITLE)}</p></div><div class="morning"><strong>GOOD MORNING, ADDIT</strong><p>오늘은 AI의 실험을 현장과 운영 구조로 연결하는 방법을 살펴봅니다.</p></div><section><div class="section-head"><h2>TODAY’S 5 SIGNALS</h2><span>11.03 · AI OPERATING BRIEF</span></div><div class="signals">{signals_html}</div></section><section><div class="section-head"><h2>CASE STUDY</h2><span>3 KR / 2 GLOBAL · 원문 대조 완료</span></div><div class="cases">{cards_html}</div></section><section><div class="section-head"><h2>SOURCE CHECK</h2><span>nextworks.dev 5건 원문 검수</span></div><div class="watch">{watch_html}</div></section><section class="action"><h2>ADDIT ACTION CHECK</h2><ul><li>현장 데이터를 공통 분류 체계로 바꿀 수 있는가?</li><li>에이전트의 역할·승인·산출물 경계가 분명한가?</li><li>실험 결과를 조직의 보안·품질 기준으로 연결했는가?</li><li>모델 API와 업무 시스템 사이의 운영 책임을 정했는가?</li><li>전력·네트워크·비용까지 인프라 계획에 포함했는가?</li></ul></section><footer class="footer"><strong>AI를 잘 쓰는 조직은,<br>더 좋은 모델보다 더 좋은 운영 구조를 만든다.</strong><div class="share"><a href="../../index.html?kakao=20261103-ko-v1">최신호 홈 ↗</a><a href="../../?kakao=20261103-ko-v1">전체 아카이브 ↗</a><a href="../../assets/brief-2026-11-03-1080x1920.png">세로 브리프 이미지 ↗</a></div><div class="credit">TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief · 2026.11.03</div></footer></div></main></body></html>'''
    out = ROOT / 'archive' / '2026-11-03'; out.mkdir(parents=True, exist_ok=True); (out / 'index.html').write_text(html_doc, encoding='utf-8')
    (ROOT / 'index.html').write_text(f'<meta http-equiv="refresh" content="0; url=archive/2026-11-03/index.html?kakao=20261103-ko-v1"><link rel="canonical" href="{PAGE_URL}">', encoding='utf-8')

def create_source():
    lines = ['# Addit Daily Marketing Brief · 2026-11-03', '', '## 한 줄 결론', '', '**AI 도입의 다음 단계는 모델보다 운영 구조를 설계하는 일이다.** 오늘의 5개 원문을 대조해 모델 수정, 멀티모달 API, 현장 표준화, 에이전트 팀, 전력·네트워크 인프라라는 다섯 축으로 재구성했다.', '', '## 오늘의 5대 트렌드', '']
    lines += [f'{i}. {s}' for i,s in enumerate(SIGNALS, 1)] + ['', '## CASE STUDY', '']
    for i,c in enumerate(CASES, 1): lines += [f'### {i}. {c["name"]} — {c["strategy"]}', '', '- 지역: ' + c['region'], '- 원문: ' + c['source'], '- 이미지: ' + c['image_source'], '- 확인 사실: ' + c['facts'], '- Addit Insight: ' + c['insight'], '']
    lines += ['## 원문 검수 목록', '']
    for n,d,u in SOURCE_ITEMS: lines += [f'- [{n}]({u}) — {d}']
    lines += ['', '## Addit ACTION CHECK', '', '- 현장 데이터를 공통 분류 체계로 바꿀 수 있는가?', '- 에이전트의 역할·승인·산출물 경계가 분명한가?', '- 실험 결과를 조직의 보안·품질 기준으로 연결했는가?', '- 모델 API와 업무 시스템 사이의 운영 책임을 정했는가?', '- 전력·네트워크·비용까지 인프라 계획에 포함했는가?', '', '## 출처 및 검증 메모', '', '- 원고: 사용자가 제공한 https://blog.nextworks.dev/daily/2026-11-03.', '- 링크 페이지의 5개 뉴스와 세부 원문 링크를 직접 요청해 정상 페이지 제목·내용을 확인했다.', '- CASE STUDY는 국내 3건·글로벌 2건으로 편성했다. 국내 사례는 슈퍼브에이아이×LH·한컴 노마디안·AI 정부 실험실이며, 글로벌 사례는 MIT Weight-Space Programming·OpenAI Grid Protectors다.', '- 모든 수치·정책·제공 범위는 원문 표현을 유지하고, 실행 해석은 Addit Insight로 분리했다.']
    (ROOT / 'source').mkdir(exist_ok=True); (ROOT / 'source' / '2026-11-03.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

def create_manifest():
    manifest = {'date':'2026-11-03','title':TITLE,'html':'archive/2026-11-03/index.html','published_url':SHARE_URL,'og_image_path':'assets/og-2026-11-03-v1.png','og_image_url':OG_URL,'cases':[{'name':c['name'],'region':c['region'],'source_url':c['source'],'image_source_url':c['image_source'],'image_local_path':'assets/case/2026-11-03/'+c['image']} for c in CASES]}
    (ROOT / 'brief-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

def create_readme():
    (ROOT / 'README.md').write_text('# MKT_Brief\n\n- [2026.11.03 · AI 도입의 다음 단계는 모델보다 운영 구조를 설계하는 일이다](archive/2026-11-03/index.html)\n- [2026.11.02 · AI를 잘 쓰는 조직은 한도·검수·책임을 먼저 설계한다](archive/2026-11-02/index.html)\n- [2026.10.30 · AI는 성능을 넘어, 실제 업무에 쓰이는 구조를 만든다](archive/2026-10-30/index.html)\n- [2026.10.29 · AI는 기능이 아니라, 자료·권한·검수의 흐름으로 설계된다](archive/2026-10-29/index.html)\n- [2026.10.28 · AI가 확장될수록, 비용·현장·책임을 함께 설계한다](archive/2026-10-28/index.html)\n- [2026.10.27 · AI가 커질수록, 접근권한과 책임을 먼저 설계한다](archive/2026-10-27/index.html)\n', encoding='utf-8')

def main():
    CASE_DIR.mkdir(parents=True, exist_ok=True)
    create_images(); create_html(); create_source(); create_manifest(); create_readme()

if __name__ == '__main__': main()
