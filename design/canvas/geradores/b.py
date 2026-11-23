import sys; sys.path.insert(0,'/home/claude/gen')
from data import *; from svgs import *
K="#0E0E0E"; L="#CFCFCC"; MK="#A9A9A6"; ML="#3A3A38"
fonts="family=Archivo+Narrow:wght@400;500;600;700&amp;family=IBM+Plex+Mono:wght@400;500"
style=f"""body{{margin:0;background:{K}}}
a{{color:inherit}}a:hover{{opacity:0.75}}
a:focus-visible{{outline:1.5px solid currentColor;outline-offset:4px}}
.contorno{{color:transparent;-webkit-text-stroke:1.5px {L}}}
@media (max-width: 820px){{.hero-b,.proj-b{{grid-template-columns:minmax(0,1fr) !important}}.proj-b .img-b{{order:-1}}}}"""
mono="font-family: 'IBM Plex Mono', ui-monospace, monospace; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase"
nar="font-family: 'Archivo Narrow', 'Arial Narrow', sans-serif"
ast=lambda s,c: f'<span aria-hidden="true" style="{nar}; font-weight: 700; font-size: {s}px; line-height: 1; color: {c}">*</span>'
bw,bc=barcode("MONTOVANELLI",46,K,2)
def regua():
    ticks=[]
    for i in range(0,81):
        h=18 if i%20==0 else (10 if i%5==0 else 6)
        ticks.append(f'<line x1="{i*10+0.5}" y1="30" x2="{i*10+0.5}" y2="{30-h}" stroke="{K}" stroke-width="1"></line>')
    labs="".join(f'<text x="{i*200+0.5}" y="8" font-family="IBM Plex Mono, monospace" font-size="11" fill="{K}" text-anchor="{"start" if i==0 else ("end" if i==4 else "middle")}">{"%02d"%i}</text>' for i in range(5))
    return f'<svg viewBox="0 -4 801 36" aria-hidden="true" style="width: 100%; height: auto; display: block"><line x1="0" y1="30.5" x2="801" y2="30.5" stroke="{K}"></line>{"".join(ticks)}{labs}</svg>'
def proj(p,i):
    escuro = i%2==1
    bg,fg,mu = (K,L,MK) if escuro else (L,K,ML)
    tags=" / ".join(p['hw']+p['sw'])
    dest = f'<p style="margin: 0; {mono}; color: {fg}">{ast(16,fg)} {p["dest"]}</p>' if p['dest'] else ''
    eclipse=f'''<svg viewBox="0 0 300 533" preserveAspectRatio="xMidYMid meet" aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%"><circle cx="150" cy="266" r="110" fill="none" stroke="{fg}" stroke-width="1"></circle><circle cx="150" cy="266" r="92" fill="none" stroke="{fg}" stroke-width="0.6" stroke-dasharray="2 4"></circle><line x1="20" y1="266" x2="280" y2="266" stroke="{fg}" stroke-width="0.6"></line></svg>'''
    if p["img"]:
        leg=f"{mono}; font-size: 10px; color: {mu}; line-height: 1.3"
        imgb=f'<div class="img-b" style="display: flex; flex-direction: column; gap: 8px"><figure style="margin: 0; aspect-ratio: 9 / 16; border: 1px solid {fg}; overflow: hidden"><img src="{p["img"]}" alt="{p["alt"]}" style="display: block; width: 100%; height: 100%; object-fit: cover"></figure>{thumbs(p,"1px solid "+fg,leg)}</div>'
    else:
        imgb=f'<div class="img-b" style="position: relative; aspect-ratio: 9 / 16; border: 1px solid {fg}">{eclipse}<span style="position: absolute; left: 12px; bottom: 10px; {mono}; font-size: 11px; color: {mu}">[Foto do projeto]</span></div>'
    return f'''<article style="position: relative; overflow: hidden; background: {bg}; color: {fg}">
{grao(0.5 if not escuro else 0.25, "multiply" if not escuro else "screen", "grao-b"+p["n"])}
<div class="proj-b" style="position: relative; max-width: 1280px; margin: 0 auto; padding: 56px clamp(20px, 4vw, 48px); box-sizing: border-box; display: grid; grid-template-columns: 140px minmax(0, 1fr) 260px; gap: 40px; align-items: start">
<div style="{nar}; font-weight: 700; font-size: 64px; line-height: 0.9; letter-spacing: -0.01em">{p["n"]}<span style="display: block; {mono}; font-size: 12px; margin-top: 10px; color: {mu}">/ 04</span></div>
<div style="display: flex; flex-direction: column; gap: 14px">
<span style="{mono}; color: {mu}">{p["ctx"]}</span>
<h2 style="margin: 0; {nar}; font-weight: 700; font-size: 44px; line-height: 1; text-transform: uppercase; letter-spacing: 0.01em">{p["titulo"]}</h2>
<p style="margin: 0; max-width: 58ch; {nar}; font-size: 20px; line-height: 1.4">{p["desc"]}</p>
{dest}
<p style="margin: 0; {mono}; color: {mu}; line-height: 1.7">{tags}</p>
</div>
{imgb}
</div>
</article>'''
body=f'''<div style="color: {K}; font-family: 'Archivo Narrow', 'Arial Narrow', sans-serif">
<header style="position: relative; overflow: hidden; background: {K}; color: {L}">
{grao(0.28,"screen","grao-b-topo")}
<div class="hero-b" style="position: relative; max-width: 1280px; margin: 0 auto; padding: 28px clamp(20px, 4vw, 48px) 48px; box-sizing: border-box; display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 32px; align-items: center">
<div style="grid-column: 1 / -1; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px">
<div style="display: flex; align-items: center; gap: 18px"><span aria-hidden="true" style="{nar}; font-weight: 700; font-size: 34px; letter-spacing: -0.12em; line-height: 1">❯❯❯❯</span><span style="{mono}; color: {MK}; line-height: 1.3; white-space: pre-line">Enrico Montovanelli
Portfólio / projetos</span></div>
<a href="Main.dc.html" style="{mono}; padding: 10px 0; text-underline-offset: 4px">Voltar ao menu</a>
</div>
<div style="position: relative"><svg viewBox="0 0 520 520" aria-hidden="true" style="width: 100%; max-width: 560px; height: auto; display: block">{globe(260,260,240,L,1)}</svg><span style="position: absolute; right: 8%; top: 6%">{ast(64,L)}</span></div>
<div style="display: flex; flex-direction: column; gap: 28px">
<h1 class="contorno" style="margin: 0; font-family: 'Archivo Narrow', sans-serif; font-weight: 600; font-size: clamp(56px, 8.5vw, 124px); letter-spacing: 0.22em; line-height: 1; text-transform: uppercase">Projetos</h1>
<div style="display: grid; grid-template-columns: 120px minmax(0, 1fr); border: 1px solid {L}">
<div style="border-right: 1px solid {L}; padding: 14px; {mono}; font-size: 22px; letter-spacing: 0; font-weight: 500">04/04</div>
<p style="margin: 0; padding: 14px 16px; font-size: 18px; line-height: 1.4">{INTRO}</p>
</div>
<div style="display: flex; gap: 40px; align-items: center">{ast(40,L)}<span style="{mono}; color: {MK}">Embarcados / IoT / Automação</span></div>
</div>
</div>
</header>
<div style="position: relative; overflow: hidden; background: {L}">
{grao(0.5,"multiply","grao-b-regua")}
<div style="position: relative; max-width: 1280px; margin: 0 auto; padding: 22px clamp(20px, 4vw, 48px) 10px; box-sizing: border-box">{regua()}</div>
</div>
<section aria-labelledby="fac-b-t">
<div style="position: relative; overflow: hidden; background: {K}; color: {L}; border-top: 1px solid {L}">{grao(0.25,"screen","fac-b")}<div style="position: relative; max-width: 1280px; margin: 0 auto; padding: 28px clamp(20px, 4vw, 48px); box-sizing: border-box; display: flex; flex-wrap: wrap; align-items: baseline; gap: 12px 32px"><span style="{nar}; font-weight: 700; font-size: 56px; line-height: 1">A</span><h2 id="fac-b-t" style="margin: 0; {nar}; font-weight: 700; font-size: 40px; text-transform: uppercase; letter-spacing: 0.04em">Projetos da faculdade</h2><span style="{mono}; color: {MK}">04 projetos / FAESA</span></div></div>
{"".join(proj(p,i) for i,p in enumerate(P))}
</section>
<section aria-labelledby="pes-b-t" style="position: relative; overflow: hidden; background: {K}; color: {L}">{grao(0.25,"screen","pes-b")}<div style="position: relative; max-width: 1280px; margin: 0 auto; padding: 40px clamp(20px, 4vw, 48px); box-sizing: border-box; display: flex; flex-wrap: wrap; align-items: baseline; gap: 12px 32px"><span style="{nar}; font-weight: 700; font-size: 56px; line-height: 1">B</span><h2 id="pes-b-t" style="margin: 0; {nar}; font-weight: 700; font-size: 40px; text-transform: uppercase; letter-spacing: 0.04em">Projetos pessoais</h2><span style="display: flex; align-items: center; gap: 12px; {mono}; color: {MK}">{ast(24,L)} {PESSOAIS}</span></div></section>
<footer style="position: relative; overflow: hidden; background: {L}">
{grao(0.5,"multiply","grao-b-rod")}
<div style="position: relative; max-width: 1280px; margin: 0 auto; padding: 32px clamp(20px, 4vw, 48px); box-sizing: border-box; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 20px">
<p style="margin: 0; max-width: 46ch; font-size: 16px; line-height: 1.4">Enrico Montovanelli. Engenharia da Computação, FAESA. Estagiário na automação da Laminação de Tiras a Quente da ArcelorMittal Tubarão.</p>
<svg viewBox="0 0 {bw} 46" aria-hidden="true" style="width: 220px; height: 46px">{bc}</svg>
</div>
</footer>
</div>'''
open(sys.argv[1],"w").write(page("Projetos, modelo B: monitor",fonts,style,body,3900))
