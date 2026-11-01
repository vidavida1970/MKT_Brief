from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import html, json, re, shutil

BASE = Path('/workspace/scratch/ca3169652574')
ROOT = Path('/workspace/scratch/ca3169652574/mkt-repo-20261102')
CASE_DIR = ROOT / 'assets' / 'case' / '2026-11-02'
RAW = ROOT
FONT = '/tmp/NotoSansCJKkr-Bold.otf'
RED, INK, MUTED, LINE, PINK = '#E6002D', '#151515', '#5B5B5B', '#E6E6E6', '#FFF1F3'
TITLE = 'AI를 잘 쓰는 조직은 한도·검수·책임을 먼저 설계한다'
SUBTITLE = '오늘의 뉴스는 AI가 더 많은 일을 하는 만큼 사용량의 기준, 결과 검증, 운영 주체의 책임을 함께 정해야 한다는 사실을 보여줍니다.'
PAGE_URL = 'https://vidavida1970.github.io/MKT_Brief/archive/2026-11-02/index.html'
SHARE_URL = PAGE_URL + '?kakao=20261102-ko-v1'
OG_URL = 'https://vidavida1970.github.io/MKT_Brief/assets/og-2026-11-02-v1.png'

CASES = [
    dict(no='01', region='KR', name='삼성SDS Shadow AI 조사', strategy='개인의 AI 사용을 안전한 기업 인프라로 전환하다',
         facts='삼성SDS는 국내 기업·공공기관 재직자 1,750명 조사에서 업무용 GenAI가 일상 업무 인프라로 확장됐다고 분석했다. 승인 없이 개인 비용으로 쓰는 Shadow AI 비중도 38%로 제시하며, 데이터 연결·자동화·보안·거버넌스를 갖춘 Enterprise AI 환경을 대안으로 설명한다.',
         insight='사용을 막는 정책보다 안전한 공식 도구와 데이터 경로를 먼저 제공해야 Shadow AI를 줄일 수 있다.',
         source='https://www.samsungsds.com/kr/insights/enterprise-genai-usage-survey_part1.html', image_source='https://image.samsungsds.com/kr/insights/__icsFiles/afieldfile/2026/07/30/02_INSIGHT_03_Thumb_list_2.png?queryString=20261022095632', image='samsung-sds.png', alt='삼성SDS 국내 기업 GenAI 활용 실태 대표 이미지'),
    dict(no='02', region='KR', name='KOTRA AI 무역인재양성', strategy='AI 교육을 수출 콘텐츠와 바이어 발굴로 연결하다',
         facts='KOTRA AI 무역지원센터는 참가기업과 취·창업 준비생을 매칭해 9주 동안 AI 활용 수출상품 콘텐츠 제작, 온라인 등록, SNS 캠페인, 바이어 발굴을 실습한다. 기업이 교육을 듣는 데서 끝나지 않고 실제 상품·시장·교신 과제로 이어지는 구조다.',
         insight='AI 교육의 성과는 수료 인원보다 현장에서 완성된 콘텐츠와 다음 영업 행동으로 측정해야 한다.',
         source='https://www.kotra.or.kr/subList/20000020753/subhome/bizAply/selectBizMntInfoDetail.do?cpbizYn=N&dtlBizMntNo=26ED00N', image_source='https://www.kotra.or.kr:443/module/upload/file/selectImageView.do?atchFileId=40000041484&fileSn=0', image='kotra.png', alt='KOTRA AI 무역인재양성 공식 이미지'),
    dict(no='03', region='KR', name='AI 법령 비서', strategy='공공 데이터를 업무 검토 단계에 연결하다',
         facts='법제처·행정안전부·과학기술정보통신부가 공무원이 직접 만든 AI 법령 비서를 시범 운영했다. 법령·행정규칙·판례 등 자료를 검색해 법적 질문에 답하지만, AI 답변은 최종 법적 판단이 아니라 공무원의 중간 검토자료로 한정한다.',
         insight='전문 영역의 AI는 자동 결론보다 검색 근거와 검토자의 책임 범위를 함께 설계해야 한다.',
         source='https://m.korea.kr/multi/visualNewsView.do?newsId=148968063&pWise=mSub&pWiseSub=RT1', image_source='https://www.korea.kr/newsWeb/resources/attaches/2026.07/13/97149bca70b70437dbb78cd63853f89d.jpg', image='ai-law-assistant.jpg', alt='공무원이 직접 만든 AI 법령 비서 공식 이미지'),
    dict(no='04', region='KR', name='AWS 한국 AI 잠재력 리포트', strategy='도입률을 현장 생산성과 에이전트로 확장하다',
         facts='AWS가 의뢰한 2026년 한국 AI 잠재력 조사에서 국내 기업 AI 도입률이 48%에서 58%로 늘었다고 보도됐다. 신한금융그룹은 Amazon Bedrock AgentCore 기반 시스템으로 고객 의도 분류 챗봇을 운영 중인 사례로 소개됐으며, 도입 이후에는 정확도·비용·응답시간을 함께 관리하는 기준이 필요하다.',
         insight='AI 도입률 자체보다 업무별 정확도, 운영비, 응답시간을 묶어 성과지표로 만들어야 다음 투자가 설득력을 얻는다.',
         source='https://www3.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02177926645580120', image_source='https://image.edaily.co.kr/images/Photo/files/NP/S/2026/09/PS26091400228.jpg', image='edaily-ai.png', alt='AWS 2026년 한국 AI 잠재력 리포트 발표 이미지'),
    dict(no='05', region='GLOBAL', name='OpenAI ChatGPT·Codex 공통 한도', strategy='대화와 에이전트 작업을 하나의 사용량 예산으로 관리하다',
         facts='OpenAI는 12월부터 Plus·Pro·Business의 ChatGPT와 Codex 사용 한도를 공유한다고 안내했다. 모델과 작업의 복잡도에 따라 사용량이 달라지고, 즉시 응답 대화는 사용량에서 차감하지 않는 방식으로 설명돼 단순 채팅과 에이전트 작업의 비용 구조가 달라진다.',
         insight='AI 예산은 메시지 수가 아니라 모델·작업 유형·결과 검수까지 포함한 업무 단위로 관리해야 한다.',
         source='https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits', image_source='https://help.openai.com/og-image.png', image='openai-og.png', alt='OpenAI ChatGPT와 Codex 사용 한도 공식 안내 이미지'),
]

SIGNALS = [
    'ChatGPT와 Codex가 한도를 공유하며 AI 사용량이 업무 예산이 된다.',
    '청소년 안전·게임 복제 제한처럼 AI의 경계가 대화 안에서 작동한다.',
    'AI 에이전트가 대신 실행해도 승인·기록·책임은 운영 조직에 남는다.',
    '법률 문서와 연구 결과는 초안 생성보다 사람의 검증 비용이 핵심이 된다.',
    '오프라인 음성 도구처럼 데이터가 내 기기에 남는 AI 선택지가 넓어진다.',
]

SOURCE_ITEMS = [
    ('ChatGPT 유료 계정 제한', '기기·결제 카드별 유료 계정 수 제한 관련 원문', 'https://the-decoder.com/openai-is-steering-chatgpt-users-toward-more-paid-usage/'),
    ('청소년 ChatGPT 안전조치', '무기 정보 제한과 폭력 징후 대화 중단', 'https://www.aitimes.com/news/articleView.html?idxno=216847'),
    ('Claude Code 게임 복제 제한', '기존 게임 복제 제한과 정상 작업 차단 논란', 'https://www.aitimes.com/news/articleView.html?idxno=216862'),
    ('영국 AI 에이전트 책임', '운영 기업의 법적 책임을 다룬 규제기관 공동 입장', 'https://www.aitimes.kr/news/articleView.html?idxno=42523'),
    ('호주 빅토리아 변호사 조사', 'AI 활용 증가와 문서 검증 부담', 'https://www.aitimes.kr/news/articleView.html?idxno=42524'),
    ('ChatGPT·Codex 공통 한도', '12월부터 대화와 Codex 사용량 공유', 'https://the-decoder.com/openais-upcoming-chat-and-work-merger-in-chatgpt-signals-the-end-of-all-you-can-prompt-pricing/'),
    ('AI 정치적 답변 연구', '질문 언어가 모델 답변에 미치는 영향', 'https://the-decoder.com/chinese-ai-models-are-politically-complex-not-just-government-mouthpieces-study-finds/'),
    ('앤트로픽 안전성 연구', '소설처럼 보이는 학습 자료와 정렬 실패', 'https://www.aitimes.com/news/articleView.html?idxno=216859'),
    ('Gemini Notebook 무료 교재', '미국·인도 지역 무료 교재 수백 권 추가', 'https://www.aitimes.com/news/articleView.html?idxno=216863'),
    ('Hex', 'Mac·Windows·Linux 오프라인 음성 받아쓰기', 'https://github.com/anomalyco/hex'),
    ('HackerBooks', 'Hacker News 책 언급과 댓글 탐색 서비스', 'https://hackerbooks.org/'),
    ('Handy', '무료·오프라인 음성 받아쓰기 도구', 'https://github.com/cjpais/Handy'),
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
    draw.text((950 if width == 1200 else width-275, 62), '2026.11.02 MON', font=font(21 if width == 1200 else 22), fill=INK)
    draw.line((margin, 125, width-margin, 125), fill=LINE, width=2)

def create_images():
    ROOT.joinpath('assets').mkdir(parents=True, exist_ok=True)
    im = Image.new('RGB', (1200, 630), 'white'); d = ImageDraw.Draw(im); header(d, 1200)
    d.text((70, 160), 'ADDIT DAILY MARKETING BRIEF', font=font(22), fill=RED)
    y = draw_wrap(d, (70, 205), TITLE, font(43), width=1080, gap=4)
    draw_wrap(d, (70, y+18), SUBTITLE, font(20), fill=MUTED, width=1080, gap=3)
    d.rounded_rectangle((70, 535, 1130, 585), radius=25, fill=PINK)
    d.text((95, 547), "TODAY'S TREND, TOMORROW'S STRATEGY.", font=font(20), fill=RED)
    im.save(ROOT / 'assets/og-2026-11-02-v1.png')

    W, H, m = 1080, 1920, 48
    im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im); header(d, W)
    d.text((m, 160), 'ADDIT DAILY MARKETING BRIEF', font=font(19), fill=RED)
    y = draw_wrap(d, (m, 205), TITLE, font(35), width=W-2*m, gap=4)
    draw_wrap(d, (m, y+10), SUBTITLE, font(18), fill=MUTED, width=W-2*m, gap=2); y += 105
    rounded(d, (m, y, W-m, y+104), fill='#FAFAFA'); d.text((m+24, y+18), 'GOOD MORNING, ADDIT', font=font(22), fill=RED)
    draw_wrap(d, (m+24, y+56), '오늘은 AI를 도입하기 전에 사용량과 검수·책임의 구조를 살펴봅니다.', font(19), fill=MUTED, width=W-2*m-48, gap=2); y += 140
    d.text((m, y), "TODAY'S 5 SIGNALS", font=font(20), fill=RED); y += 40
    for i, s in enumerate(SIGNALS, 1):
        by = y + (i-1)*62; rounded(d, (m, by, W-m, by+51), radius=14); d.ellipse((m+12, by+7, m+48, by+43), fill=RED); d.text((m+20, by+13), f'{i:02d}', font=font(14), fill='white'); d.text((m+64, by+13), s, font=font(16), fill=INK)
    y += 5*62 + 24; d.text((m, y), 'CASE STUDY · 4 KR / 1 GLOBAL', font=font(20), fill=RED); y += 42
    for c in CASES:
        bh = 136; rounded(d, (m, y, W-m, y+bh), radius=18); src = Image.open(CASE_DIR / c['image']).convert('RGB'); crop = ImageOps.fit(src, (250, 98), method=Image.Resampling.LANCZOS); im.paste(crop, (m+16, y+19)); d.rounded_rectangle((m+16, y+19, m+266, y+117), radius=12, outline=LINE, width=1)
        d.ellipse((m+292, y+17, m+338, y+63), fill=RED); d.text((m+305, y+25), c['no'], font=font(15), fill='white'); d.text((m+362, y+21), c['name'], font=font(17), fill=INK); draw_wrap(d, (m+292, y+66), c['strategy'], font(13), fill=MUTED, width=650, gap=2); y += bh + 8
    y += 12; rounded(d, (m, y, W-m, y+170), radius=18, fill=PINK, outline='#F1D7DC'); d.text((m+24, y+15), 'ADDIT ACTION CHECK', font=font(20), fill=RED)
    actions = ['사용량을 업무 단위로 관리하는가?', '원문 근거와 검수자를 남겼는가?', '권한과 중단 조건을 정했는가?', '공식 도구·데이터 경로를 제공했는가?', '오프라인 처리와 보안 책임을 점검했는가?']
    for i, a in enumerate(actions): d.text((m+28, y+50+i*22), '□  '+a, font=font(15), fill=INK)
    y += 194; d.line((m, y, W-m, y), fill=LINE, width=2); d.text((m, y+17), 'AI를 잘 쓰는 조직은,', font=font(20), fill=MUTED); d.text((m, y+51), '더 똑똑한 답보다 더 분명한 책임을 설계한다.', font=font(22), fill=INK)
    im.save(ROOT / 'assets/brief-2026-11-02-1080x1920.png')

def esc(value): return html.escape(value, quote=True)
def slug(value): return re.sub(r'[^a-z0-9가-힣]+', '-', value.lower()).strip('-')
def case_html(c):
    ident = slug(c['name'])
    return f'''<article class="case"><a data-case-study="{esc(ident)}" href="{esc(c['source'])}" target="_blank" rel="noopener noreferrer"><img data-source-image="{esc(c['image_source'])}" src="../../assets/case/2026-11-02/{esc(c['image'])}" alt="{esc(c['alt'])}"></a><div><div class="num">{c['no']} · {c['region']}</div><h3>{esc(c['name'])}</h3><p class="strategy">{esc(c['strategy'])}</p><p class="facts">{esc(c['facts'])}</p><a class="source" data-case-study="{ident}-source" href="{esc(c['source'])}" target="_blank" rel="noopener noreferrer">원문 보기 ↗</a></div><div class="insight"><strong>ADDIT INSIGHT</strong><p>{esc(c['insight'])}</p></div></article>'''

def create_html():
    watch_html = ''.join(f'<a href="{u}" target="_blank" rel="noopener noreferrer"><b>{esc(n)}</b><span>{esc(d)}</span></a>' for n,d,u in SOURCE_ITEMS)
    css_source = ROOT / 'archive' / '2026-10-30' / 'index.html'
    css = re.search(r'<style>(.*?)</style>', css_source.read_text(encoding='utf-8'), re.S).group(1)
    signals_html = ''.join(f'<div class="signal"><b>{i:02d}</b><p>{esc(s)}</p></div>' for i,s in enumerate(SIGNALS, 1))
    cards_html = '\n'.join(case_html(c) for c in CASES)
    html_doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(TITLE)} | Addit Daily Marketing Brief</title><meta name="description" content="{esc(SUBTITLE)}"><link rel="canonical" href="{PAGE_URL}"><link rel="image_src" href="{OG_URL}"><meta name="thumbnail" content="{OG_URL}"><meta property="og:type" content="article"><meta property="og:locale" content="ko_KR"><meta property="og:title" content="{esc(TITLE)}"><meta property="og:description" content="{esc(SUBTITLE)}"><meta property="og:url" content="{SHARE_URL}"><meta property="og:image" content="{OG_URL}"><meta property="og:image:url" content="{OG_URL}"><meta property="og:image:secure_url" content="{OG_URL}"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{esc(TITLE)}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(TITLE)}"><meta name="twitter:image" content="{OG_URL}"><style>{css}</style></head><body><main class="page"><div class="top"></div><div class="wrap"><header class="mast"><div class="brand">addit+</div><div class="date">2026.11.02 MON</div></header><div class="hero"><div class="eyebrow">ADDIT DAILY MARKETING BRIEF</div><h1>AI를 잘 쓰는 조직은<br>한도·검수·책임을 먼저 설계한다</h1><p>{esc(SUBTITLE)}</p></div><div class="morning"><strong>GOOD MORNING, ADDIT</strong><p>오늘은 AI를 도입하기 전에 사용량과 검수·책임의 구조를 살펴봅니다.</p></div><section><div class="section-head"><h2>TODAY’S 5 SIGNALS</h2><span>11.02 · AI OPERATING BRIEF</span></div><div class="signals">{signals_html}</div></section><section><div class="section-head"><h2>CASE STUDY</h2><span>4 KR / 1 GLOBAL · 원문 대조 완료</span></div><div class="cases">{cards_html}</div></section><section><div class="section-head"><h2>SOURCE CHECK</h2><span>baeksang.dev 12건 원문 검수</span></div><div class="watch">{watch_html}</div></section><section class="action"><h2>ADDIT ACTION CHECK</h2><ul><li>사용량을 메시지 수가 아닌 업무 단위로 관리하는가?</li><li>AI 결과의 원문 근거와 사람의 검수자를 남겼는가?</li><li>에이전트가 실행할 수 있는 권한과 중단 조건을 정했는가?</li><li>Shadow AI 대신 공식 도구·데이터 경로를 제공했는가?</li><li>오프라인 처리와 업데이트·보안 책임을 함께 점검했는가?</li></ul></section><footer class="footer"><strong>AI를 잘 쓰는 조직은,<br>더 똑똑한 답보다 더 분명한 책임을 설계한다.</strong><div class="share"><a href="../../index.html?kakao=20261102-ko-v1">최신호 홈 ↗</a><a href="../../?kakao=20261102-ko-v1">전체 아카이브 ↗</a><a href="../../assets/brief-2026-11-02-1080x1920.png">세로 브리프 이미지 ↗</a></div><div class="credit">TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief · 2026.11.02</div></footer></div></main></body></html>'''
    out = ROOT / 'archive' / '2026-11-02'; out.mkdir(parents=True, exist_ok=True); (out / 'index.html').write_text(html_doc, encoding='utf-8')
    (ROOT / 'index.html').write_text(f'<meta http-equiv="refresh" content="0; url=archive/2026-11-02/index.html?kakao=20261102-ko-v1"><link rel="canonical" href="{PAGE_URL}">', encoding='utf-8')

def create_source():
    lines = ['# Addit Daily Marketing Brief · 2026-11-02', '', '## 한 줄 결론', '', '**AI를 잘 쓰는 조직은 한도·검수·책임을 먼저 설계한다.** 오늘의 12개 원문을 대조해 사용량 예산, 안전 경계, 에이전트 책임, 전문가 검증, 오프라인 처리라는 다섯 축으로 재구성했다.', '', '## 오늘의 5대 트렌드', '']
    lines += [f'{i}. {s}' for i,s in enumerate(SIGNALS, 1)] + ['', '## CASE STUDY', '']
    for i,c in enumerate(CASES, 1): lines += [f'### {i}. {c["name"]} — {c["strategy"]}', '', '- 지역: ' + c['region'], '- 원문: ' + c['source'], '- 이미지: ' + c['image_source'], '- 확인 사실: ' + c['facts'], '- Addit Insight: ' + c['insight'], '']
    lines += ['## 원문 검수 목록', '']
    for n,d,u in SOURCE_ITEMS: lines += [f'- [{n}]({u}) — {d}']
    lines += ['', '## Addit ACTION CHECK', '', '- 사용량을 메시지 수가 아닌 업무 단위로 관리하는가?', '- AI 결과의 원문 근거와 사람의 검수자를 남겼는가?', '- 에이전트가 실행할 수 있는 권한과 중단 조건을 정했는가?', '- Shadow AI 대신 공식 도구·데이터 경로를 제공했는가?', '- 오프라인 처리와 업데이트·보안 책임을 함께 점검했는가?', '', '## 출처 및 검증 메모', '', '- 원고: 사용자가 제공한 https://baeksang.dev/daily/2026-11-02.', '- 링크 페이지의 12개 뉴스 URL을 직접 요청해 모두 HTTP 200 및 정상 페이지 제목을 확인했다.', '- CASE STUDY는 국내 4건·글로벌 1건으로 편성했다. 국내 사례는 삼성SDS·KOTRA·정부 AI 법령 비서·AWS 한국 리포트이며, 글로벌 사례는 OpenAI 공식 사용량 안내다.', '- 모든 수치·정책·제공 지역은 원문 표현을 유지하고, 실행 해석은 Addit Insight로 분리했다.']
    (ROOT / 'source').mkdir(exist_ok=True); (ROOT / 'source' / '2026-11-02.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

def create_manifest():
    manifest = {'date':'2026-11-02','title':TITLE,'html':'archive/2026-11-02/index.html','published_url':SHARE_URL,'og_image_path':'assets/og-2026-11-02-v1.png','og_image_url':OG_URL,'cases':[{'name':c['name'],'region':c['region'],'source_url':c['source'],'image_source_url':c['image_source'],'image_local_path':'assets/case/2026-11-02/'+c['image']} for c in CASES]}
    (ROOT / 'brief-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

def create_readme():
    (ROOT / 'README.md').write_text('# MKT_Brief\n\n- [2026.11.02 · AI를 잘 쓰는 조직은 한도·검수·책임을 먼저 설계한다](archive/2026-11-02/index.html)\n- [2026.10.30 · AI는 성능을 넘어, 실제 업무에 쓰이는 구조를 만든다](archive/2026-10-30/index.html)\n- [2026.10.29 · AI는 기능이 아니라, 자료·권한·검수의 흐름으로 설계된다](archive/2026-10-29/index.html)\n- [2026.10.28 · AI가 확장될수록, 비용·현장·책임을 함께 설계한다](archive/2026-10-28/index.html)\n- [2026.10.27 · AI가 커질수록, 접근권한과 책임을 먼저 설계한다](archive/2026-10-27/index.html)\n', encoding='utf-8')

def main():
    CASE_DIR.mkdir(parents=True, exist_ok=True)
    create_images(); create_html(); create_source(); create_manifest(); create_readme()

if __name__ == '__main__': main()
