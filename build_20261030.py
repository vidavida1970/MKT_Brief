from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import html, json, re, shutil

BASE = Path('/workspace/scratch/ca3169652574')
ROOT = BASE / 'work-2026-10-30'
CASE_DIR = ROOT / 'assets' / 'case' / '2026-10-30'
RAW = Path('/tmp/mkt30/raw')
FONT = '/workspace/NotoSansKR-Bold.ttf'
RED, INK, MUTED, LINE, PINK = '#E6002D', '#151515', '#5B5B5B', '#E6E6E6', '#FFF1F3'
TITLE = 'AI는 성능을 넘어, 실제 업무에 쓰이는 구조를 만든다'
SUBTITLE = '법률·디자인·제조·보안 현장이 보여준 공통점은 모델 점수가 아니라 연결 방식, 근거 확인, 실행 권한, 현장 배치였습니다.'
PAGE_URL = 'https://vidavida1970.github.io/MKT_Brief/archive/2026-10-30/index.html'
SHARE_URL = PAGE_URL + '?kakao=20261030-ko-v1'
OG_URL = 'https://vidavida1970.github.io/MKT_Brief/assets/og-2026-10-30-v1.png'

CASES = [
    dict(no='01', region='KR', name='미리캔버스 AI 커넥터', strategy='대화형 AI를 실제 디자인 작업공간으로 연결하다',
         facts='미리캔버스 AI 커넥터는 ChatGPT·Claude와 대화하며 프레젠테이션·보고서·제안서 등의 디자인 초안을 만들고, 선택한 템플릿에 결과물을 저장한다. 이후 미리캔버스 에디터에서 편집·다운로드할 수 있어 생성과 실무 마무리가 한 흐름으로 이어진다.',
         insight='AI 활용의 체감은 답변 품질보다 결과물이 저장되고 수정되는 업무 흐름에 달려 있다.',
         source='https://help.miricanvas.com/hc/ko/articles/63391689320601-%EB%AF%B8%EB%A6%AC%EC%BA%94%EB%B2%84%EC%8A%A4-AI-%EC%BB%A4%EB%84%A5%ED%84%B0-%EC%86%8C%EA%B0%9C', image_source='https://image.zdnet.co.kr/2026/10/29/0de54b42a336da61c8c3c5ff96542f54.jpg', image='miricanvas.jpg', alt='미리캔버스 AI 커넥터 디자인 작업 화면'),
    dict(no='02', region='KR', name='클립아트코리아 AI 연결', strategy='대화형 검색을 콘텐츠 자산 탐색으로 확장하다',
         facts='클립아트코리아는 ChatGPT와 Claude에서 자사 스톡 이미지를 검색할 수 있는 AI 연동 서비스를 출시했다. 공식 서비스 안내는 연결·검색에 로그인 없이 사용할 수 있고, AI가 정리한 검색어와 이미지 조건을 전달해 결과를 찾는 방식이라고 설명한다.',
         insight='콘텐츠 플랫폼은 AI를 별도 채팅창으로 만들기보다 이용자가 이미 일하는 대화 안에 검색 자산을 넣어야 한다.',
         source='https://www.clipartkorea.co.kr/service/ai_connect', image_source='https://www.madtimes.co.kr/news/thumbnail/202610/29488_72391_2517_v150.jpg', image='clipart.jpg', alt='클립아트코리아 AI 이미지 검색 서비스 소개 이미지'),
    dict(no='03', region='KR', name='중소제조 피지컬 AI 확산 전략', strategy='DX·AX·RX를 제조 현장 배치로 연결하다',
         facts='정부는 2030년까지 스마트제조혁신에 5조 원 이상을 투입해 중소기업의 디지털 전환율을 30%에서 50%, AI 도입률을 1%에서 10%로 높이는 전략을 발표했다. 데이터·AI·로봇 전환을 묶어 중소 제조현장을 피지컬 AI의 실증 무대로 삼는 계획이다.',
         insight='피지컬 AI는 데모를 늘리는 것보다 현장 데이터와 인력 교육, 안전 기준을 함께 배치할 때 산업 전환이 된다.',
         source='https://www.korea.kr/news/policyNewsView.do?newsId=148974541', image_source='https://www.korea.kr/newsWeb/resources/attaches/2026.10/29/6780e9a2267970448a044d54ffc69f7a.jpg', image='physical.jpg', alt='중소 제조현장 피지컬 AI 확산 전략 대표 이미지'),
    dict(no='04', region='GLOBAL', name='Claude for Legal Artifacts', strategy='법률 AI에 결과보다 근거와 재사용 구조를 붙이다',
         facts='Anthropic은 계약 검토, 규제 변화 추적, 법률 요청 접수, 인용 확인 등을 위한 재사용형 Artifacts 갤러리를 공개했다. 계약 조항을 표로 정리할 때 각 답변을 원문 문구와 연결하고, 법률팀이 자체 자료·커넥터에 맞게 수정·공유할 수 있도록 설계했다.',
         insight='고위험 전문 업무에서 AI의 첫 결과는 결론이 아니라 근거 링크와 사람이 검토할 수 있는 작업판이어야 한다.',
         source='https://claude.com/ko/resources/articles/introducing-artifacts-for-legal-work', image_source='https://claude.com/ko/resources/articles/introducing-artifacts-for-legal-work/opengraph-image/og', image='claude-legal.png', alt='Claude for Legal Artifacts 공식 발표 이미지'),
    dict(no='05', region='GLOBAL', name='SentinelOne × Claude Mythos 5.1', strategy='AI가 찾은 취약점을 실제 위험 순서로 좁히다',
         facts='SentinelOne은 Wayfinder Frontier AI Services에 Anthropic Claude Mythos 5.1을 추가한다고 발표했다. 인간 보안 전문가와 frontier 모델이 취약점을 찾은 뒤 실제 악용 가능성을 검증하고, 고객이 먼저 고칠 위험을 우선순위로 제시하는 방식이다.',
         insight='AI 보안의 생산성은 발견 건수보다 실제로 닫아야 할 위험을 좁혀주는 triage 품질로 판단해야 한다.',
         source='https://www.sentinelone.com/press/sentinelone-to-add-anthropic-s-claude-mythos-5-1-to-wayfinder-frontier-ai-services/', image_source='https://content-media.investing.com/news/SentinelOne_800x533_L_1625147631.jpg', image='sentinelone.jpg', alt='SentinelOne Claude Mythos 5.1 발표 관련 대표 이미지'),
]

SIGNALS = [
    'AI 경쟁의 기준이 모델 점수에서 비용·생산성·검수 시간으로 이동한다.',
    '대화형 AI의 다음 단계는 답변이 아니라 디자인·법률·콘텐츠 자산으로의 연결이다.',
    '사칭 앱과 채굴 악성코드는 기업 AI 도구 관리와 설치 경로를 보안 항목으로 만든다.',
    '전문 업무에서는 생성 결과보다 원문 근거·권한·사람의 최종 판단이 중요하다.',
    '피지컬 AI는 데모 경쟁을 넘어 제조 데이터·로봇·교육·현장 배치 경쟁으로 들어섰다.',
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
    draw.text((950 if width == 1200 else width-275, 62), '2026.10.30 FRI', font=font(21 if width == 1200 else 22), fill=INK)
    draw.line((margin, 125, width-margin, 125), fill=LINE, width=2)

def create_images():
    ROOT.joinpath('assets').mkdir(parents=True, exist_ok=True)
    im = Image.new('RGB', (1200, 630), 'white'); d = ImageDraw.Draw(im); header(d, 1200)
    d.text((70, 160), 'ADDIT DAILY MARKETING BRIEF', font=font(22), fill=RED)
    y = draw_wrap(d, (70, 205), TITLE, font(43), width=1080, gap=4)
    draw_wrap(d, (70, y+18), SUBTITLE, font(20), fill=MUTED, width=1080, gap=3)
    d.rounded_rectangle((70, 535, 1130, 585), radius=25, fill=PINK)
    d.text((95, 547), "TODAY'S TREND, TOMORROW'S STRATEGY.", font=font(20), fill=RED)
    im.save(ROOT / 'assets/og-2026-10-30-v1.png')

    W, H, m = 1080, 1920, 48
    im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im); header(d, W)
    d.text((m, 160), 'ADDIT DAILY MARKETING BRIEF', font=font(19), fill=RED)
    y = draw_wrap(d, (m, 205), TITLE, font(35), width=W-2*m, gap=4)
    draw_wrap(d, (m, y+10), SUBTITLE, font(18), fill=MUTED, width=W-2*m, gap=2); y += 105
    rounded(d, (m, y, W-m, y+104), fill='#FAFAFA'); d.text((m+24, y+18), 'GOOD MORNING, ADDIT', font=font(22), fill=RED)
    draw_wrap(d, (m+24, y+56), '오늘은 성능보다 실제 업무에 연결되는 구조를 살펴봅니다.', font(19), fill=MUTED, width=W-2*m-48, gap=2); y += 140
    d.text((m, y), "TODAY'S 5 SIGNALS", font=font(20), fill=RED); y += 40
    for i, s in enumerate(SIGNALS, 1):
        by = y + (i-1)*62; rounded(d, (m, by, W-m, by+51), radius=14); d.ellipse((m+12, by+7, m+48, by+43), fill=RED); d.text((m+20, by+13), f'{i:02d}', font=font(14), fill='white'); d.text((m+64, by+13), s, font=font(16), fill=INK)
    y += 5*62 + 24; d.text((m, y), 'CASE STUDY · 3 KR / 2 GLOBAL', font=font(20), fill=RED); y += 42
    for c in CASES:
        bh = 136; rounded(d, (m, y, W-m, y+bh), radius=18); src = Image.open(CASE_DIR / c['image']).convert('RGB'); crop = ImageOps.fit(src, (250, 98), method=Image.Resampling.LANCZOS); im.paste(crop, (m+16, y+19)); d.rounded_rectangle((m+16, y+19, m+266, y+117), radius=12, outline=LINE, width=1)
        d.ellipse((m+292, y+17, m+338, y+63), fill=RED); d.text((m+305, y+25), c['no'], font=font(15), fill='white'); d.text((m+362, y+21), c['name'], font=font(17), fill=INK); draw_wrap(d, (m+292, y+66), c['strategy'], font(13), fill=MUTED, width=650, gap=2); y += bh + 8
    y += 12; rounded(d, (m, y, W-m, y+126), radius=18, fill=PINK, outline='#F1D7DC'); d.text((m+24, y+15), 'ADDIT ACTION CHECK', font=font(20), fill=RED)
    actions = ['AI 도구가 실제 업무공간에 저장·수정되도록 연결했는가?', '출처·근거·원문 링크를 결과와 함께 남겼는가?', '사칭 앱·설치 경로·권한을 점검했는가?', '작업당 비용과 검수 시간을 계산했는가?', '현장 배치 전 데이터·교육·안전 기준을 정했는가?']
    for i, a in enumerate(actions): d.text((m+28, y+48+i*18), '□  '+a, font=font(15), fill=INK)
    y += 150; d.line((m, y, W-m, y), fill=LINE, width=2); d.text((m, y+17), 'AI를 잘 쓰는 조직은,', font=font(20), fill=MUTED); d.text((m, y+51), '결과보다 연결 구조를 설계한다.', font=font(22), fill=INK)
    im.save(ROOT / 'assets/brief-2026-10-30-1080x1920.png')

def esc(value): return html.escape(value, quote=True)
def slug(value): return re.sub(r'[^a-z0-9가-힣]+', '-', value.lower()).strip('-')
def case_html(c):
    ident = slug(c['name'])
    return f'''<article class="case"><a data-case-study="{esc(ident)}" href="{esc(c['source'])}" target="_blank" rel="noopener noreferrer"><img data-source-image="{esc(c['image_source'])}" src="../../assets/case/2026-10-30/{esc(c['image'])}" alt="{esc(c['alt'])}"></a><div><div class="num">{c['no']} · {c['region']}</div><h3>{esc(c['name'])}</h3><p class="strategy">{esc(c['strategy'])}</p><p class="facts">{esc(c['facts'])}</p><a class="source" data-case-study="{ident}-source" href="{esc(c['source'])}" target="_blank" rel="noopener noreferrer">원문 보기 ↗</a></div><div class="insight"><strong>ADDIT INSIGHT</strong><p>{esc(c['insight'])}</p></div></article>'''

def create_html():
    watch = [
        ('Claude Duet', '미국 Max 우선 출시 후 Pro 확대 예정', 'https://www.orcarouter.ai/ko/blog/claude-duet-rollout-max-first-pro-next'),
        ('ChatGPT 통합', '대화·업무 기능을 연내 하나의 흐름으로 통합', 'https://www.aitimes.com/news/articleView.html?idxno=216804'),
        ('Gemini 4 Carbon', '사이버 보안 담당자부터 단계적 제공', 'https://www.unite.ai/ko/staged-rollout-sends-googles-gemini-4-carbon-to-cyber-defenders-first/'),
        ('AI 사칭 악성코드', '공식 앱처럼 보이는 설치 파일과 채굴 악성코드 주의', 'https://www.cio.com/article/4241962/%EC%B1%97gpt-%ED%81%B4%EB%A1%9C%EB%93%9C-%EC%82%AC%EC%B9%AD-%EC%B1%84%EA%B5%B4-%EC%95%85%EC%84%B1%EC%BD%94%EB%93%9C.html'),
        ('AI 가성비·생산성', '성능보다 작업당 비용과 결과물 생산성 측정', 'https://www.yna.co.kr/view/AKR20261029040600017'),
        ('의료 AI', '건강 정보는 참고와 진료 판단을 구분', 'https://www.dailymedi.com/news/news_view.php?wr_id=941663'),
    ]
    watch_html = ''.join(f'<a href="{u}" target="_blank" rel="noopener noreferrer"><b>{esc(n)}</b><span>{esc(d)}</span></a>' for n,d,u in watch)
    css_source = Path('/tmp/mkt30-repo/archive/2026-10-29/index.html')
    css = re.search(r'<style>(.*?)</style>', css_source.read_text(encoding='utf-8'), re.S).group(1)
    signals_html = ''.join(f'<div class="signal"><b>{i:02d}</b><p>{esc(s)}</p></div>' for i,s in enumerate(SIGNALS, 1))
    cards_html = '\n'.join(case_html(c) for c in CASES)
    html_doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(TITLE)} | Addit Daily Marketing Brief</title><meta name="description" content="{esc(SUBTITLE)}"><link rel="canonical" href="{PAGE_URL}"><link rel="image_src" href="{OG_URL}"><meta name="thumbnail" content="{OG_URL}"><meta property="og:type" content="article"><meta property="og:locale" content="ko_KR"><meta property="og:title" content="{esc(TITLE)}"><meta property="og:description" content="{esc(SUBTITLE)}"><meta property="og:url" content="{SHARE_URL}"><meta property="og:image" content="{OG_URL}"><meta property="og:image:url" content="{OG_URL}"><meta property="og:image:secure_url" content="{OG_URL}"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{esc(TITLE)}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(TITLE)}"><meta name="twitter:image" content="{OG_URL}"><style>{css}</style></head><body><main class="page"><div class="top"></div><div class="wrap"><header class="mast"><div class="brand">addit+</div><div class="date">2026.10.30 FRI</div></header><div class="hero"><div class="eyebrow">ADDIT DAILY MARKETING BRIEF</div><h1>AI는 성능을 넘어,<br>실제 업무에 쓰이는 구조를 만든다</h1><p>{esc(SUBTITLE)}</p></div><div class="morning"><strong>GOOD MORNING, ADDIT</strong><p>오늘은 성능보다 실제 업무에 연결되는 구조를 살펴봅니다.</p></div><section><div class="section-head"><h2>TODAY’S 5 SIGNALS</h2><span>10.30 · AI OPERATING BRIEF</span></div><div class="signals">{signals_html}</div></section><section><div class="section-head"><h2>CASE STUDY</h2><span>3 KR / 2 GLOBAL · 원문 대조 완료</span></div><div class="cases">{cards_html}</div></section><section><div class="section-head"><h2>PLATFORM WATCH</h2><span>오늘 원고에서 확인한 추가 신호</span></div><div class="watch">{watch_html}</div></section><section class="action"><h2>ADDIT ACTION CHECK</h2><ul><li>AI 도구가 실제 업무공간에 저장·수정되도록 연결했는가?</li><li>출처·근거·원문 링크를 결과와 함께 남겼는가?</li><li>사칭 앱·설치 경로·권한을 점검했는가?</li><li>작업당 비용과 검수 시간을 계산했는가?</li><li>현장 배치 전 데이터·교육·안전 기준을 정했는가?</li></ul></section><footer class="footer"><strong>AI를 잘 쓰는 조직은,<br>결과보다 연결 구조를 설계한다.</strong><div class="share"><a href="../../index.html?kakao=20261030-ko-v1">최신호 홈 ↗</a><a href="../../?kakao=20261030-ko-v1">전체 아카이브 ↗</a><a href="../../assets/brief-2026-10-30-1080x1920.png">세로 브리프 이미지 ↗</a></div><div class="credit">TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief · 2026.10.30</div></footer></div></main></body></html>'''
    out = ROOT / 'archive' / '2026-10-30'; out.mkdir(parents=True, exist_ok=True); (out / 'index.html').write_text(html_doc, encoding='utf-8')
    (ROOT / 'index.html').write_text(f'<meta http-equiv="refresh" content="0; url=archive/2026-10-30/index.html?kakao=20261030-ko-v1"><link rel="canonical" href="{PAGE_URL}">', encoding='utf-8')

def create_source():
    lines = ['# Addit Daily Marketing Brief · 2026-10-30', '', '## 한 줄 결론', '', '**AI는 성능을 넘어, 실제 업무에 쓰이는 구조를 만든다.** 법률·디자인·제조·보안 사례를 연결해 비용·근거·권한·현장 배치라는 실행 기준으로 재구성했다.', '', '## 오늘의 5대 트렌드', '']
    lines += [f'{i}. {s}' for i,s in enumerate(SIGNALS, 1)] + ['', '## CASE STUDY', '']
    for i,c in enumerate(CASES, 1): lines += [f'### {i}. {c["name"]} — {c["strategy"]}', '', '- 지역: ' + c['region'], '- 원문: ' + c['source'], '- 이미지: ' + c['image_source'], '- 확인 사실: ' + c['facts'], '- Addit Insight: ' + c['insight'], '']
    lines += ['## 중복·연속 이슈 편집 메모', '', '- 제미나이 4 카본은 전날 모델 공개 이슈와 연속되므로 이번 호에서는 보안 담당자 우선 단계적 출시라는 접근 정책만 업데이트했다.', '- 클로드·챗GPT 사칭 악성코드는 기능 뉴스와 분리해 기업 AI 도구 관리·설치 경로 점검 신호로 배치했다.', '- AI 경쟁 가성비 논쟁은 사례 카드가 아닌 전체 트렌드의 공통 축으로 반영했다.', '', '## 원고에서 확인한 추가 링크', '', '- Claude Duet: https://www.orcarouter.ai/ko/blog/claude-duet-rollout-max-first-pro-next', '- ChatGPT 통합: https://www.aitimes.com/news/articleView.html?idxno=216804', '- Gemini 4 Carbon 단계적 출시: https://www.unite.ai/ko/staged-rollout-sends-googles-gemini-4-carbon-to-cyber-defenders-first/', '- AI 사칭 악성코드: https://www.cio.com/article/4241962/%EC%B1%97gpt-%ED%81%B4%EB%A1%9C%EB%93%9C-%EC%82%AC%EC%B9%AD-%EC%B1%84%EA%B5%B4-%EC%95%85%EC%84%B1%EC%BD%94%EB%93%9C.html', '- AI 가성비·생산성: https://www.yna.co.kr/view/AKR20261029040600017', '- 중소제조 피지컬 AI: https://www.korea.kr/news/policyNewsView.do?newsId=148974541', '', '## Addit ACTION CHECK', '', '- AI 도구가 실제 업무공간에 저장·수정되도록 연결했는가?', '- 출처·근거·원문 링크를 결과와 함께 남겼는가?', '- 사칭 앱·설치 경로·권한을 점검했는가?', '- 작업당 비용과 검수 시간을 계산했는가?', '- 현장 배치 전 데이터·교육·안전 기준을 정했는가?', '', '## 출처 및 검증 메모', '', '- 원고: 사용자가 제공한 AI 뉴스 브리핑 | 2026-10-30.', '- 공식·기관 원문을 우선해 CASE STUDY를 재검증했다.', '- CASE STUDY 지역 편성은 3 KR / 2 GLOBAL이며, 직전 호의 1 KR / 4 GLOBAL과 합산하면 4 KR / 6 GLOBAL이다. 이번 호는 원고에서 실제로 확인 가능한 국내 실행 사례를 우선 반영했다.', '- 기사에서 발표된 수치와 편집자의 실행 해석을 분리해 표기했다.']
    (ROOT / 'source').mkdir(exist_ok=True); (ROOT / 'source' / '2026-10-30.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

def create_manifest():
    manifest = {'date':'2026-10-30','title':TITLE,'html':'archive/2026-10-30/index.html','published_url':SHARE_URL,'og_image_path':'assets/og-2026-10-30-v1.png','og_image_url':OG_URL,'cases':[{'name':c['name'],'region':c['region'],'source_url':c['source'],'image_source_url':c['image_source'],'image_local_path':'assets/case/2026-10-30/'+c['image']} for c in CASES]}
    (ROOT / 'brief-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

def create_readme():
    (ROOT / 'README.md').write_text('# MKT_Brief\n\n- [2026.10.30 · AI는 성능을 넘어, 실제 업무에 쓰이는 구조를 만든다](archive/2026-10-30/index.html)\n- [2026.10.29 · AI는 기능이 아니라, 자료·권한·검수의 흐름으로 설계된다](archive/2026-10-29/index.html)\n- [2026.10.28 · AI가 확장될수록, 비용·현장·책임을 함께 설계한다](archive/2026-10-28/index.html)\n- [2026.10.27 · AI가 커질수록, 접근권한과 책임을 먼저 설계한다](archive/2026-10-27/index.html)\n', encoding='utf-8')

def main():
    CASE_DIR.mkdir(parents=True, exist_ok=True)
    for name in ['claude-legal.png','clipart.jpg','miricanvas.jpg','physical.jpg','sentinelone.jpg']: shutil.copyfile(RAW / name, CASE_DIR / name)
    create_images(); create_html(); create_source(); create_manifest(); create_readme()

if __name__ == '__main__': main()
