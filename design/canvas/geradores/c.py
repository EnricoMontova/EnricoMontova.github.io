import sys; sys.path.insert(0,'/home/claude/gen')
from data import *; from svgs import *
BG="#050505"; FG="#F2F1EE"; MU="#A8A7A3"; LN="1px solid #F2F1EE"
fonts="family=Tektur:wdth,wght@125,500;125,800&amp;family=JetBrains+Mono:wght@400;500;700"
style=f"""body{{margin:0;background:{BG}}}
a{{color:{FG}}}a:hover{{color:#FFFFFF}}
a:focus-visible{{outline:1.5px solid {FG};outline-offset:4px}}
.pixel{{background-image:radial-gradient({FG} 1.2px, transparent 1.4px);background-size:6px 6px;opacity:0.55}}
@media (max-width: 820px){{.topo-c,.ficha-c{{grid-template-columns:minmax(0,1fr) !important}}.ficha-c>div{{border-right:0 !important}}}}"""
mono="font-family: 'JetBrains Mono', ui-monospace, monospace; font-size: 13px; letter-spacing: 0.04em; text-transform: uppercase"
tek="font-family: 'Tektur', 'Arial Black', sans-serif; font-stretch: 125%"
ponto='<span aria-hidden="true" style="position: absolute; width: 7px; height: 7px; border-radius: 50%; background: '+FG+'; POS"></span>'
def cantos():
    return "".join(ponto.replace("POS",p) for p in ["left: -4px; top: -4px","right: -4px; top: -4px","left: -4px; bottom: -4px","right: -4px; bottom: -4px"])
def colchetes(c=FG):
    s="position: absolute; width: 16px; height: 16px; border-color: %s; border-style: solid;"%c
    return (f'<span aria-hidden="true" style="{s} left: 10px; top: 10px; border-width: 1px 0 0 1px"></span>'
            f'<span aria-hidden="true" style="{s} right: 10px; top: 10px; border-width: 1px 1px 0 0"></span>'
            f'<span aria-hidden="true" style="{s} left: 10px; bottom: 10px; border-width: 0 0 1px 1px"></span>'
            f'<span aria-hidden="true" style="{s} right: 10px; bottom: 10px; border-width: 0 1px 1px 0"></span>')
def linha(rot,val,ult=False):
    b="" if ult else f"border-bottom: {LN};"
    return f'<div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 6px 24px; padding: 12px 16px; {b} {mono}"><span style="font-weight: 700">//{rot}_</span><span style="text-align: right">{val}</span></div>'
def ficha(p):
    rows=[("Projeto",p["titulo"]),("Contexto",p["ctx"]),("Hardware"," / ".join(p["hw"])),("Software"," / ".join(p["sw"]))]
    if p["dest"]: rows.append(("Destaque",p["dest"]))
    linhas="".join(linha(r,v) for r,v in rows)
    if p["img"]:
        leg=f"font-family: 'JetBrains Mono', monospace; font-size: 10px; text-transform: uppercase; color: {MU}; line-height: 1.3"
        imgc=f'<div style="border-right: {LN}; display: flex; flex-direction: column"><figure style="margin: 0; aspect-ratio: 9 / 16; overflow: hidden; border-bottom: {LN}"><img src="{p["img"]}" alt="{p["alt"]}" style="display: block; width: 100%; height: 100%; object-fit: cover"></figure><div style="padding: 10px">{thumbs(p,LN,leg)}</div></div>'
    else:
        imgc=f'''<div style="position: relative; border-right: {LN}; aspect-ratio: 9 / 16; display: flex; align-items: flex-end; padding: 14px 16px; box-sizing: border-box">
<div class="pixel" aria-hidden="true" style="position: absolute; inset: 30px"></div>{colchetes()}
<span style="position: relative; {mono}; font-size: 11px; background: {BG}; padding: 2px 6px">[Foto do projeto]</span></div>'''
    return f'''<article style="position: relative; border: {LN}">{cantos()}
<div class="ficha-c" style="display: grid; grid-template-columns: 260px minmax(0, 1fr)">
{imgc}
<div style="display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; align-items: center; padding: 12px 16px; border-bottom: {LN}; {mono}"><span>Projeto #{p["n"]}</span><span aria-hidden="true">///</span></div>
{linhas}
<p style="margin: 0; padding: 16px; font-family: 'JetBrains Mono', monospace; font-size: 14px; line-height: 1.6; color: {FG}">{p["desc"]}</p>
</div></div></article>'''
cw=" ".join
painel=f'''<svg viewBox="0 0 1180 90" aria-hidden="true" style="width: 100%; height: auto; display: block">{"".join(f'<g transform="translate({i*98},0)"><polygon points="4,8 86,22 86,68 4,82" fill="none" stroke="{FG}" stroke-width="1"></polygon>{"".join(f"<line x1=\"{4+k*10.25:.1f}\" y1=\"{8+k*1.75:.1f}\" x2=\"{4+k*10.25:.1f}\" y2=\"{82-k*1.75:.1f}\" stroke=\"{FG}\" stroke-width=\"0.6\"></line>" for k in range(1,8))}</g>' for i in range(12))}</svg>'''
body=f'''<div style="background: {BG}; color: {FG}; font-family: 'JetBrains Mono', ui-monospace, monospace">
<div style="max-width: 1200px; margin: 0 auto; padding: clamp(20px, 4vw, 48px); box-sizing: border-box; display: flex; flex-direction: column; gap: 28px">
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px; {mono}; font-weight: 700"><span>Enrico Montovanelli</span><span aria-hidden="true">✦</span><a href="Main.dc.html" style="padding: 4px 0; text-underline-offset: 4px">Voltar ao menu</a></div>
<div style="position: relative; border: {LN}">{cantos()}
<div class="topo-c" style="display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr)">
<div style="border-right: {LN}; display: flex; flex-direction: column">
<div style="padding: 12px 16px; border-bottom: {LN}; {mono}">Portfólio / projetos #04</div>
<div style="position: relative; flex: 1; min-height: 240px"><div class="pixel" aria-hidden="true" style="position: absolute; inset: 28px"></div>{colchetes()}</div>
</div>
<div style="display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; padding: 12px 16px; border-bottom: {LN}; {mono}"><span>///</span><span>FAESA / ArcelorMittal</span></div>
<div style="display: grid; grid-template-columns: minmax(0, 1fr) 170px; gap: 12px; padding: 16px; align-items: center">
<p style="margin: 0; {mono}; font-size: 12px; line-height: 1.7; white-space: pre-line">Sistemas embarcados
IoT
Automação
Firmware em C/C++</p>
<svg viewBox="0 0 200 200" aria-hidden="true" style="width: 100%; height: auto">{globe(100,100,92,FG,0.8)}</svg>
</div>
<div style="padding: 0 16px 14px"><div style="display: flex; justify-content: space-between; {mono}; font-size: 11px"><span>2022</span><span>2026</span></div><div aria-hidden="true" style="height: 10px; border-bottom: {LN}; background-image: linear-gradient(90deg, {FG} 1px, transparent 1px); background-size: 12px 100%"></div></div>
<p style="margin: 0; padding: 14px 16px; border-top: {LN}; font-size: 14px; line-height: 1.6">{INTRO}</p>
</div></div></div>
<h1 style="margin: 0; {tek}; font-weight: 800; font-size: clamp(56px, 11vw, 150px); letter-spacing: 0.02em; line-height: 0.9; text-transform: uppercase">Projetos</h1>
<section aria-labelledby="fac-c" style="display: flex; flex-direction: column; gap: 22px">
<div style="display: flex; justify-content: space-between; gap: 16px; padding: 12px 16px; border: {LN}; background: {FG}; color: {BG}; {mono}"><h2 id="fac-c" style="margin: 0; font: inherit; font-weight: 700">//Projetos da faculdade_</h2><span>04 / FAESA</span></div>
{"".join(ficha(p) for p in P)}
</section>
<section aria-labelledby="pes-c" style="position: relative; border: {LN}">{cantos()}
<div style="display: flex; justify-content: space-between; gap: 16px; padding: 12px 16px; border-bottom: {LN}; {mono}"><h2 id="pes-c" style="margin: 0; font: inherit; font-weight: 700">//Projetos pessoais_</h2><span>00</span></div>
<p style="margin: 0; padding: 16px; font-size: 14px; color: {MU}">{PESSOAIS}</p>
</section>
<div style="border: {LN}; padding: 10px 14px">{painel}</div>
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px; {mono}; font-weight: 700; padding-bottom: 8px"><span>Graduação 2022 a 2027</span><span>Enrico Montovanelli</span></div>
</div></div>'''
open(sys.argv[1],"w").write(page("Projetos, modelo C: ficha",fonts,style,body,4100))
