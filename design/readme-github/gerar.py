"""Gera as imagens do README do perfil do GitHub (repositório EnricoMontova/EnricoMontova).

Uso: python design/readme-github/gerar.py PASTA_DE_SAIDA
Saída: banner.svg (cabeçalho), rodape.svg (rodapé) e tecnologias.svg (painel), no sistema visual B3 do site.

O GitHub não aceita CSS nem fontes no README, então o visual vai dentro das imagens SVG,
com as fontes do site embutidas (só as letras usadas) e o grão por filtro.
"""

import base64
import io
import re
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

RAIZ = Path(__file__).resolve().parents[2]
FONTES = RAIZ / "curriculo" / "fontes"
AQUI = Path(__file__).resolve().parent

PRETO, PAPEL, VERMELHO = "#0E0E0F", "#E8E6E1", "#D21A16"
W = 1280

NOME = "ENRICO MONTOVANELLI"
TOPO_ESQ = "ENRICO.MONTOVANELLI / GITHUB"
TOPO_DIR = "ENRICOMONTOVA.GITHUB.IO"
AREAS = "AUTOMAÇÃO   SOFTWARE   DADOS"
BAIXO_ESQ = "> ARCELORMITTAL TUBARÃO · FAESA · VITÓRIA, ES"
BAIXO_DIR = "2026"
RODAPE_ESQ = "ENRICO MONTOVANELLI · 2026"
RODAPE_DIR = "ENRICOMONTOVA.GITHUB.IO"


def fonte(arquivo, texto, inst=None):
    f = TTFont(FONTES / arquivo)
    if inst:
        f = instancer.instantiateVariableFont(f, inst)
    op = subset.Options()
    op.flavor = "woff2"
    s = subset.Subsetter(op)
    s.populate(text=texto)
    s.subset(f)
    f.flavor = "woff2"
    b = io.BytesIO()
    f.save(b)
    medir = TTFont(io.BytesIO(b.getvalue()))
    return base64.b64encode(b.getvalue()).decode(), medir


def largura(fnt, texto, tamanho, espaco=0.0):
    cmap, hm, upm = fnt.getBestCmap(), fnt["hmtx"], fnt["head"].unitsPerEm
    return sum(hm[cmap[ord(c)]][0] for c in texto) / upm * tamanho + espaco * tamanho * len(texto)


def estilo(t, m, c):
    return (
        "<style>"
        f"@font-face{{font-family:T;src:url(data:font/woff2;base64,{t}) format('woff2')}}"
        f"@font-face{{font-family:M;src:url(data:font/woff2;base64,{m}) format('woff2')}}"
        f"@font-face{{font-family:C;src:url(data:font/woff2;base64,{c}) format('woff2')}}"
        f".m{{font-family:M,monospace;font-size:15px;letter-spacing:.08em;fill:{PAPEL}}}"
        "</style>"
    )


GRAO = (
    '<filter id="g"><feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="3" stitchTiles="stitch"/>'
    '<feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1.6 -0.55"/></filter>'
)
ESTRELA = "M20 0 L22 18 L40 20 L22 22 L20 40 L18 22 L0 20 L18 18 Z"


def cursor(x, y):
    return (f'<rect x="{x:.1f}" y="{y - 13}" width="9" height="16" fill="{PAPEL}">'
            '<animate attributeName="opacity" values="1;0" keyTimes="0;0.5" dur="1s" calcMode="discrete" repeatCount="indefinite"/></rect>')


def banner(t, m, c, ft, fm, fc):
    H = 380
    barras = AQUI.joinpath("codigo-de-barras.svg").read_text(encoding="utf-8")
    rects = "".join(re.findall(r"<rect[^>]*>(?:</rect>)?", barras)).replace("></rect>", "/>")

    tam_nome = 80
    x_nome = 110
    w_nome = largura(ft, NOME, tam_nome, 0.01)
    x_estrela = x_nome + w_nome + 6

    tam_areas = 19
    x_areas = 330
    w_areas = largura(fc, AREAS, tam_areas, 0.12)

    passo_mono = 15 * 0.6 + 15 * 0.08
    x_cursor = 32 + len(BAIXO_ESQ) * passo_mono + 4

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Enrico Montovanelli">
<title>Enrico Montovanelli</title>
<defs>{estilo(t, m, c)}{GRAO}</defs>
<rect width="{W}" height="{H}" fill="{PRETO}"/>
<rect width="{W}" height="{H}" filter="url(#g)" opacity=".22" style="mix-blend-mode:screen"/>
<text class="m" x="32" y="35">{TOPO_ESQ}</text>
<text class="m" x="{W - 32}" y="35" text-anchor="end">{TOPO_DIR}</text>
<rect x="0" y="56" width="{W}" height="2" fill="{PAPEL}"/>
<text x="{x_nome}" y="200" font-family="T" font-weight="500" font-size="{tam_nome}" letter-spacing=".01em" fill="{PAPEL}">{NOME}</text>
<path d="{ESTRELA}" fill="{PAPEL}" transform="translate({x_estrela:.1f},112) scale(.85)"/>
<g fill="none" stroke="{PAPEL}" stroke-width="1.6"><path d="M{x_nome + 1} 218 V230 H{x_nome + w_nome * 0.72:.0f}"/><path d="M{x_nome + w_nome * 0.48:.0f} 230 V224 H{x_nome + w_nome * 0.48 + 40:.0f} V230"/></g>
<g fill="{PAPEL}" transform="translate(110,262)">{rects}</g>
<text x="{x_areas}" y="282" font-family="C" font-size="{tam_areas}" letter-spacing=".12em" fill="{PAPEL}" xml:space="preserve">{AREAS}</text>
<rect x="{x_areas + w_areas + 22:.0f}" y="275" width="{W - (x_areas + w_areas + 22):.0f}" height="1.4" fill="{PAPEL}"/>
<rect x="0" y="322" width="{W}" height="2" fill="{PAPEL}"/>
<text class="m" x="32" y="357">{BAIXO_ESQ}</text>
{cursor(x_cursor, 357)}
<rect x="{W - 32 - 4 * passo_mono - 22:.1f}" y="345" width="7" height="7" fill="{VERMELHO}"/>
<text class="m" x="{W - 32}" y="357" text-anchor="end">{BAIXO_DIR}</text>
</svg>
"""


def rodape(m):
    H = 64
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="enricomontova.github.io">
<defs><style>@font-face{{font-family:M;src:url(data:font/woff2;base64,{m}) format('woff2')}}.m{{font-family:M,monospace;font-size:15px;letter-spacing:.08em;fill:{PAPEL}}}</style>{GRAO}</defs>
<rect width="{W}" height="{H}" fill="{PRETO}"/>
<rect width="{W}" height="{H}" filter="url(#g)" opacity=".22" style="mix-blend-mode:screen"/>
<rect x="0" y="0" width="{W}" height="2" fill="{PAPEL}"/>
<text class="m" x="32" y="39">{RODAPE_ESQ}</text>
<text class="m" x="{W - 32}" y="39" text-anchor="end">{RODAPE_DIR}</text>
</svg>
"""


# ---------------------------------------------------------------- painel de tecnologias

CINZA = "#A3A19C"
ESTAGIO = [  # (ícone, nome, contexto)
    ("c", "C", "TRU64 UNIX"),
    ("cplusplus", "C++", "TRU64 UNIX"),
    ("csharp", "C#", "WINDOWS 10"),
    ("visualbasic", "VB6", "WINDOWS XP"),
    ("java", "JAVA", "DATA LAKE"),
    ("sql", "SQL", "DATA LAKE · BI"),
    ("databricks", "DATABRICKS", "BI"),
    ("terminal", "TRU64 UNIX", "LEVEL 2"),
    ("windows", "WINDOWS", "XP · 10"),
]
ESTUDOS = [
    ("arduino", "ARDUINO", "IOT · ESX 2025"),
    ("espressif", "ESP32", "DRONE"),
    ("datacamp", "DATACAMP", "DATA ENG."),
]
TITULO_1 = "ESTÁGIO / INTERNSHIP"
TITULO_2 = "ESTUDOS E PROJETOS / STUDIES AND PROJECTS"


def icone(nome, x, y, tam):
    src = AQUI.joinpath("icones", nome + ".svg").read_text(encoding="utf-8")
    vb = re.search(r'viewBox="([^"]+)"', src).group(1)
    corpo = re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", src.strip(), flags=re.S)
    corpo = re.sub(r'<title>.*?</title>', "", corpo, flags=re.S)
    corpo = re.sub(r'\s(fill|style|stroke)="[^"]*"', "", corpo)
    return f'<svg x="{x:.1f}" y="{y:.1f}" width="{tam}" height="{tam}" viewBox="{vb}" fill="{PAPEL}">{corpo}</svg>'


def caixa(x, y, w, h, titulo):
    cantos = "".join(f'<rect x="{cx - 3.5:.1f}" y="{cy - 3.5:.1f}" width="7" height="7" fill="{PAPEL}"/>'
                     for cx, cy in [(x, y), (x + w, y), (x, y + h), (x + w, y + h)])
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{PAPEL}" stroke-width="1"/>{cantos}'
            f'<rect x="{x}" y="{y + 40}" width="{w}" height="1" fill="{PAPEL}"/>'
            f'<rect x="{x + 20}" y="{y + 17}" width="7" height="7" fill="{PAPEL}"/>'
            f'<text x="{x + 38}" y="{y + 26}" font-family="C" font-size="15" letter-spacing=".12em" fill="{PAPEL}">{titulo}</text>')


def cartoes(lista, x0, y0, cw, ch, gap):
    out = []
    for i, (ic, nome, ctx) in enumerate(lista):
        x = x0 + i * (cw + gap)
        cx = x + cw / 2
        out.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="{ch}" fill="none" stroke="{PAPEL}" stroke-opacity=".35"/>')
        out.append(icone(ic, cx - 22, y0 + 20, 44))
        out.append(f'<text class="m" x="{cx:.1f}" y="{y0 + 92}" text-anchor="middle" font-size="13">{nome}</text>')
        out.append(f'<text class="m" x="{cx:.1f}" y="{y0 + 112}" text-anchor="middle" font-size="10.5" style="fill:{CINZA}">{ctx}</text>')
    return "".join(out)


def tecnologias(m, c):
    cw, ch, gap = 120, 128, 12
    pad = 20
    x0 = 32
    w1 = len(ESTAGIO) * cw + (len(ESTAGIO) - 1) * gap + 2 * pad
    W2 = w1 + 2 * x0
    y1 = 24
    h1 = 40 + pad + ch + pad
    y2 = y1 + h1 + 28
    H = y2 + h1 + 24
    barras = AQUI.joinpath("codigo-de-barras.svg").read_text(encoding="utf-8")
    rects = "".join(re.findall(r"<rect[^>]*>(?:</rect>)?", barras)).replace("></rect>", "/>")
    x_barras = x0 + pad + len(ESTUDOS) * (cw + gap) + 24
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W2} {H}" width="{W2}" height="{H}" role="img" aria-label="Tecnologias / Technologies">
<title>Tecnologias / Technologies</title>
<defs><style>@font-face{{font-family:M;src:url(data:font/woff2;base64,{m}) format('woff2')}}@font-face{{font-family:C;src:url(data:font/woff2;base64,{c}) format('woff2')}}.m{{font-family:M,monospace;letter-spacing:.08em;fill:{PAPEL}}}</style>{GRAO}</defs>
<rect width="{W2}" height="{H}" fill="{PRETO}"/>
<rect width="{W2}" height="{H}" filter="url(#g)" opacity=".22" style="mix-blend-mode:screen"/>
{caixa(x0, y1, w1, h1, TITULO_1)}
{cartoes(ESTAGIO, x0 + pad, y1 + 40 + pad, cw, ch, gap)}
{caixa(x0, y2, w1, h1, TITULO_2)}
{cartoes(ESTUDOS, x0 + pad, y2 + 40 + pad, cw, ch, gap)}
<g fill="{PAPEL}" transform="translate({x_barras},{y2 + 40 + pad + ch / 2 - 13:.0f})">{rects}</g>
<rect x="{x_barras + 187 + 20}" y="{y2 + 40 + pad + ch / 2:.0f}" width="{x0 + w1 - pad - (x_barras + 207)}" height="1.4" fill="{PAPEL}"/>
</svg>
"""


def fontes_atividade(saida):
    """Fontes (só os caracteres necessários) para o script do painel de atividade, que roda no GitHub Actions."""
    import json
    mono_txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÃÂÇÉÊÍÓÔÕÚabcdefghijklmnopqrstuvwxyzáãâçéêíóôõú0123456789 /·%-.,:()>+#_"
    t, _ = fonte("tektur-latin-standard-normal.woff2", "0123456789", {"wdth": 100, "wght": 500})
    m, _ = fonte("jetbrains-mono-latin-400-normal.woff2", mono_txt)
    (saida.parent / "scripts").mkdir(parents=True, exist_ok=True)
    (saida.parent / "scripts" / "fontes.json").write_text(json.dumps({"tektur": t, "mono": m}), encoding="utf-8")


def main():
    saida = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI / "saida"
    saida.mkdir(parents=True, exist_ok=True)
    texto_mono = TOPO_ESQ + TOPO_DIR + BAIXO_ESQ + BAIXO_DIR + RODAPE_ESQ + RODAPE_DIR
    texto_mono += "".join(n + c_ for _, n, c_ in ESTAGIO + ESTUDOS)
    t, ft = fonte("tektur-latin-standard-normal.woff2", NOME, {"wdth": 100, "wght": 500})
    m, fm = fonte("jetbrains-mono-latin-400-normal.woff2", texto_mono)
    c, fc = fonte("marcellus-latin-400-normal.woff2", AREAS + TITULO_1 + TITULO_2)
    (saida / "banner.svg").write_text(banner(t, m, c, ft, fm, fc), encoding="utf-8")
    (saida / "rodape.svg").write_text(rodape(m), encoding="utf-8")
    (saida / "tecnologias.svg").write_text(tecnologias(m, c), encoding="utf-8")
    fontes_atividade(saida)
    print(saida / "banner.svg", saida / "rodape.svg", saida / "tecnologias.svg", saida.parent / "scripts" / "fontes.json")


if __name__ == "__main__":
    main()
