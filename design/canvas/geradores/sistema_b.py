# Gera os modelos da direção B ("dia e noite") para o canvas.
# Duas variantes que dividem o mesmo sistema (papel/negativo, barras de terminal,
# vermelho único, marcas) e mudam só a tipografia de destaque:
#   B1: Tektur larga (a letra do nome no menu atual) + Marcellus nos subtítulos
#   B2: Antonio condensada, em caixa alta, com ponto vermelho (referências "The grid is lying")
# Uso: python3 sistema_b.py  (escreve SistemaB1*.dc.html e SistemaB2*.dc.html em design/canvas/)
import random, pathlib

SAIDA = pathlib.Path(__file__).resolve().parent.parent
W, H = 1440, 960
PAPEL, GRAFITE, NOITE, VERMELHO = "#E8E6E1", "#2E2E2E", "#0E0E0F", "#D21A16"
MONO = "'JetBrains Mono', ui-monospace, monospace"
TEXTO = "'Inter Tight', 'Helvetica Neue', Arial, sans-serif"

VARIANTES = {
    "B1": {
        "fontes": "family=Tektur:wdth,wght@75..125,400..900&amp;family=Marcellus&amp;family=JetBrains+Mono:wght@400;500&amp;family=Inter+Tight:wght@400;500;600",
        "display": "font-family: 'Tektur', system-ui, sans-serif; font-weight: 500; font-stretch: 125%; letter-spacing: 0.01em; text-transform: uppercase",
        "sub": "font-family: 'Marcellus', Georgia, serif; letter-spacing: 0.12em; text-transform: uppercase",
        "ponto": False,
    },
    "B2": {
        "fontes": "family=Antonio:wght@400;700&amp;family=JetBrains+Mono:wght@400;500&amp;family=Inter+Tight:wght@400;500;600",
        "display": "font-family: 'Antonio', 'Arial Narrow', sans-serif; font-weight: 700; letter-spacing: -0.01em; text-transform: uppercase",
        "sub": "font-family: 'Antonio', 'Arial Narrow', sans-serif; font-weight: 700; letter-spacing: 0.02em; text-transform: uppercase",
        "ponto": True,
    },
}

VERMELHO_NOITE = "#EA3E34"  # mesmo vermelho, um pouco mais claro para texto pequeno sobre preto (contraste >= 4.5:1)

DIA = {"fundo": PAPEL, "tinta": GRAFITE, "apagado": "rgba(46,46,46,0.45)", "verm": VERMELHO, "noite": False, "barra": None}
NOITE_P = {"fundo": NOITE, "tinta": PAPEL, "apagado": "rgba(232,230,225,0.42)", "verm": VERMELHO_NOITE, "noite": True, "barra": None}
NOITE_BARRA_PAPEL = dict(NOITE_P, barra=(PAPEL, GRAFITE))

ESTRELA = "M20 0 L22 18 L40 20 L22 22 L20 40 L18 22 L0 20 L18 18 Z"


def grao(fid, noite):
    if noite:
        return (f'<svg aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0.22; mix-blend-mode: screen; pointer-events: none">'
                f'<filter id="{fid}"><feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="3" stitchTiles="stitch"></feTurbulence>'
                f'<feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1.6 -0.55"></feColorMatrix></filter>'
                f'<rect width="100%" height="100%" filter="url(#{fid})"></rect></svg>')
    return (f'<svg aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0.6; mix-blend-mode: multiply; pointer-events: none">'
            f'<filter id="{fid}"><feTurbulence type="fractalNoise" baseFrequency="0.95" numOctaves="3" stitchTiles="stitch"></feTurbulence>'
            f'<feColorMatrix type="saturate" values="0"></feColorMatrix></filter>'
            f'<rect width="100%" height="100%" filter="url(#{fid})"></rect></svg>')


def barra(tinta, esquerda, direita, embaixo=False, cursor=False, fundo=None):
    borda = "border-top" if embaixo else "border-bottom"
    if fundo:
        fundo_barra, tinta = fundo
        extra = f"background: {fundo_barra}; "
    else:
        extra = ""
    cur = (f'<span aria-hidden="true" style="display: inline-block; width: 0.6em; height: 1em; margin-left: 6px; vertical-align: -2px; background: {tinta}"></span>' if cursor else "")
    return (f'<div style="position: relative; display: flex; justify-content: space-between; align-items: center; gap: 24px; padding: 12px 32px; '
            f'font-family: {MONO}; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: {tinta}; {extra}{borda}: 2px solid {tinta}">'
            f'<span>{esquerda}{cur}</span><span style="display: flex; gap: 22px">{direita}</span></div>')


def contatos(tinta):
    return (f'<a href="https://www.linkedin.com/in/enricomontovanelli/" style="color: {tinta}">LinkedIn ↗</a>'
            f'<a href="https://github.com/EnricoMontova" style="color: {tinta}">GitHub ↗</a>'
            f'<a href="#" style="color: {tinta}">Currículo</a>')


def codigo_barras(texto, tinta, altura=26):
    x, partes = 0, []
    for i, c in enumerate(texto.upper()):
        n = ord(c)
        for k in range(3):
            w = 1 + ((n >> k) + i) % 3
            partes.append(f'<rect x="{x}" y="0" width="{w}" height="{altura}"></rect>')
            x += w + 1 + ((n >> (k + 2)) % 2)
    return f'<svg aria-hidden="true" viewBox="0 0 {x} {altura}" style="display: block; height: {altura}px; width: auto; flex: none" fill="{tinta}">{"".join(partes)}</svg>'


def titulo(v, texto, tamanho, tinta):
    ponto = f'<span style="color: {VERMELHO}">.</span>' if v["ponto"] else ""
    estrela = "" if v["ponto"] else (f'<svg aria-hidden="true" viewBox="0 0 40 40" style="position: absolute; right: -10px; top: -16px; width: 30px; height: 30px" fill="{tinta}"><path d="{ESTRELA}"></path></svg>')
    lh = "0.9" if v["ponto"] else "1.02"
    return (f'<div style="position: relative; align-self: flex-start; padding-right: 30px">'
            f'<h1 style="margin: 0; {v["display"]}; font-size: {tamanho}px; line-height: {lh}; color: {tinta}">{texto}{ponto}</h1>{estrela}</div>')


def secao(v, numero, nome, tinta, apagado):
    if v["ponto"]:
        return (f'<div style="display: flex; align-items: flex-end; gap: 16px">'
                f'<div style="display: flex; flex-direction: column; gap: 6px"><span style="{v["display"]}; font-size: 44px; line-height: 0.9; color: {tinta}">{numero}</span>'
                f'<span aria-hidden="true" style="display: block; width: 22px; height: 3px; background: {tinta}"></span></div>'
                f'<span style="font-family: {MONO}; font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: {apagado}; padding-bottom: 2px">{nome}</span>'
                f'<span aria-hidden="true" style="flex: 1; height: 1px; background: {apagado}; margin-bottom: 7px"></span></div>')
    return (f'<div style="display: flex; align-items: center; gap: 14px">'
            f'<span aria-hidden="true" style="width: 7px; height: 7px; background: {tinta}; flex: none"></span>'
            f'<span style="{v["sub"]}; font-size: 17px; color: {tinta}">{nome}</span>'
            f'<span aria-hidden="true" style="flex: 1; height: 1px; background: {apagado}"></span>'
            f'<span style="font-family: {MONO}; font-size: 11px; letter-spacing: 0.1em; color: {apagado}">{numero}</span></div>')


def pagina(titulo_doc, fontes, fundo, corpo):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{titulo_doc}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fontes}&amp;display=swap">
<style>
body{{margin:0;background:{fundo}}}
a{{text-decoration:none}}a:hover{{text-decoration:underline}}
</style>
</helmet>
{corpo}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{W},"height":{H}}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''


def bobinadeira(cor=GRAFITE):
    p = []
    for cx, cy, r0, r1 in ((1230, 170, 62, 215), (180, 650, 52, 150)):
        for r in range(r0, r1, 5):
            p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke-dasharray="{3 + r % 7} 2"></circle>')
        p.append(f'<circle cx="{cx}" cy="{cy}" r="{r0 - 12}"></circle>')
        p.append(f'<path d="M{cx - 30} {cy} H{cx + 30} M{cx} {cy - 30} V{cy + 30}"></path>')
    p.append('<path d="M250 530 L1090 320 M254 540 L1094 330"></path>')
    for k in range(0, 21):
        x = 250 + k * 42; y = 530 - k * 10.5
        p.append(f'<path d="M{x:.0f} {y:.0f} l4 10"></path>')
    random.seed(7)
    for _ in range(46):
        x, y, s = random.randint(0, 1440) // 8 * 8, random.randint(0, 800) // 8 * 8, random.choice((8, 8, 16))
        p.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{cor}" stroke="none" opacity="{random.choice((0.08, 0.12, 0.18))}"></rect>')
    return (f'<svg aria-hidden="true" viewBox="0 0 1440 816" preserveAspectRatio="xMidYMid slice" style="position: absolute; inset: 0; width: 100%; height: 100%" '
            f'fill="none" stroke="{cor}" stroke-width="0.9" opacity="0.55">{"".join(p)}</svg>')


def menu(v, nome, pal=DIA, arte_fundo=True):
    t, bt, ap, vm = pal["tinta"], (pal["barra"][1] if pal["barra"] else pal["tinta"]), pal["apagado"], pal["verm"]
    if v["ponto"]:
        nome_html = (f'<h1 style="margin: 0; {v["display"]}; font-size: 150px; line-height: 0.86; color: {t}">Enrico<br>Montovanelli<span style="color: {vm}">.</span></h1>')
        links = "".join(f'<a href="#" style="{v["sub"]}; font-size: 30px; color: {t}">{rot}</a>' for rot in ("Carreira", "Projetos", "Hobbies"))
    else:
        nome_html = (f'<div style="position: relative; align-self: flex-start; padding-right: 30px">'
                     f'<h1 style="margin: 0; {v["display"]}; font-size: 72px; line-height: 1.05; color: {t}">Enrico Montovanelli</h1>'
                     f'<svg aria-hidden="true" viewBox="0 0 40 40" style="position: absolute; right: -6px; top: -18px; width: 34px; height: 34px" fill="{t}"><path d="{ESTRELA}"></path></svg>'
                     f'<svg aria-hidden="true" viewBox="0 0 600 14" preserveAspectRatio="none" style="display: block; width: 72%; height: 14px; margin-top: 10px" fill="none" stroke="{t}" stroke-width="1.4"><path d="M1 0 V12 H600"></path><path d="M380 12 V6 H430 V12"></path></svg></div>')
        links = "".join(f'<a href="#" style="{v["sub"]}; font-size: 19px; color: {t}">{rot}</a>' for rot in ("Carreira", "Projetos", "Hobbies"))
    apresentacao = "Eng. de Software na automação · ArcelorMittal Tubarão · Eng. da Computação · Vitória, ES"
    corpo = f'''<main style="position: relative; overflow: hidden; width: {W}px; height: {H}px; background: {pal["fundo"]}; color: {t}; display: flex; flex-direction: column">
{barra(t, "Enrico.Montovanelli / portfólio", f"<span>{apresentacao}</span><span>14:10:33</span>", fundo=pal["barra"])}
<div style="position: relative; flex: 1; min-height: 0">
{bobinadeira(t) if arte_fundo else ""}
<div style="position: relative; height: 100%; box-sizing: border-box; padding: 0 0 0 150px; display: flex; flex-direction: column; justify-content: center; gap: 26px">
{nome_html}
<div style="display: flex; align-items: center; gap: 26px; padding-left: 200px">
{codigo_barras("ENRICO", t)}
<nav aria-label="Seções" style="display: flex; gap: 30px">{links}</nav>
<span aria-hidden="true" style="flex: 1; height: 1.4px; background: {t}"></span>
</div>
</div>
</div>
{barra(t, "Selecione uma seção", contatos(bt), embaixo=True, cursor=True, fundo=pal["barra"])}
{grao("g-" + nome, pal["noite"])}
</main>'''
    return pagina(f"Sistema {nome}, menu", v["fontes"], pal["fundo"], corpo)


def carreira(v, nome, pal=DIA):
    t, bt, vm = pal["tinta"], (pal["barra"][1] if pal["barra"] else pal["tinta"]), pal["verm"]
    apagado = pal["apagado"]
    trechos = [("Gol Linhas Aéreas", "Jovem aprendiz, RH", "jul. 2024", 14, False),
               ("Mudanças e Fretes", "Ajudante de mudanças", "set. 2025", 5, False),
               ("ArcelorMittal Tubarão", "Estagiário de Eng. de Software", "fev. 2026", 9, True)]
    total = sum(t[3] for t in trechos)
    segs = ""
    for onde, funcao, inicio, meses, atual in trechos:
        cor = vm if atual else t
        segs += (f'<div style="flex: {meses} 1 0; min-width: 0; display: flex; flex-direction: column; gap: 10px">'
                 f'<span style="font-family: {MONO}; font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: {cor}">{inicio}{" · hoje" if atual else ""} / {meses} meses</span>'
                 f'<div style="position: relative; height: 14px; border-left: 1.4px solid {t}">'
                 f'<span style="position: absolute; left: 0; right: 0; top: 6px; height: {3 if atual else 1.4}px; background: {cor}"></span></div>'
                 f'<span style="font-family: {TEXTO}; font-size: 15px; font-weight: 600; color: {t}">{onde}</span>'
                 f'<span style="font-family: {TEXTO}; font-size: 14px; color: {t}">{funcao}</span></div>')
    cargos = [("ArcelorMittal, Tubarão Aços Planos", "fev. 2026 · hoje", "Automação da LTQ, em sistemas de Nível 2: a camada que liga o controle da planta (Nível 1) à gestão da produção (Nível 3).", True),
              ("Mudanças e Fretes", "set. 2025 · fev. 2026", "Ao lado do meu pai em fretes e mudanças, no carregamento e transporte de móveis.", False),
              ("Gol Linhas Aéreas", "jul. 2024 · set. 2025", "Jovem aprendiz em Recursos Humanos: controle de planilhas e suporte às rotinas administrativas.", False)]
    blocos = ""
    for onde, quando, texto, atual in cargos:
        cor = vm if atual else t
        blocos += (f'<article style="display: flex; flex-direction: column; gap: 12px">'
                   f'<div style="display: flex; align-items: center"><span aria-hidden="true" style="flex: 1; height: 1px; background: {t}"></span><span aria-hidden="true" style="width: 7px; height: 7px; background: {cor}"></span></div>'
                   f'<span style="font-family: {MONO}; font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: {cor}">{"atual · " if atual else ""}{quando}</span>'
                   f'<h3 style="margin: 0; {v["sub"]}; font-size: {26 if v["ponto"] else 18}px; line-height: 1.1; color: {t}">{onde}</h3>'
                   f'<p style="margin: 0; font-family: {TEXTO}; font-size: 15px; line-height: 1.5; color: {t}">{texto}</p></article>')
    certs = [("DataCamp", "12/11/2026", "Intermediate SQL"), ("DataCamp", "06/08/2026", "Introduction to Databricks"), ("DataCamp", "28/04/2026", "Introduction to Shell"), ("Udemy", "21/11/2025", "Java completo: POO + projetos")]
    quadros = "".join(f'<div style="width: 150px; height: 150px; box-sizing: border-box; padding: 12px; border: 1px solid {t}; display: flex; flex-direction: column; justify-content: space-between">'
                      f'<span style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.08em; text-transform: uppercase; display: flex; justify-content: space-between"><span>{p}</span><span>{d}</span></span>'
                      f'<span style="font-family: {TEXTO}; font-size: 14px; font-weight: 600; line-height: 1.25">{c}</span>'
                      f'<span style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.08em; text-transform: uppercase; color: {apagado}">ver certificado ↗</span></div>' for p, d, c in certs)
    corpo = f'''<main style="position: relative; overflow: hidden; width: {W}px; height: {H}px; background: {pal["fundo"]}; color: {t}; display: flex; flex-direction: column">
{barra(t, "Enrico.Montovanelli / carreira", "<span>&lt; /menu</span><span>14:10:33</span>", fundo=pal["barra"])}
<div style="position: relative; flex: 1; min-height: 0; box-sizing: border-box; padding: 44px 64px 36px; display: flex; flex-direction: column; gap: 40px">
<header style="display: flex; justify-content: space-between; align-items: flex-end; gap: 48px">
{titulo(v, "Carreira", 120 if v["ponto"] else 76, t)}
<p style="margin: 0; max-width: 480px; font-family: {TEXTO}; font-size: 18px; line-height: 1.5">Estudante de Engenharia da Computação no 9º período, pela FAESA. Hoje sou estagiário de engenharia de software na automação da Laminação de Tiras a Quente da ArcelorMittal Tubarão.</p>
</header>
<section style="display: flex; flex-direction: column; gap: 22px">
{secao(v, "01", "Trajetória", t, apagado)}
<div style="display: flex; gap: 0; border-right: 1.4px solid {t}">{segs}</div>
</section>
<section style="display: flex; gap: 48px; align-items: flex-start">
<div style="flex: 1; display: flex; flex-direction: column; gap: 22px">
{secao(v, "02", "Experiência", t, apagado)}
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px">{blocos}</div>
</div>
</section>
<section style="display: flex; flex-direction: column; gap: 18px">
{secao(v, "03", "Certificados", t, apagado)}
<div style="display: flex; gap: 16px">{quadros}</div>
</section>
</div>
{barra(t, "&gt; voltar /menu", contatos(bt), embaixo=True, cursor=True, fundo=pal["barra"])}
{grao("g-" + nome, pal["noite"])}
</main>'''
    return pagina(f"Sistema {nome}, Carreira", v["fontes"], pal["fundo"], corpo)


def estrela_particulas(v):
    random.seed(11)
    p = [f'<path d="{ESTRELA}" transform="translate(150 150) scale(4.2) translate(-20 -20)" fill="{PAPEL}"></path>']
    for _ in range(170):
        ang = random.random() * 6.283
        import math
        raio = 40 + abs(random.gauss(0, 1)) * 95
        braco = random.choice((0, 1.5708, 3.1416, 4.7124))
        if random.random() < 0.55:
            ang = braco + random.gauss(0, 0.12)
        x = 150 + math.cos(ang) * raio; y = 150 + math.sin(ang) * raio
        s = random.choice((1.5, 2, 2, 3, 4))
        p.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{s}" height="{s}" fill="{PAPEL}" opacity="{max(0.15, 1 - raio / 260):.2f}"></rect>')
    p.append(f'<circle cx="150" cy="150" r="128" fill="none" stroke="{PAPEL}" stroke-width="0.7" stroke-dasharray="2 5" opacity="0.5"></circle>')
    return f'<svg aria-hidden="true" viewBox="0 0 300 300" style="width: 300px; height: 300px; flex: none">{"".join(p)}</svg>'


def projetos(v, nome, pal=NOITE_P):
    bt, vm = (pal["barra"][1] if pal["barra"] else pal["tinta"]), pal["verm"]
    tinta = pal["tinta"]
    apagado = pal["apagado"]
    proj = [("Projeto integrador · 1º período", "Balança Digital com Arduino", "Balança digital funcional com Arduino, aplicando a Lei de Hooke e conceitos de física, automação e programação.", "Arduino UNO · HC-SR04 · LCD 16x2 · C/C++"),
            ("Apresentado no ESX 2025", "Carrinho de Controle Remoto", "Veículo controlado remotamente com Arduino, sensores ultrassônicos e comunicação sem fio. No ESX 2025, os visitantes controlavam os carrinhos pelo celular.", "Arduino · Bluetooth HC-05 · Motores DC · C/C++"),
            ("Sistemas Embarcados", "Drone com Sistemas Embarcados", "Drone controlado por microcontrolador, com controle de voo e estabilidade por acelerômetro e giroscópio e controle remoto sem fio via ESP32.", "ESP32 · MPU6050 · Motores e hélices · C/C++ · PID"),
            ("Projeto Integrador II", "Detecção de Incêndios IoT", "Monitoramento de temperatura e gases em ambientes industriais e recicladoras, com sensores de chama e gases.", "Arduino · MQ-135 · MLX90614 · C/C++ · IoT")]
    cards = ""
    for i, (ctx, n, d, t) in enumerate(proj, 1):
        destaque = vm if i == 2 else tinta
        cards += (f'<article style="box-sizing: border-box; padding: 18px; border: 1px solid {apagado}; display: flex; flex-direction: column; gap: 14px; min-height: 290px">'
                  f'<div style="display: flex; justify-content: space-between; font-family: {MONO}; font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: {apagado}"><span>02.{i}</span><span style="color: {destaque}">{ctx}</span></div>'
                  f'<h3 style="margin: 0; {v["sub"]}; font-size: {28 if v["ponto"] else 19}px; line-height: 1.15; color: {tinta}">{n}</h3>'
                  f'<p style="margin: 0; font-family: {TEXTO}; font-size: 14px; line-height: 1.5; color: {tinta}">{d}</p>'
                  f'<span style="margin-top: auto; font-family: {MONO}; font-size: 10px; letter-spacing: 0.08em; text-transform: uppercase; color: {apagado}; line-height: 1.6">{t}</span></article>')
    corpo = f'''<main style="position: relative; overflow: hidden; width: {W}px; height: {H}px; background: {NOITE}; color: {tinta}; display: flex; flex-direction: column">
{barra(tinta, "Enrico.Montovanelli / projetos", "<span>&lt; /menu</span><span>14:10:33</span>", fundo=pal["barra"])}
<div style="position: relative; flex: 1; min-height: 0; box-sizing: border-box; padding: 36px 64px 36px; display: flex; flex-direction: column; gap: 30px">
<header style="display: flex; justify-content: space-between; align-items: center; gap: 48px">
<div style="display: flex; flex-direction: column; gap: 22px">
{titulo(v, "Projetos", 120 if v["ponto"] else 76, tinta)}
<p style="margin: 0; max-width: 520px; font-family: {TEXTO}; font-size: 18px; line-height: 1.5">Projetos pessoais e projetos da graduação em Engenharia da Computação, na FAESA.</p>
</div>
{estrela_particulas(v)}
</header>
<section style="display: flex; flex-direction: column; gap: 14px">
{secao(v, "01", "Projetos pessoais", tinta, apagado)}
<p style="margin: 0; font-family: {MONO}; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: {apagado}">Em desenvolvimento.</p>
</section>
<section style="display: flex; flex-direction: column; gap: 18px">
{secao(v, "02", "Projetos da faculdade", tinta, apagado)}
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px">{cards}</div>
</section>
</div>
{barra(tinta, "&gt; voltar /menu", contatos(bt), embaixo=True, cursor=True, fundo=pal["barra"])}
{grao("g-" + nome, True)}
</main>'''
    return pagina(f"Sistema {nome}, Projetos", v["fontes"], NOITE, corpo)


if __name__ == "__main__":
    # B3 e B4: tipografia da B1, tudo em preto (escolha de 25/11/2026)
    for nome, pal in (("B3", NOITE_P), ("B4", NOITE_BARRA_PAPEL)):
        v = VARIANTES["B1"]
        # B3 escolhida em 25/11/2026: menu sem bobinadeira e sem cubinhos
        (SAIDA / f"Sistema{nome}Menu.dc.html").write_text(menu(v, nome + "m", pal, arte_fundo=(nome != "B3")), encoding="utf-8")
        (SAIDA / f"Sistema{nome}Carreira.dc.html").write_text(carreira(v, nome + "c", pal), encoding="utf-8")
        (SAIDA / f"Sistema{nome}Projetos.dc.html").write_text(projetos(v, nome + "p", pal), encoding="utf-8")
    # B3: telas ligadas entre si no canvas (menu, Carreira e Projetos navegáveis)
    import re as _re
    for tela in ("Menu", "Carreira", "Projetos"):
        f = SAIDA / f"SistemaB3{tela}.dc.html"
        h = f.read_text(encoding="utf-8")
        h = _re.sub(r'<a href="#" (style="[^"]*">)(Carreira|Projetos)</a>', lambda m: f'<a href="SistemaB3{m.group(2)}.dc.html" {m.group(1)}{m.group(2)}</a>', h)
        h = h.replace('<a href="#" style="color: #E8E6E1">Currículo</a>', '<a href="SistemaB3Carreira.dc.html" style="color: #E8E6E1">Currículo</a>')
        h = h.replace('<span>&lt; /menu</span>', '<a href="SistemaB3Menu.dc.html" style="color: #E8E6E1">&lt; /menu</a>')
        h = h.replace('<span>&gt; voltar /menu', '<span><a href="SistemaB3Menu.dc.html" style="color: #E8E6E1">&gt; voltar /menu</a>')
        f.write_text(h, encoding="utf-8")
    for nome, v in VARIANTES.items():
        (SAIDA / f"Sistema{nome}Menu.dc.html").write_text(menu(v, nome + "m"), encoding="utf-8")
        (SAIDA / f"Sistema{nome}Carreira.dc.html").write_text(carreira(v, nome + "c"), encoding="utf-8")
        (SAIDA / f"Sistema{nome}Projetos.dc.html").write_text(projetos(v, nome + "p"), encoding="utf-8")
    print("ok")
