"""Gera as imagens do README do perfil do GitHub (repositório EnricoMontova/EnricoMontova).

Uso: python design/readme-github/gerar.py PASTA_DE_SAIDA
Saída: banner.svg (cabeçalho) e rodape.svg (rodapé), no sistema visual B3 do site.

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


def main():
    saida = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI / "saida"
    saida.mkdir(parents=True, exist_ok=True)
    texto_mono = TOPO_ESQ + TOPO_DIR + BAIXO_ESQ + BAIXO_DIR + RODAPE_ESQ + RODAPE_DIR
    t, ft = fonte("tektur-latin-standard-normal.woff2", NOME, {"wdth": 100, "wght": 500})
    m, fm = fonte("jetbrains-mono-latin-400-normal.woff2", texto_mono)
    c, fc = fonte("marcellus-latin-400-normal.woff2", AREAS)
    (saida / "banner.svg").write_text(banner(t, m, c, ft, fm, fc), encoding="utf-8")
    (saida / "rodape.svg").write_text(rodape(m), encoding="utf-8")
    print(saida / "banner.svg", saida / "rodape.svg")


if __name__ == "__main__":
    main()
