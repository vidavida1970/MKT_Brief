from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import shutil

ROOT = Path('/workspace/scratch/ca3169652574/work-2026-10-16')
CASE = ROOT / 'assets' / 'case' / '2026-10-16'
FONT = '/tmp/fonts/NotoSansKR.otf'
RED, INK, MUTED, LINE, PINK = '#E6002D', '#151515', '#5B5B5B', '#E6E6E6', '#FFF1F3'

TITLE = 'AI를 더 많이 쓰는 조직보다,\n더 안전하게 연결하는 조직이 앞선다'
SUBTITLE = '안전·공공서비스·업무·인프라까지 AI 도입의 기준이 달라지고 있습니다.'
PAGE_URL = 'https://vidavida1970.github.io/MKT_Brief/archive/2026-10-16/index.html'
SHARE_URL = PAGE_URL + '?kakao=20261016-ko-v1'
OG_URL = 'https://vidavida1970.github.io/MKT_Brief/assets/og-2026-10-16-v1.png'

cases = [
    {
        'no':'01', 'region':'KR', 'name':'경찰 AI 범죄 대응',
        'strategy':'AI 범죄를 탐지·분석·추적하는 수사 체계로 확장하다',
        'facts':'경찰청은 AI 불법 조작물 정밀 탐지와 범행 과정 분석을 위한 기본계획을 수립했다. 영상·음성·문자를 함께 보는 멀티모달 탐지, AI 전문분석관, 표준 절차 등 8대 과제를 추진한다.',
        'insight':'안전한 AI는 필터 하나가 아니라 탐지·분석·인력·절차의 운영체계다.',
        'source':'https://www.korea.kr/briefing/pressReleaseView.do?newsId=156785315',
        'image_source':'https://www.korea.kr/common/download.do?fileId=198570434&tblKey=GMN',
        'image':'police-cover.png', 'alt':'경찰청 AI 악용 범죄 대응 능력 업그레이드 공식 보도자료 첫 페이지',
    },
    {
        'no':'02', 'region':'KR', 'name':'산림청 임업직불제 AI 챗봇',
        'strategy':'현장 질문에 근거 문서까지 연결하는 업무형 챗봇을 만들다',
        'facts':'산림청은 10월 15일부터 임업직불제 업무용 AI 챗봇을 정식 운영한다. 질문에 답하면서 참고 문서와 유사 질의·회신 사례를 함께 보여주고, 업무지원시스템 안에서 바로 이용하게 했다.',
        'insight':'공공 AI의 신뢰는 답변 속도보다 근거와 업무 맥락을 함께 보여주는 데서 생긴다.',
        'source':'https://www.korea.kr/briefing/pressReleaseView.do?newsId=156785285',
        'image_source':'https://www.korea.kr/common/download.do?fileId=198570310&tblKey=GMN',
        'image':'forest-poster.jpg', 'alt':'산림청 임업직불제 업무용 AI 챗봇 서비스 공식 포스터',
    },
    {
        'no':'03', 'region':'KR', 'name':'SKT AI-RAN 무인차 이송',
        'strategy':'통신망을 센서·판단·제어가 이어지는 현장 인프라로 전환하다',
        'facts':'SKT는 AI-RAN 기반 완성차 무인 자율 이송으로 Network X 어워드의 혁신적인 5G 서비스 부문을 수상했다. 라이다 데이터로 디지털 트윈을 만들고, 경로 계산과 주행 명령까지 연결해 일반 차량의 무인 이송을 실증했다.',
        'insight':'피지컬 AI의 경쟁력은 모델보다 센서 데이터와 현장 제어 루프에 있다.',
        'source':'https://news.sktelecom.com/231994',
        'image_source':'https://news-static.sktelecom.com/wp-content/uploads/2026/10/SKT-%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C-SKT-Network-X-%EC%96%B4%EC%9B%8C%EB%93%9C-%EC%88%98%EC%83%81.-AI-%EA%B8%B0%EB%B0%98-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EA%B8%B0%EC%88%A0%EB%A0%A5-%EC%9D%B8%EC%A0%95_1_FB_1200x628.jpg',
        'image':'skt.jpg', 'alt':'SK텔레콤 AI-RAN 무인차 자율 이송 Network X 어워드 수상 현장',
    },
    {
        'no':'04', 'region':'KR', 'name':'팀스파르타 × Gemini Seoul',
        'strategy':'도구 도입 전에 조직의 AI 활용 수준부터 진단하다',
        'facts':'팀스파르타는 Google Cloud의 Build with Gemini Seoul에서 AI 역량 진단 도구 AXPI 체험존을 운영했다. AXPI는 기업과 구성원의 AI 활용 수준을 진단하며, 누적 진단 인원은 3만 명을 넘어섰다고 보도됐다.',
        'insight':'AX 전환은 새 도구를 사는 일보다 현재 역량과 직무별 격차를 먼저 측정하는 일이다.',
        'source':'https://ditoday.com/%ED%8C%80%EC%8A%A4%ED%8C%8C%EB%A5%B4%ED%83%80-%EA%B5%AC%EA%B8%80-%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-build-with-gemini-seoul-%EC%B0%B8%EA%B0%80/',
        'image_source':'https://ditoday.com/wp-content/uploads/2026/10/41.jpg',
        'image':'teamsparta.jpg', 'alt':'팀스파르타 Build with Gemini Seoul AXPI 체험존 현장',
    },
    {
        'no':'05', 'region':'GLOBAL', 'name':'Anthropic Singapore',
        'strategy':'지역 확장과 정부 협력으로 안전한 도입의 현장성을 높이다',
        'facts':'Anthropic은 싱가포르에 아시아·태평양 다섯 번째 사무소를 열고 정부와 AI 안전·평가·책임 있는 도입을 위한 MOU를 체결했다. 공식 발표는 싱가포르가 인구 대비 Claude 사용량 121개국 중 2위이며 GovTech·Grab·DBS 등이 활용 중이라고 설명한다.',
        'insight':'글로벌 AI 확장은 모델 판매가 아니라 현지 파트너·평가·안전 체계를 함께 구축하는 일이다.',
        'source':'https://www.anthropic.com/news/singapore-office-opening',
        'image_source':'https://www-cdn.anthropic.com/images/4zrzovbb/website/5f455d24ea80569b34eb4347f06152d8a5508722-1000x1000.svg',
        'image':'anthropic.png', 'alt':'Anthropic Singapore office and government MOU 공식 대표 일러스트',
    },
]

def f(size, bold=False):
    ft = ImageFont.truetype(FONT, size)
    try: ft.set_variation_by_axes([700 if bold else 400])
    except Exception: pass
    return ft

def lines(draw, text, font, max_width):
    out=[]
    for para in text.split('\n'):
        line=''
        for ch in para:
            if draw.textbbox((0,0), line+ch, font=font)[2] <= max_width: line += ch
            else:
                if line: out.append(line)
                line=ch
        if line: out.append(line)
    return out

def wrap(draw, xy, text, font, fill=INK, max_width=900, spacing=8):
    x,y=xy
    for line in lines(draw,text,font,max_width):
        draw.text((x,y),line,font=font,fill=fill); y += font.size+spacing
    return y

def rounded(draw, box, radius=18, fill='white', outline=LINE, width=2):
    draw.rounded_rectangle(box,radius=radius,fill=fill,outline=outline,width=width)

def header(d, W):
    margin=70 if W==1200 else 48
    d.rectangle((0,0,W,14),fill=RED)
    d.text((margin,48 if W==1200 else 42),'addit+',font=f(42 if W==1200 else 55,True),fill=RED)
    d.text((950 if W==1200 else W-260,62 if W==1200 else 60),'2026.10.16 FRI',font=f(21 if W==1200 else 22,True),fill=INK)
    d.line((margin,125,W-margin,125),fill=LINE,width=2)

def create_og():
    im=Image.new('RGB',(1200,630),'white'); d=ImageDraw.Draw(im); header(d,1200)
    d.text((70,160),'ADDIT DAILY MARKETING BRIEF',font=f(22,True),fill=RED)
    y=wrap(d,(70,205),TITLE,f(46,True),max_width=1080,spacing=4)
    d.text((72,y+18),SUBTITLE,font=f(21),fill=MUTED)
    d.rounded_rectangle((70,535,1130,585),radius=25,fill=PINK)
    d.text((95,547),"TODAY’S TREND, TOMORROW’S STRATEGY.",font=f(20,True),fill=RED)
    im.save(ROOT/'assets/og-2026-10-16-v1.png')

def create_vertical():
    W,H,margin=1080,1920,48
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im); header(d,W)
    d.text((margin,160),'ADDIT DAILY MARKETING BRIEF',font=f(19,True),fill=RED)
    y=wrap(d,(margin,205),TITLE,f(40,True),max_width=W-2*margin,spacing=4)
    y+=10; d.text((margin,y),SUBTITLE,font=f(20),fill=MUTED); y+=58
    rounded(d,(margin,y,W-margin,y+103),radius=18,fill='#FAFAFA')
    d.text((margin+24,y+18),'GOOD MORNING, ADDIT',font=f(22,True),fill=RED)
    wrap(d,(margin+24,y+54),'AI는 도입보다 연결 방식이 중요해지는 단계로 들어섰습니다.',f(20),fill=MUTED,max_width=W-2*margin-48,spacing=2)
    y+=138; d.text((margin,y),'TODAY’S 5 SIGNALS',font=f(20,True),fill=RED); y+=40
    trends=[
        'AI는 기능에서 공공·업무·생활 인프라로 내려온다',
        '모델 가격 하락과 MCP 연결이 실제 도입 비용을 낮춘다',
        'AI 안전은 탐지·추적·사람 검토 체계로 확장된다',
        '사용자 신뢰가 무너지면 서비스와 기업가치가 함께 흔들린다',
        'AI 투자 리스크의 중심이 모델에서 인프라·신용으로 이동한다',
    ]
    for i,t in enumerate(trends,1):
        by=y+(i-1)*63; rounded(d,(margin,by,W-margin,by+52),radius=14)
        d.ellipse((margin+12,by+7,margin+48,by+43),fill=RED); d.text((margin+20,by+13),f'{i:02d}',font=f(14,True),fill='white')
        d.text((margin+64,by+13),t,font=f(17,True),fill=INK)
    y+=5*63+24; d.text((margin,y),'CASE STUDY · 4 KR / 1 GLOBAL',font=f(20,True),fill=RED); y+=42
    for c in cases:
        box_h=148; rounded(d,(margin,y,W-margin,y+box_h),radius=18)
        src=Image.open(CASE/c['image']).convert('RGB'); crop=ImageOps.fit(src,(250,108),method=Image.Resampling.LANCZOS,centering=(0.5,0.5)); im.paste(crop,(margin+16,y+20))
        d.rounded_rectangle((margin+16,y+20,margin+266,y+128),radius=12,outline=LINE,width=1)
        d.ellipse((margin+292,y+18,margin+338,y+64),fill=RED); d.text((margin+305,y+26),c['no'],font=f(15,True),fill='white')
        d.text((margin+362,y+22),c['name'],font=f(20,True),fill=INK)
        wrap(d,(margin+292,y+67),c['strategy'],f(14),fill=MUTED,max_width=650,spacing=2); y+=box_h+10
    y+=12; rounded(d,(margin,y,W-margin,y+142),radius=18,fill=PINK,outline='#F1D7DC')
    d.text((margin+24,y+15),'ADDIT ACTION CHECK',font=f(20,True),fill=RED)
    actions=['모델 권한과 업무 범위를 분리했는가?','답변의 근거 문서와 검토 주체가 있는가?','민감 데이터의 경계를 정했는가?','현장 적용의 안전 기준을 준비했는가?','비용·연동·신뢰 지표를 함께 관리하는가?']
    for i,a in enumerate(actions): d.text((margin+28,y+48+i*18),'□  '+a,font=f(15),fill=INK)
    y+=178; d.line((margin,y,W-margin,y),fill=LINE,width=2); d.text((margin,y+17),'AI를 더 많이 쓰는 조직보다,',font=f(20),fill=MUTED); d.text((margin,y+51),'더 안전하게 연결하는 조직이 앞선다.',font=f(23,True),fill=INK)
    im.save(ROOT/'assets/brief-2026-10-16-1080x1920.png')

def card_html(c):
    slug=c['name'].lower().replace(' ','-').replace('×','x').replace('·','-')
    return f'''<article class="case"><a data-case-study="{slug}" href="{c['source']}" target="_blank" rel="noopener noreferrer"><img data-source-image="{c['image_source']}" src="../../assets/case/2026-10-16/{c['image']}" alt="{c['alt']}"></a><div><div class="num">{c['no']} · {c['region']}</div><h3>{c['name']}</h3><p class="strategy">{c['strategy']}</p><p class="facts">{c['facts']}</p><a class="source" data-case-study="{slug}-source" href="{c['source']}" target="_blank" rel="noopener noreferrer">원문 보기 ↗</a></div><div class="insight"><strong>ADDIT INSIGHT</strong><p>{c['insight']}</p></div></article>'''

def create_html():
    card_block='\n'.join(card_html(c) for c in cases)
    html=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI를 더 많이 쓰는 조직보다, 더 안전하게 연결하는 조직이 앞선다 | Addit Daily Marketing Brief</title>
<meta name="description" content="안전·공공서비스·업무·인프라까지 AI 도입의 기준이 달라지고 있습니다.">
<link rel="canonical" href="{PAGE_URL}">
<meta property="og:type" content="article"><meta property="og:locale" content="ko_KR"><meta property="og:title" content="AI를 더 많이 쓰는 조직보다, 더 안전하게 연결하는 조직이 앞선다"><meta property="og:description" content="안전·공공서비스·업무·인프라까지 AI 도입의 기준이 달라지고 있습니다."><meta property="og:url" content="{SHARE_URL}"><meta property="og:image" content="{OG_URL}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{OG_URL}">
<style>
:root{{--red:#e6002d;--ink:#151515;--muted:#5b5b5b;--line:#e6e6e6;--pink:#fff1f3;--bg:#faf9f7}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:Arial,"Noto Sans KR",sans-serif;line-height:1.55}}a{{color:inherit}}.page{{max-width:980px;margin:auto;background:#fff;box-shadow:0 0 0 1px #f0eeee}}.top{{height:10px;background:var(--red)}}.wrap{{padding:34px 56px 68px}}.mast{{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--line);padding-bottom:22px}}.brand{{font-size:35px;font-weight:900;color:var(--red);letter-spacing:-.07em}}.date{{font-size:14px;font-weight:800}}.eyebrow{{margin-top:40px;color:var(--red);font-size:14px;font-weight:900;letter-spacing:.04em}}.hero h1{{font-size:clamp(36px,5vw,64px);line-height:1.08;letter-spacing:-.07em;max-width:900px;margin:18px 0}}.hero p{{font-size:19px;color:var(--muted);margin:0;max-width:760px}}.morning{{margin-top:32px;border:1px solid var(--line);border-radius:18px;padding:21px 24px;background:#fcfcfc}}.morning strong,.section-head span{{color:var(--red);font-size:14px;letter-spacing:.04em}}.morning p{{margin:6px 0 0;color:var(--muted)}}section{{margin-top:55px}}.section-head{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid var(--ink);padding-bottom:12px}}.section-head h2{{font-size:20px;margin:0;letter-spacing:-.04em}}.section-head span{{font-size:12px;font-weight:800}}.signals{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}}.signal{{border:1px solid var(--line);border-radius:14px;padding:17px 18px;display:flex;gap:14px}}.signal b{{background:var(--red);color:#fff;border-radius:50%;width:32px;height:32px;display:grid;place-items:center;font-size:12px;flex:0 0 auto}}.signal p{{margin:4px 0 0;font-weight:800;line-height:1.4;letter-spacing:-.03em}}.cases{{display:grid;gap:18px;margin-top:20px}}.case{{display:grid;grid-template-columns:240px 1fr 205px;gap:24px;align-items:center;border:1px solid var(--line);border-radius:18px;padding:18px;background:#fff}}.case img{{width:240px;height:150px;object-fit:cover;border-radius:12px;background:#eee}}.case .num{{color:var(--red);font-size:12px;font-weight:900;letter-spacing:.08em}}.case h3{{font-size:25px;line-height:1.2;letter-spacing:-.05em;margin:5px 0 9px}}.strategy{{font-weight:800;margin:0 0 9px;letter-spacing:-.03em}}.facts{{color:var(--muted);font-size:14px;margin:0;line-height:1.55}}.insight{{background:var(--pink);border:1px solid #f1d7dc;border-radius:14px;padding:18px}}.insight strong{{display:block;color:var(--red);font-size:12px;letter-spacing:.04em;margin-bottom:7px}}.insight p{{font-size:14px;font-weight:800;line-height:1.45;margin:0}}.source{{display:inline-block;margin-top:12px;color:var(--red);font-size:12px;font-weight:800;text-decoration:none;border-bottom:1px solid #f5a8b8}}.watch{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}}.watch a{{border:1px solid var(--line);border-radius:14px;padding:16px;text-decoration:none;background:#fff}}.watch b{{display:block;font-size:14px;margin-bottom:5px}}.watch span{{font-size:13px;color:var(--muted)}}.action{{margin-top:55px;background:var(--pink);border:1px solid #f1d7dc;border-radius:18px;padding:25px}}.action h2{{color:var(--red);font-size:18px;margin:0 0 13px}}.action ul{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:9px 18px}}.action li{{font-size:14px}}.action li:before{{content:"□  ";color:var(--red);font-weight:900}}.footer{{margin-top:50px;border-top:1px solid var(--line);padding-top:24px;color:var(--muted)}}.footer strong{{display:block;color:var(--ink);font-size:21px;letter-spacing:-.04em}}.share{{display:flex;gap:12px;flex-wrap:wrap;margin-top:16px}}.share a{{font-size:12px;text-decoration:none;color:var(--red);font-weight:800}}.credit{{font-size:11px;color:#888;margin-top:20px}}@media(max-width:760px){{.wrap{{padding:24px 20px 48px}}.brand{{font-size:29px}}.date{{font-size:11px}}.hero h1{{font-size:43px}}.hero p{{font-size:16px}}.signals,.watch,.action ul{{grid-template-columns:1fr}}.section-head{{display:block}}.section-head span{{display:block;margin-top:5px}}.case{{grid-template-columns:1fr;gap:13px}}.case img{{width:100%;height:190px}}.case h3{{font-size:24px}}}}
</style></head><body><main class="page"><div class="top"></div><div class="wrap">
<header class="mast"><div class="brand">addit+</div><div class="date">2026.10.16 FRI</div></header>
<div class="hero"><div class="eyebrow">ADDIT DAILY MARKETING BRIEF</div><h1>AI를 더 많이 쓰는 조직보다,<br>더 안전하게 연결하는 조직이 앞선다</h1><p>{SUBTITLE}</p></div>
<div class="morning"><strong>GOOD MORNING, ADDIT</strong><p>AI는 도입보다 연결 방식이 중요해지는 단계로 들어섰습니다.</p></div>
<section><div class="section-head"><h2>TODAY’S 5 SIGNALS</h2><span>10.16 · AI OPERATING BRIEF</span></div><div class="signals"><div class="signal"><b>01</b><p>AI는 기능에서 공공·업무·생활 인프라로 내려온다.</p></div><div class="signal"><b>02</b><p>모델 가격 하락과 MCP 연결이 실제 도입 비용을 낮춘다.</p></div><div class="signal"><b>03</b><p>AI 안전은 탐지·추적·사람 검토 체계로 확장된다.</p></div><div class="signal"><b>04</b><p>사용자 신뢰가 무너지면 서비스와 기업가치가 함께 흔들린다.</p></div><div class="signal"><b>05</b><p>AI 투자 리스크의 중심이 모델에서 인프라·신용으로 이동한다.</p></div></div></section>
<section><div class="section-head"><h2>CASE STUDY</h2><span>4 KR / 1 GLOBAL</span></div><div class="cases">{card_block}</div></section>
<section><div class="section-head"><h2>PLATFORM WATCH</h2><span>원고에서 확인한 추가 신호</span></div><div class="watch"><a href="https://aws.amazon.com/ko/blogs/korea/aws-weekly-roundup-prime-day-2026-by-the-numbers-claude-haiku-5-5-amazon-nova-2-5-sonic-and-more-october-13-2026/" target="_blank" rel="noopener noreferrer"><b>Claude Haiku 5.5</b><span>Haiku 4.5보다 약 75% 낮아진 비용과 작업별 추론 조절</span></a><a href="https://www.globenewswire.com/news-release/2026/10/15/3381918/0/ko/axi-mt5-%EA%B3%84%EC%A0%95%EA%B3%BC-%ED%81%B4%EB%A1%9C%EB%93%9C-%EC%97%B0%EA%B2%B0%ED%95%98%EB%8A%94-mcp-%ED%86%B5%ED%95%A9-%EC%86%94%EB%A3%A8%EC%85%98-%EC%B6%9C%EC%8B%9C.html" target="_blank" rel="noopener noreferrer"><b>Axi × Claude MCP</b><span>MT5 계정과 Claude를 연결하는 금융 업무 커넥터</span></a><a href="https://news.kbs.co.kr/news/pc/view/view.do?ncd=8686303" target="_blank" rel="noopener noreferrer"><b>청소년 안전 소송</b><span>챗GPT 사용 안전성과 사업자 책임을 둘러싼 미국 8개 주 제소</span></a><a href="https://www.aitimes.com/news/articleView.html?idxno=216239" target="_blank" rel="noopener noreferrer"><b>Character.AI 파산보호</b><span>생성형 캐릭터 서비스의 성장 이후 지속가능성 이슈</span></a><a href="https://news.einfomax.co.kr/news/articleView.html?idxno=4439287" target="_blank" rel="noopener noreferrer"><b>CoreWeave 채권 쇼크</b><span>AI 인프라 투자와 신용 리스크가 연결되는 시장 신호</span></a><a href="https://ko.laodong.vn/cong-nghe/google-tich-hop-ai-gemini-vao-android-de-phat-hien-tin-nhan-lua-dao-1783497.ldo" target="_blank" rel="noopener noreferrer"><b>Gemini 사기 메시지 탐지</b><span>생활 속 안전 기능으로 확장되는 AI</span></a></div></section>
<section class="action"><h2>ADDIT ACTION CHECK</h2><ul><li>모델 권한과 업무 범위를 분리했는가?</li><li>답변의 근거 문서와 검토 주체가 있는가?</li><li>민감 데이터의 경계를 정했는가?</li><li>현장 적용의 안전 기준을 준비했는가?</li><li>비용·연동·신뢰 지표를 함께 관리하는가?</li></ul></section>
<footer class="footer"><strong>AI를 더 많이 쓰는 조직보다,<br>더 안전하게 연결하는 조직이 앞선다.</strong><div class="share"><a href="../../index.html?kakao=20261016-ko-v1">최신호 홈 ↗</a><a href="../../?kakao=20261016-ko-v1">전체 아카이브 ↗</a><a href="../../assets/brief-2026-10-16-1080x1920.png">세로 브리프 이미지 ↗</a></div><div class="credit">TODAY’S TREND, TOMORROW’S STRATEGY. · Addit Daily Marketing Brief · 2026.10.16</div></footer>
</div></main></body></html>'''
    out=ROOT/'archive'/'2026-10-16'; out.mkdir(parents=True,exist_ok=True); (out/'index.html').write_text(html,encoding='utf-8')
    (ROOT/'index.html').write_text('<meta http-equiv="refresh" content="0; url=archive/2026-10-16/index.html?kakao=20261016-ko-v1"><link rel="canonical" href="https://vidavida1970.github.io/MKT_Brief/archive/2026-10-16/index.html">',encoding='utf-8')
    (ROOT/'archive'/'index.html').write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Addit Daily Marketing Brief Archive</title></head><body><h1>Addit Daily Marketing Brief</h1><ul><li><a href="2026-10-16/index.html">2026.10.16 · AI를 더 많이 쓰는 조직보다, 더 안전하게 연결하는 조직이 앞선다</a></li><li><a href="2026-10-15/index.html">2026.10.15 · AI가 전면으로 열릴수록, 도입보다 검증을 설계한다</a></li></ul></body></html>',encoding='utf-8')

def main():
    CASE.mkdir(parents=True,exist_ok=True); (ROOT/'assets').mkdir(exist_ok=True)
    src=Path('/tmp/mkt16-sources/assets')
    for name in ('police-cover.png','forest-poster.jpg','skt.jpg','teamsparta.jpg','anthropic.png'):
        shutil.copy2(src/name,CASE/name)
    (ROOT/'source').mkdir(exist_ok=True); create_og(); create_vertical(); create_html()

if __name__=='__main__': main()
