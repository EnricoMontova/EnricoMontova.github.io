import sys, json; sys.path.insert(0,'/home/claude/gen')
from data import *; from svgs import *
BG="#D9DDD3"; INK="#141414"; MU="#454842"; RED="#D21A16"; LN=f"1px solid {INK}"
fonts="family=Space+Grotesk:wght@500;700&amp;family=IBM+Plex+Mono:wght@400;500;600"
style=f"""body{{margin:0;background:{BG}}}
a{{color:{INK}}}a:hover{{color:{RED}}}
a:focus-visible,button:focus-visible{{outline:2px solid {RED};outline-offset:2px}}
@keyframes pisca{{0%,49%{{opacity:1}}50%,100%{{opacity:0.2}}}}
@media (prefers-reduced-motion: reduce){{.pisca{{animation:none !important}}}}
@media (max-width: 900px){{.lado-d{{flex-basis:100% !important}}.dir-d{{grid-template-columns:minmax(0,1fr) !important}}}}"""
mono="font-family: 'IBM Plex Mono', ui-monospace, monospace; font-size: 12px; letter-spacing: 0.04em; text-transform: uppercase"
grot="font-family: 'Space Grotesk', 'Helvetica Neue', sans-serif"
bw,bc=barcode("221126",26,INK,1)
def cantos():
    s=f"position: absolute; width: 10px; height: 10px; border-color: {INK}; border-style: solid;"
    return (f'<span aria-hidden="true" style="{s} left: 8px; top: 8px; border-width: 1px 0 0 1px"></span>'
            f'<span aria-hidden="true" style="{s} right: 8px; top: 8px; border-width: 1px 1px 0 0"></span>'
            f'<span aria-hidden="true" style="{s} left: 8px; bottom: 8px; border-width: 0 0 1px 1px"></span>'
            f'<span aria-hidden="true" style="{s} right: 8px; bottom: 8px; border-width: 0 1px 1px 0"></span>')
dados=[dict(n=p["n"],titulo=p["titulo"],curto=p["curto"].upper(),ctx=p["ctx"],desc=p["desc"],
            hw=" / ".join(p["hw"]),sw=" / ".join(p["sw"]),techs=[{"t":t} for t in p["hw"]+p["sw"]],
            dest=p["dest"] or "",temDest=bool(p["dest"]),apr=p["apr"] or "",temApr=bool(p["apr"]),ehDrone=p["curto"]=="Drone",ehBalanca=p["curto"]=="Balança",ehCarrinho=p["curto"]=="Carrinho",ehIncendio=p["curto"]=="Incêndios IoT",semImg=not p["img"]) for p in P]
script="""class Component extends DCLogic {
constructor(props) { super(props); this.state = { sel: 0 }; }
renderVals() {
const dados = %s;
const sel = this.state.sel;
const lista = dados.map((p, i) => ({ ...p, ativo: i === sel, inativo: i !== sel, pick: () => this.setState({ sel: i }) }));
return { lista: lista, p: dados[sel] };
}
}"""%json.dumps(dados,ensure_ascii=False)
item=f'''<sc-for list="{{{{lista}}}}" as="item" hint-placeholder-count="4">
<li style="border-bottom: {LN}">
<sc-if value="{{{{item.ativo}}}}" hint-placeholder-val="{{{{false}}}}"><button type="button" onClick="{{{{item.pick}}}}" aria-pressed="true" style="width: 100%; text-align: left; border: 0; margin: 0; padding: 14px 16px; background: {INK}; color: {BG}; cursor: pointer; display: flex; flex-direction: column; gap: 6px; {mono}"><span style="font-weight: 600">[{{{{item.curto}}}}]</span><span style="text-transform: none; letter-spacing: 0">- {{{{item.ctx}}}}</span><span style="font-size: 10px; line-height: 1.5; opacity: 0.85">{{{{item.hw}}}}</span><span aria-hidden="true" style="height: 3px; background: {RED}; margin-top: 4px"></span></button></sc-if>
<sc-if value="{{{{item.inativo}}}}" hint-placeholder-val="{{{{true}}}}"><button type="button" onClick="{{{{item.pick}}}}" aria-pressed="false" style="width: 100%; text-align: left; border: 0; margin: 0; padding: 14px 16px; background: transparent; color: {INK}; cursor: pointer; display: flex; flex-direction: column; gap: 6px; {mono}"><span style="font-weight: 600">[{{{{item.curto}}}}]</span><span style="text-transform: none; letter-spacing: 0; color: {MU}">- {{{{item.ctx}}}}</span><span style="font-size: 10px; line-height: 1.5; color: {MU}">{{{{item.hw}}}}</span><span aria-hidden="true" style="height: 3px; background: {INK}; opacity: 0.25; margin-top: 4px"></span></button></sc-if>
</li>
</sc-for>'''
painel=lambda tit,conteudo: f'<div style="border: {LN}; display: flex; flex-direction: column"><h3 style="margin: 0; padding: 10px 14px; border-bottom: {LN}; {grot}; font-weight: 700; font-size: 15px; text-transform: uppercase; letter-spacing: 0.02em">{tit}</h3><div style="padding: 14px">{conteudo}</div></div>'
techs=f'<ul style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 8px; {mono}"><sc-for list="{{{{p.techs}}}}" as="t" hint-placeholder-count="4"><li style="display: flex; align-items: center; gap: 10px"><span aria-hidden="true" style="width: 6px; height: 6px; background: {INK}"></span>{{{{t.t}}}}</li></sc-for></ul>'
dest=f'<sc-if value="{{{{p.temDest}}}}" hint-placeholder-val="{{{{false}}}}">{painel("Destaque", f"<p style=\"margin: 0; {mono}; text-transform: none; font-size: 13px; line-height: 1.5\"><span style=\"color: {RED}\">●</span> {{{{p.dest}}}}</p>")}</sc-if>'
apr=f'<sc-if value="{{{{p.temApr}}}}" hint-placeholder-val="{{{{true}}}}">{painel("Aprendizados", f"<p style=\"margin: 0; font-size: 14px; line-height: 1.5\">{{{{p.apr}}}}</p>")}</sc-if>'
malha=f'<svg viewBox="0 0 760 360" aria-hidden="true" style="width: 100%; height: auto; display: block">{mesh(760,360,INK)}</svg>'
body=f'''<div style="position: relative; background: {BG}; color: {INK}; {grot}; font-size: 15px">
<div style="max-width: 1400px; margin: 0 auto; padding: clamp(12px, 2vw, 24px); box-sizing: border-box">
<div style="border: {LN}; display: flex; flex-direction: column">
<header style="display: flex; flex-wrap: wrap; border-bottom: {LN}">
<div style="padding: 12px 16px; border-right: {LN}; display: flex; flex-direction: column; gap: 4px"><span style="{mono}; font-size: 10px">Projetos / registro</span><span style="font-weight: 700; font-size: 28px; letter-spacing: 0.02em">22.11.26</span><svg viewBox="0 0 {bw} 26" aria-hidden="true" style="width: 120px; height: 14px">{bc}</svg></div>
<div style="flex: 1 1 380px; padding: 12px 20px; border-right: {LN}; display: flex; flex-direction: column; justify-content: center; gap: 6px"><h1 style="margin: 0; font-weight: 700; font-size: clamp(22px, 2.4vw, 34px); text-transform: uppercase; letter-spacing: 0.01em">Projetos / Enrico Montovanelli</h1><span style="{mono}">Sistemas embarcados · IoT · Automação</span></div>
<div style="padding: 12px 16px; border-right: {LN}; display: flex; flex-direction: column; justify-content: center; gap: 4px; {mono}"><span style="font-size: 10px">Status</span><span style="font-weight: 600"><span class="pisca" style="color: {RED}; animation: pisca 1.2s steps(1) infinite">●</span> 4 projetos</span></div>
<div style="padding: 12px 16px; display: flex; align-items: center"><a href="Main.dc.html" style="{mono}; font-weight: 600; padding: 10px 0">Voltar ao menu</a></div>
</header>
<div style="display: flex; flex-wrap: wrap">
<nav class="lado-d" aria-label="Projetos" style="flex: 0 0 280px; border-right: {LN}"><h2 style="margin: 0; padding: 10px 16px; border-bottom: {LN}; background: {INK}; color: {BG}; {mono}; font-weight: 600">Projetos da faculdade</h2><ul style="list-style: none; margin: 0; padding: 0">{item}</ul><div style="border-bottom: {LN}"><h2 style="margin: 0; padding: 10px 16px; border-bottom: {LN}; {mono}; font-weight: 600">Projetos pessoais</h2><p style="margin: 0; padding: 14px 16px; {mono}; text-transform: none; color: {MU}">{PESSOAIS}</p></div>
<p style="margin: 0; padding: 14px 16px; font-size: 14px; line-height: 1.5; color: {MU}">{INTRO}</p></nav>
<div style="flex: 999 1 560px; min-width: 0; display: grid; grid-template-columns: minmax(0, 1fr) 300px" class="dir-d">
<main style="position: relative; padding: 24px; border-right: {LN}; display: flex; flex-direction: column; gap: 14px">{cantos()}
<div style="display: flex; justify-content: space-between; gap: 16px; {mono}"><span>Projeto {{{{p.n}}}} / 04</span><span>{{{{p.ctx}}}}</span></div>
<h2 style="margin: 0; color: {RED}; font-weight: 700; font-size: clamp(30px, 3.6vw, 48px); line-height: 1; text-transform: uppercase">{{{{p.titulo}}}}</h2>
<p style="margin: 0; max-width: 62ch; font-size: 17px; line-height: 1.5">{{{{p.desc}}}}</p>
{malha}
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px; {mono}; color: {MU}"><span>▸ Hardware: {{{{p.hw}}}}</span><span>▸ Software: {{{{p.sw}}}}</span></div>
</main>
<aside style="padding: 14px; display: flex; flex-direction: column; gap: 14px">
{painel("Tecnologias", techs)}
{dest}
{apr}
<sc-if value="{{{{p.ehDrone}}}}" hint-placeholder-val="{{{{false}}}}"><div style="display: flex; flex-direction: column; gap: 8px"><figure style="position: relative; margin: 0; border: {LN}; aspect-ratio: 9 / 16; overflow: hidden"><img src="/_blob/2a88d5f937183687928c5371716eb1dc" alt="Estrutura do drone com quatro motores e hélices, ligada a uma protoboard e a uma bateria, com multímetro na bancada" style="display: block; width: 100%; height: 100%; object-fit: cover"></figure>{thumbs(P[0],LN,mono+"; font-size: 10px; color: "+MU+"; line-height: 1.3")}</div></sc-if>
<sc-if value="{{{{p.ehCarrinho}}}}" hint-placeholder-val="{{{{false}}}}"><div style="display: flex; flex-direction: column; gap: 8px"><figure style="position: relative; margin: 0; border: {LN}; aspect-ratio: 9 / 16; overflow: hidden"><img src="/_blob/91f431831a592875852f0318446f9fcc" alt="Carrinho com rodas amarelas e carenagem decorada com o nome Macarena Racing, sobre uma mesa de vidro" style="display: block; width: 100%; height: 100%; object-fit: cover"></figure>{thumbs(P[1],LN,mono+"; font-size: 10px; color: "+MU+"; line-height: 1.3")}</div></sc-if>
<sc-if value="{{{{p.ehIncendio}}}}" hint-placeholder-val="{{{{false}}}}"><div style="display: flex; flex-direction: column; gap: 8px"><figure style="position: relative; margin: 0; border: {LN}; aspect-ratio: 9 / 16; overflow: hidden"><img src="/_blob/2ed4a68b0720300c77aa98dd02766a70" alt="Montagem em protoboard com módulos de sensores de gás e temperatura ligados a um Arduino UNO conectado ao notebook" style="display: block; width: 100%; height: 100%; object-fit: cover"></figure>{thumbs(P[2],LN,mono+"; font-size: 10px; color: "+MU+"; line-height: 1.3")}</div></sc-if>
<sc-if value="{{{{p.ehBalanca}}}}" hint-placeholder-val="{{{{false}}}}"><div style="display: flex; flex-direction: column; gap: 8px"><figure style="position: relative; margin: 0; border: {LN}; aspect-ratio: 9 / 16; overflow: hidden"><img src="/_blob/4d13a81d802c92c9e676fad8afc1943b" alt="Balança em caixa de acrílico com molas, com um peso metálico sobre a plataforma e o display LCD marcando Peso KG 4.494" style="display: block; width: 100%; height: 100%; object-fit: cover"></figure>{thumbs(P[3],LN,mono+"; font-size: 10px; color: "+MU+"; line-height: 1.3")}</div></sc-if>
<sc-if value="{{{{p.semImg}}}}" hint-placeholder-val="{{{{false}}}}"><div style="position: relative; border: {LN}; aspect-ratio: 9 / 16; display: flex; align-items: flex-end; padding: 12px; box-sizing: border-box">{cantos()}<span style="{mono}; font-size: 11px; color: {MU}">[Foto do projeto]</span></div></sc-if>
</aside>
</div></div>
<footer style="border-top: {LN}; display: flex; flex-wrap: wrap; {mono}; font-size: 11px">
<span style="padding: 10px 14px; border-right: {LN}"><span style="color: {RED}">●</span> Rec</span>
<span style="flex: 1; padding: 10px 14px; border-right: {LN}">Engenharia da Computação · FAESA · ArcelorMittal Tubarão · Nível 2</span>
<span style="padding: 10px 14px">Enrico Montovanelli</span>
</footer>
</div></div></div>'''
open(sys.argv[1],"w").write(page("Projetos, modelo D: painel",fonts,style,body,1500,script=script))
