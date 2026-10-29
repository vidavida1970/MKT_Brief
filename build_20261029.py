from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import html, json, re, shutil

BASE = Path('/workspace/scratch/ca3169652574')
ROOT = BASE / 'work-2026-10-29'
CASE_DIR = ROOT / 'assets' / 'case' / '2026-10-29'
RAW = Path('/tmp/mkt29-sources/raw')
FONT = '/workspace/NotoSansKR-Bold.ttf'
RED, INK, MUTED, LINE, PINK = '#E6002D', '#151515', '#5B5B5B', '#E6E6E6', '#FFF1F3'
TITLE = 'AI는 기능이 아니라, 자료·권한·검수의 흐름으로 설계된다'
SUBTITLE = '두 뉴스 다이제스트의 중복을 걷어내고, 개인정보 연결·보안 전용 모델·에이전트 실행 기반·로컬 AI·전문 업무 평가를 하나의 운영 원칙으로 묶었습니다.'
PAGE_URL = 'https://vidavida1970.github.io/MKT_Brief/archive/2026-10-29/index.html'
SHARE_URL = PAGE_URL + '?kakao=20261029-ko-v1'
OG_URL = 'https://vidavida1970.github.io/MKT_Brief/assets/og-2026-10-29-v1.png'

CASES = [
    dict(no='01', region='KR', name='질병관리청 건강도우미 챗봇', strategy='국가 데이터를 또래 비교와 생활습관 안내로 바꾸다',
         facts='질병관리청은 20년간 축적된 500만 건 이상의 지역사회건강조사 자료를 기반으로 건강도우미 챗봇을 개방했다. 이용자는 또래와 건강 상태를 비교하고 만성질환 위험도·생활습관 정보를 대화로 확인할 수 있다.',
         insight='공공 AI는 데이터 규모보다 개인이 다음 행동을 정할 수 있는 비교 기준과 설명 구조가 중요하다.',
         source='https://www.aitimes.kr/news/articleView.html?idxno=42468', image_source='https://cdn.aitimes.kr/news/thumbnail/202610/42468_63838_1323_v150.jpg', image='kdca.jpg', alt='질병관리청 건강도우미 챗봇을 소개하는 인공지능신문 대표 이미지'),
    dict(no='02', region='GLOBAL', name='Gemini 4 Carbon', strategy='고위험 보안 업무는 성능과 접근 통제를 함께 공개하다',
         facts='Google DeepMind는 장기 작업과 사이버 방어를 겨냥한 Gemini 4 Carbon을 발표하고 초기에는 일부 보안 전문가부터 제공한다고 밝혔다. 일반 개발자·기업·소비자 대상 공개 일정은 아직 정해지지 않은 제한 제공 단계다.',
         insight='고성능 모델의 출시일보다 누가 어떤 인증·기록·사용 목적 아래 쓰는지가 도입 판단의 핵심이다.',
         source='https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/', image_source='https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_carbon_102726_social_share.width-1300.png', image='gemini-carbon.png', alt='Gemini 4 Carbon 공식 발표 이미지'),
    dict(no='03', region='GLOBAL', name='Microsoft Copilot harness', strategy='모델보다 실행 기반을 공통화해 멀티모델을 운영하다',
         facts='Microsoft는 여러 모델에 작업 지시, 자료, 도구 호출과 실행 통제를 연결하는 Copilot harness를 개발자·기업에 제공한다고 발표했다. Copilot Code·Studio·GitHub Copilot 앱과 명령줄 도구 등에 공통 실행 기반을 적용하는 구조다.',
         insight='기업 에이전트의 표준화 대상은 모델 하나가 아니라 권한·도구·실행 기록을 묶는 harness다.',
         source='https://blogs.microsoft.com/blog/2026/10/28/introducing-the-microsoft-copilot-harness-unlocking-the-potential-of-truly-multi-model-agentic-work/', image_source='https://blogs.microsoft.com/wp-content/uploads/2026/10/OMB-CoreAI-Hero-Final-10_28-1024x576.png', image='copilot-harness.png', alt='Microsoft Copilot harness 공식 발표 이미지'),
    dict(no='04', region='GLOBAL', name='Opera WebAI', strategy='브라우저 안에서 로컬 모델을 선택형으로 실행하다',
         facts='Opera는 Opera One·GX·Neon에서 웹사이트와 확장 프로그램이 이용자 기기의 로컬 AI를 호출하는 WebAI 초기 프리뷰를 공개했다. Prompt·Decision·Semantic Embeddings API를 제공하며, 사용자가 설정에서 켜기 전에는 모델이 내려받아지지 않는다.',
         insight='로컬 AI의 장점은 무료가 아니라 데이터 이동·API 비용·운영 책임의 위치를 다시 고를 수 있다는 점이다.',
         source='https://blogs.opera.com/news/2026/10/webai-local-ai-for-the-web-now-in-opera/', image_source='https://www-static-blogs.operacdn.com/news/wp-content/uploads/sites/2/2026/10/image-6.png', image='opera-webai.png', alt='Opera WebAI 로컬 AI 브라우저 기능 공식 이미지'),
    dict(no='05', region='GLOBAL', name='Surge AI DAYJOB: Tax', strategy='전문 업무는 정답률보다 누락·판단·완결성을 평가하다',
         facts='Surge AI는 50개 환경과 1,789개 파일로 세무 에이전트의 전문 업무를 평가하는 DAYJOB: Tax를 공개했다. Claude Sonnet 5.5의 발표 기준 pass@1은 10.8%이며, 통과는 채점 기준의 95% 이상을 충족해야 한다.',
         insight='전문 업무 자동화는 계산 정확도만 보지 말고 중요한 문제를 발견하고 끝까지 완결하는지 측정해야 한다.',
         source='https://surgehq.ai/blog/dayjob-tax', image_source='https://cdn.prod.website-files.com/68dcd2ceb173c46fa029931c/6ae0beffc0ef7d2c805991ec_6ae0bef7bc59db92222e060b_dayjob-tax-cover-v3.png', image='dayjob-tax.png', alt='Surge AI DAYJOB Tax 전문 세무 업무 평가 공식 이미지'),
]

SIGNALS = [
    'AI가 메일·일정·건강정보를 읽을수록 접근 범위와 사용 목적을 먼저 정해야 한다.',
    '보안 특화 모델은 모델 이름보다 초기 사용자·인증·기록·책임 범위를 확인해야 한다.',
    '에이전트 운영의 공통 기반은 모델이 아니라 도구 권한과 실행 로그를 묶는 harness다.',
    '로컬 AI는 데이터 이동·API 비용·기기 성능의 균형을 다시 설계하게 한다.',
    '전문 업무의 자동화 평가는 정답률보다 누락 발견과 최종 검수 가능성을 봐야 한다.',
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
    draw.text((950 if width == 1200 else width-275, 62), '2026.10.29 THU', font=font(21 if width == 1200 else 22), fill=INK)
    draw.line((margin, 125, width-margin, 125), fill=LINE, width=2)

def create_images():
    ROOT.joinpath('assets').mkdir(parents=True, exist_ok=True)
    im = Image.new('RGB', (1200, 630), 'white'); d = ImageDraw.Draw(im); header(d, 1200)
    d.text((70, 160), 'ADDIT DAILY MARKETING BRIEF', font=font(22), fill=RED)
    y = draw_wrap(d, (70, 205), TITLE, font(43), width=1080, gap=4)
    draw_wrap(d, (70, y+18), SUBTITLE, font(20), fill=MUTED, width=1080, gap=3)
    d.rounded_rectangle((70, 535, 1130, 585), radius=25, fill=PINK)
    d.text((95, 547), "TODAY'S TREND, TOMORROW'S STRATEGY.", font=font(20), fill=RED)
    im.save(ROOT / 'assets/og-2026-10-29-v1.png')

    W, H, m = 1080, 1920, 48
    im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im); header(d, W)
    d.text((m, 160), 'ADDIT DAILY MARKETING BRIEF', font=font(19), fill=RED)
    y = draw_wrap(d, (m, 205), TITLE, font(35), width=W-2*m, gap=4)
    draw_wrap(d, (m, y+10), SUBTITLE, font(18), fill=MUTED, width=W-2*m, gap=2); y += 105
    rounded(d, (m, y, W-m, y+104), fill='#FAFAFA'); d.text((m+24, y+18), 'GOOD MORNING, ADDIT', font=font(22), fill=RED)
    draw_wrap(d, (m+24, y+56), '두 원문을 합쳐 중복은 덜고, 바로 적용할 운영 기준을 남겼습니다.', font(19), fill=MUTED, width=W-2*m-48, gap=2); y += 140
    d.text((m, y), "TODAY'S 5 SIGNALS", font=font(20), fill=RED); y += 40
    for i, s in enumerate(SIGNALS, 1):
        by = y + (i-1)*62; rounded(d, (m, by, W-m, by+51), radius=14); d.ellipse((m+12, by+7, m+48, by+43), fill=RED); d.text((m+20, by+13), f'{i:02d}', font=font(14), fill='white'); d.text((m+64, by+13), s, font=font(16), fill=INK)
    y += 5*62 + 24; d.text((m, y), 'CASE STUDY · 1 KR / 4 GLOBAL', font=font(20), fill=RED); y += 42
    for c in CASES:
        bh = 136; rounded(d, (m, y, W-m, y+bh), radius=18); src = Image.open(CASE_DIR / c['image']).convert('RGB'); crop = ImageOps.fit(src, (250, 98), method=Image.Resampling.LANCZOS); im.paste(crop, (m+16, y+19)); d.rounded_rectangle((m+16, y+19, m+266, y+117), radius=12, outline=LINE, width=1)
        d.ellipse((m+292, y+17, m+338, y+63), fill=RED); d.text((m+305, y+25), c['no'], font=font(15), fill='white'); d.text((m+362, y+21), c['name'], font=font(17), fill=INK); draw_wrap(d, (m+292, y+66), c['strategy'], font(13), fill=MUTED, width=650, gap=2); y += bh + 8
    y += 12; rounded(d, (m, y, W-m, y+126), radius=18, fill=PINK, outline='#F1D7DC'); d.text((m+24, y+15), 'ADDIT ACTION CHECK', font=font(20), fill=RED)
    actions = ['접근 가능한 자료와 사용 목적을 분리해 정했는가?', '에이전트 권한·도구·실행 로그를 연결했는가?', '로컬·클라우드 처리의 비용과 책임을 비교했는가?', '전문 업무 결과의 누락과 검수 기준을 정했는가?', '중복 보도와 원문 링크를 구분해 공유했는가?']
    for i, a in enumerate(actions): d.text((m+28, y+48+i*18), '□  '+a, font=font(15), fill=INK)
    y += 150; d.line((m, y, W-m, y), fill=LINE, width=2); d.text((m, y+17), 'AI를 도입할수록,', font=font(20), fill=MUTED); d.text((m, y+51), '자료·권한·검수의 흐름을 설계한다.', font=font(22), fill=INK)
    im.save(ROOT / 'assets/brief-2026-10-29-1080x1920.png')

def esc(value): return html.escape(value, quote=True)
def slug(value): return re.sub(r'[^a-z0-9가-힣]+', '-', value.lower()).strip('-')
def case_html(c):
    ident = slug(c['name'])
    return f'''<article class="case"><a data-case-study="{esc(ident)}" href="{esc(c['source'])}" target="_blank" rel="noopener noreferrer"><img data-source-image="{esc(c['image_source'])}" src="../../assets/case/2026-10-29/{esc(c['image'])}" alt="{esc(c['alt'])}"></a><div><div class="num">{c['no']} · {c['region']}</div><h3>{esc(c['name'])}</h3><p class="strategy">{esc(c['strategy'])}</p><p class="facts">{esc(c['facts'])}</p><a class="source" data-case-study="{ident}-source" href="{esc(c['source'])}" target="_blank" rel="noopener noreferrer">원문 보기 ↗</a></div><div class="insight"><strong>ADDIT INSIGHT</strong><p>{esc(c['insight'])}</p></div></article>'''

def create_html():
    watch = [
        ('ChatGPT + iCloud', '메일·캘린더 연결은 편의와 권한 범위를 함께 확인', 'https://www.aitimes.com/news/articleView.html?idxno=216753'),
        ('Chrome + Gmail', '예약·주문 메일을 양식에 넣기 전 허용 범위 점검', 'https://techcrunch.com/2026/10/28/chromes-ai-powered-autofill-can-now-dig-through-your-gmail-to-fill-out-forms/'),
        ('NVIDIA Nemotron 3.5', '전사·번역·화자 구분을 한 모델로 묶은 음성 인프라', 'https://huggingface.co/blog/nvidia/nemotron-transcribe-granary'),
        ('Microsoft MAI Image 2.7', '생성보다 조명·이미지 속 글자 수정이 차별점', 'https://www.aitimes.com/news/articleView.html?idxno=216755'),
        ('Anthropic 보안 접근', '외부 소프트웨어 권한과 실제 접근 범위를 분리해 읽기', 'https://the-decoder.com/ai-agents-hacked-anthropic-maker-of-arguably-the-most-capable-ai-models-for-cyberdefense/'),
        ('DeepSeek 안전성 시험', '정답률과 종료·감시 요청 준수 여부를 따로 평가', 'https://www.aitimes.com/news/articleView.html?idxno=216738'),
    ]
    watch_html = ''.join(f'<a href="{u}" target="_blank" rel="noopener noreferrer"><b>{esc(n)}</b><span>{esc(d)}</span></a>' for n,d,u in watch)
    old = (BASE / 'work-2026-10-23/archive/2026-10-23/index.html').read_text(encoding='utf-8')
    css = re.search(r'<style>(.*?)</style>', old, re.S).group(1)
    signals_html = ''.join(f'<div class="signal"><b>{i:02d}</b><p>{esc(s)}</p></div>' for i,s in enumerate(SIGNALS, 1))
    cards_html = '\n'.join(case_html(c) for c in CASES)
    html_doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(TITLE)} | Addit Daily Marketing Brief</title><meta name="description" content="{esc(SUBTITLE)}"><link rel="canonical" href="{PAGE_URL}"><link rel="image_src" href="{OG_URL}"><meta name="thumbnail" content="{OG_URL}"><meta property="og:type" content="article"><meta property="og:locale" content="ko_KR"><meta property="og:title" content="{esc(TITLE)}"><meta property="og:description" content="{esc(SUBTITLE)}"><meta property="og:url" content="{SHARE_URL}"><meta property="og:image" content="{OG_URL}"><meta property="og:image:url" content="{OG_URL}"><meta property="og:image:secure_url" content="{OG_URL}"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{esc(TITLE)}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(TITLE)}"><meta name="twitter:image" content="{OG_URL}"><style>{css}</style></head><body><main class="page"><div class="top"></div><div class="wrap"><header class="mast"><div class="brand">addit+</div><div class="date">2026.10.29 THU</div></header><div class="hero"><div class="eyebrow">ADDIT DAILY MARKETING BRIEF</div><h1>AI는 기능이 아니라,<br>자료·권한·검수의 흐름으로 설계된다</h1><p>{esc(SUBTITLE)}</p></div><div class="morning"><strong>GOOD MORNING, ADDIT</strong><p>두 원문을 합쳐 중복은 덜고, 바로 적용할 운영 기준을 남겼습니다.</p></div><section><div class="section-head"><h2>TODAY’S 5 SIGNALS</h2><span>10.29 · AI OPERATING BRIEF</span></div><div class="signals">{signals_html}</div></section><section><div class="section-head"><h2>CASE STUDY</h2><span>1 KR / 4 GLOBAL · 원문 대조 완료</span></div><div class="cases">{cards_html}</div></section><section><div class="section-head"><h2>PLATFORM WATCH</h2><span>두 원문에서 중복 제거 후 남긴 추가 신호</span></div><div class="watch">{watch_html}</div></section><section class="action"><h2>ADDIT ACTION CHECK</h2><ul><li>접근 가능한 자료와 사용 목적을 분리해 정했는가?</li><li>에이전트 권한·도구·실행 로그를 연결했는가?</li><li>로컬·클라우드 처리의 비용과 책임을 비교했는가?</li><li>전문 업무 결과의 누락과 검수 기준을 정했는가?</li><li>중복 보도와 원문 링크를 구분해 공유했는가?</li></ul></section><footer class="footer"><strong>AI를 도입할수록,<br>자료·권한·검수의 흐름을 설계한다.</strong><div class="share"><a href="../../index.html?kakao=20261029-ko-v1">최신호 홈 ↗</a><a href="../../?kakao=20261029-ko-v1">전체 아카이브 ↗</a><a href="../../assets/brief-2026-10-29-1080x1920.png">세로 브리프 이미지 ↗</a></div><div class="credit">TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief · 2026.10.29</div></footer></div></main></body></html>'''
    out = ROOT / 'archive' / '2026-10-29'; out.mkdir(parents=True, exist_ok=True); (out / 'index.html').write_text(html_doc, encoding='utf-8')
    (ROOT / 'index.html').write_text(f'<meta http-equiv="refresh" content="0; url=archive/2026-10-29/index.html?kakao=20261029-ko-v1"><link rel="canonical" href="{PAGE_URL}">', encoding='utf-8')

def create_source():
    lines = ['# Addit Daily Marketing Brief · 2026-10-29', '', '## 한 줄 결론', '', '**AI는 기능이 아니라, 자료·권한·검수의 흐름으로 설계된다.** 두 원문에서 겹친 Gemini 4 Carbon·NVIDIA Nemotron은 한 번만 반영하고, 나머지 고유 이슈를 도입 기준으로 재구성했다.', '', '## 중복 제거 메모', '', '- 공통 기사: Gemini 4 Carbon, NVIDIA Nemotron 3.5 Transcribe.', '- 단일 반영: ChatGPT iCloud 연결, Chrome Gmail 자동 입력, 질병관리청 건강도우미, Microsoft Copilot harness, Opera WebAI, Surge DAYJOB Tax.', '- 유사 주제는 개인정보 연결·보안 접근·실행 기반·로컬 처리·전문 업무 검수의 다섯 흐름으로 묶었다.', '', '## 오늘의 5대 트렌드', '']
    lines += [f'{i}. {s}' for i,s in enumerate(SIGNALS, 1)] + ['', '## CASE STUDY', '']
    for i,c in enumerate(CASES, 1): lines += [f'### {i}. {c["name"]} — {c["strategy"]}', '', '- 지역: ' + c['region'], '- 원문: ' + c['source'], '- 이미지: ' + c['image_source'], '- 확인 사실: ' + c['facts'], '- Addit Insight: ' + c['insight'], '']
    lines += ['## 원문에서 확인한 추가 링크', '', '- ChatGPT + iCloud: https://www.aitimes.com/news/articleView.html?idxno=216753', '- Chrome + Gmail: https://techcrunch.com/2026/10/28/chromes-ai-powered-autofill-can-now-dig-through-your-gmail-to-fill-out-forms/', '- NVIDIA Nemotron 3.5: https://huggingface.co/blog/nvidia/nemotron-transcribe-granary', '- Microsoft MAI Image 2.7: https://www.aitimes.com/news/articleView.html?idxno=216755', '- Anthropic 보안 접근: https://the-decoder.com/ai-agents-hacked-anthropic-maker-of-arguably-the-most-capable-ai-models-for-cyberdefense/', '- DeepSeek 안전성 시험: https://www.aitimes.com/news/articleView.html?idxno=216738', '', '## Addit ACTION CHECK', '', '- 접근 가능한 자료와 사용 목적을 분리해 정했는가?', '- 에이전트 권한·도구·실행 로그를 연결했는가?', '- 로컬·클라우드 처리의 비용과 책임을 비교했는가?', '- 전문 업무 결과의 누락과 검수 기준을 정했는가?', '- 중복 보도와 원문 링크를 구분해 공유했는가?', '', '## 출처 및 검증 메모', '', '- 원문 소스: https://baeksang.dev/daily/2026-10-29 및 https://blog.nextworks.dev/daily/2026-10-29', '- CASE STUDY 5개는 원문 페이지의 제목·핵심 내용·대표 이미지를 직접 대조하고 날짜별 자산으로 보관했다.', '- 지역 편성: 이번 원문은 국내 기관 사례 1건과 글로벌 제품·연구 사례가 중심이어서 1 KR / 4 GLOBAL로 표기했다. 지역 비율을 억지로 바꾸지 않았다.', '- 기사에서 발표된 수치와 편집자의 실행 해석을 분리해 표기했다.']
    (ROOT / 'source').mkdir(exist_ok=True); (ROOT / 'source' / '2026-10-29.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

def create_manifest():
    manifest = {'date':'2026-10-29','title':TITLE,'html':'archive/2026-10-29/index.html','published_url':SHARE_URL,'og_image_path':'assets/og-2026-10-29-v1.png','og_image_url':OG_URL,'cases':[{'name':c['name'],'region':c['region'],'source_url':c['source'],'image_source_url':c['image_source'],'image_local_path':'assets/case/2026-10-29/'+c['image']} for c in CASES]}
    (ROOT / 'brief-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

def create_readme():
    (ROOT / 'README.md').write_text('# MKT_Brief\n\n- [2026.10.29 · AI는 기능이 아니라, 자료·권한·검수의 흐름으로 설계된다](archive/2026-10-29/index.html)\n- [2026.10.28 · AI가 확장될수록, 비용·현장·책임을 함께 설계한다](archive/2026-10-28/index.html)\n- [2026.10.27 · AI가 커질수록, 접근권한과 책임을 먼저 설계한다](archive/2026-10-27/index.html)\n- [2026.10.26 · AI가 커질수록, 성과보다 검증과 통제가 먼저다](archive/2026-10-26/index.html)\n', encoding='utf-8')

def main():
    CASE_DIR.mkdir(parents=True, exist_ok=True)
    for name in ['kdca.jpg','gemini-carbon.png','copilot-harness.png','opera-webai.png','dayjob-tax.png']: shutil.copyfile(RAW / name, CASE_DIR / name)
    create_images(); create_html(); create_source(); create_manifest(); create_readme()

if __name__ == '__main__': main()
