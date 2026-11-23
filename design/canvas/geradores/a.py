import sys; sys.path.insert(0,'/home/claude/gen')
from data import *; from svgs import *
BG="#0B0B0C"; FG="#E8E6E1"; MU="#A3A19C"
fonts="family=Syncopate:wght@400;700&amp;family=Inter+Tight:wght@400;500;600&amp;family=IBM+Plex+Mono:wght@400;500"
style=f"""body{{margin:0;background:{BG}}}
a{{color:{FG}}}a:hover{{color:#FFFFFF}}
a:focus-visible{{outline:1.5px solid {FG};outline-offset:4px}}
.listrado{{background:repeating-linear-gradient(0deg,{FG} 0 3px,transparent 3px 6px);-webkit-background-clip:text;background-clip:text;color:transparent}}
@media (max-width: 820px){{.proj-a{{grid-template-columns:minmax(0,1fr) !important}}.hero-a{{grid-template-columns:minmax(0,1fr) !important}}}}"""
mono="font-family: 'IBM Plex Mono', ui-monospace, monospace; font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase"
wide="font-family: 'Syncopate', 'Inter Tight', sans-serif; text-transform: uppercase"
sq='<span aria-hidden="true" style="display: inline-block; width: 6px; height: 6px; background: %s"></span>'
def linha_pontos(label=None):
    lab = f'<span style="{mono}; color: {MU}; white-space: nowrap">{label}</span>' if label else ''
    return f'''<div style="display: flex; align-items: center; gap: 14px">{lab}<div aria-hidden="true" style="flex: 1; display: flex; align-items: center; gap: 0"><span style="width: 7px; height: 7px; border-radius: 50%; border: 1px solid {FG}; box-sizing: border-box"></span><span style="flex: 1; height: 1px; background: {FG}; opacity: 0.6"></span><span style="width: 4px; height: 4px; border-radius: 50%; background: {FG}"></span><span style="width: 40px; height: 1px; background: {FG}; opacity: 0.6"></span><span style="width: 4px; height: 4px; border-radius: 50%; background: {FG}"></span><span style="width: 40px; height: 1px; background: {FG}; opacity: 0.6"></span><span style="width: 9px; height: 9px; border-radius: 50%; border: 1px solid {FG}; box-sizing: border-box"></span></div></div>'''
stars=f'''<svg viewBox="0 0 560 520" role="img" aria-label="Estrela de quatro pontas se desfazendo em partículas" style="width: 100%; height: auto; display: block">
<circle cx="300" cy="260" r="190" fill="none" stroke="{FG}" stroke-width="10" opacity="0.18"></circle>
<circle cx="300" cy="260" r="190" fill="none" stroke="{FG}" stroke-width="1" opacity="0.7" stroke-dasharray="1 0"></circle>
{particles(300,260,60,250,520,7,FG,-80,95)}
{star(250,250,200,color=FG)}
{star(78,470,26,color=FG)}
</svg>'''
def img_a(p):
    if p["img"]:
        leg=f"font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: 0.06em; text-transform: uppercase; color: {MU}; line-height: 1.3"
        return f'<div style="display: flex; flex-direction: column; gap: 8px"><figure style="margin: 0; aspect-ratio: 9 / 16; border: 1px solid rgba(232,230,225,0.35); overflow: hidden"><img src="{p["img"]}" alt="{p["alt"]}" style="display: block; width: 100%; height: 100%; object-fit: cover"></figure>{thumbs(p,"1px solid rgba(232,230,225,0.35)",leg)}</div>'
    return f'''<div style="position: relative; aspect-ratio: 9 / 16; border: 1px solid rgba(232,230,225,0.35); display: flex; align-items: center; justify-content: center; {mono}; color: {MU}">
<span aria-hidden="true" style="position: absolute; left: 50%; top: 50%; width: 22px; height: 1px; background: {MU}; transform: translate(-50%, -50%)"></span>
<span aria-hidden="true" style="position: absolute; left: 50%; top: 50%; width: 1px; height: 22px; background: {MU}; transform: translate(-50%, -50%)"></span>
<span style="position: absolute; bottom: 10px; left: 12px">[Foto do projeto]</span>
</div>'''
def proj(p):
    tags=" • ".join(p['hw']+p['sw'])
    dest = f'<p style="margin: 0; {mono}; color: {FG}">✦ {p["dest"]}</p>'.replace("✦ ","") if p['dest'] else ''
    if p['dest']: dest=f'<p style="margin: 0; display: flex; gap: 10px; align-items: center; {mono}; color: {FG}">{sq%FG} {p["dest"]}</p>'
    return f'''<article class="proj-a" style="display: grid; grid-template-columns: 200px minmax(0, 1fr) 240px; gap: 32px; align-items: start; padding: 40px 0; border-top: 1px solid rgba(232,230,225,0.28)">
<div style="display: flex; flex-direction: column; gap: 10px; {mono}">
<span style="color: {FG}">Arquivo / {p["n"]}</span>
<span style="color: {MU}; letter-spacing: 0.06em; line-height: 1.5">{p["ctx"]}</span>
</div>
<div style="display: flex; flex-direction: column; gap: 16px">
<h2 style="margin: 0; {wide}; font-weight: 700; font-size: 26px; letter-spacing: 0.08em; line-height: 1.25">{p["titulo"]}</h2>
<p style="margin: 0; max-width: 60ch; font-size: 16px; line-height: 1.55; color: {FG}">{p["desc"]}</p>
{dest}
<p style="margin: 0; {mono}; color: {MU}; letter-spacing: 0.06em; line-height: 1.7">{tags}</p>
</div>
{img_a(p)}
</article>'''
body=f'''<div style="position: relative; overflow: hidden; background: {BG}; color: {FG}; font-family: 'Inter Tight', 'Helvetica Neue', Arial, sans-serif; font-size: 15px; line-height: 1.45">
{grao(0.22,"screen","grao-a")}
<div style="position: relative; max-width: 1280px; margin: 0 auto; padding: clamp(20px, 4vw, 48px); box-sizing: border-box; display: flex; flex-direction: column; gap: 56px">
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px; {mono}">
<div style="display: flex; align-items: center; gap: 14px"><span style="font-weight: 500">EM // Arquivo de projetos</span><span style="display: flex; gap: 4px">{sq%FG}{sq%FG}{sq%MU}{sq%MU}</span></div>
<div style="display: flex; align-items: center; gap: 28px"><span style="color: {MU}">Embarcados • IoT • Automação</span><a href="Main.dc.html" style="padding: 10px 0; text-underline-offset: 4px">Voltar ao menu</a></div>
</div>
<div class="hero-a" style="display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr); gap: 32px; align-items: center">
<div style="display: flex; flex-direction: column; gap: 26px">
<span style="align-self: flex-start; padding: 6px 16px; border: 1px solid rgba(232,230,225,0.5); border-radius: 20px; {mono}">Arquivo / 04</span>
<span style="{mono}; font-size: 10px; color: {MU}">Enrico Montovanelli</span>
<h1 class="listrado" style="margin: 0; {wide}; font-weight: 700; font-size: clamp(48px, 7.4vw, 104px); letter-spacing: 0.04em; line-height: 0.95">Projetos</h1>
<div aria-hidden="true" style="display: flex; gap: 6px"><span style="width: 30px; height: 6px; background: {FG}"></span><span style="width: 10px; height: 6px; background: {FG}"></span><span style="width: 10px; height: 6px; background: {MU}"></span><span style="width: 10px; height: 6px; background: {MU}"></span></div>
<p style="margin: 0; max-width: 42ch; font-size: 18px; line-height: 1.5">{INTRO}</p>
</div>
<div>{stars}</div>
</div>
{linha_pontos("Setor / 01 · Faculdade")}
<section aria-labelledby="sec-fac" style="display: flex; flex-direction: column">
<h2 id="sec-fac" style="margin: 0 0 8px; {wide}; font-weight: 400; font-size: 14px; letter-spacing: 0.3em">Projetos da faculdade</h2>
{"".join(proj(p) for p in P)}
</section>
{linha_pontos("Setor / 02 · Pessoais")}
<section aria-labelledby="sec-pes" style="display: grid; grid-template-columns: 200px minmax(0, 1fr); gap: 32px; padding: 8px 0 24px" class="proj-a">
<span style="{mono}; color: {MU}">Arquivo / --</span>
<div style="display: flex; flex-direction: column; gap: 10px"><h2 id="sec-pes" style="margin: 0; {wide}; font-weight: 400; font-size: 14px; letter-spacing: 0.3em">Projetos pessoais</h2><p style="margin: 0; font-size: 16px; color: {MU}">{PESSOAIS}</p></div>
</section>
{linha_pontos()}
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px; {mono}; color: {MU}; padding-bottom: 8px"><span>Sistemas embarcados • IoT • Automação</span><span>Enrico Montovanelli • 2026</span></div>
</div>
</div>'''
open(sys.argv[1],"w").write(page("Projetos, modelo A: arquivo",fonts,style,body,3600))
