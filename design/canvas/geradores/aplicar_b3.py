# Aplica o sistema B3 (tipografia da B1 com estética preta, escolhido em 25/11/2026)
# às três páginas do site.
# Entrada: as páginas da versão anterior, guardadas em versoes/2026-11-25-tres-estilos/
# Saída: index.html, carreira.html e projetos.html na raiz do repositório.
# Uso: python3 design/canvas/geradores/aplicar_b3.py
import pathlib, re

RAIZ = pathlib.Path(__file__).resolve().parents[3]
ORIGEM = RAIZ / "versoes" / "2026-11-25-tres-estilos"


def ler(nome):
    # as cópias guardadas apontam para ../../assets/; na raiz o caminho volta a ser assets/
    return (ORIGEM / nome).read_text(encoding="utf-8").replace('"../../assets/', '"assets/')

NOITE, PAPEL, GRAFITE = "#0E0E0F", "#E8E6E1", "#2E2E2E"
VERM_TEXTO = "#EA3E34"
MONO = "'JetBrains Mono', ui-monospace, monospace"
FONTES = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Tektur:wdth,wght@75..125,400..900'
          '&amp;family=Marcellus&amp;family=JetBrains+Mono:wght@400;500&amp;family=Inter+Tight:wght@400;500;600;700;800&amp;display=swap">')
ESTRELA = '<svg aria-hidden="true" viewBox="0 0 40 40" style="position: absolute; right: -8px; top: -14px; width: 30px; height: 30px" fill="#E8E6E1"><path d="M20 0 L22 18 L40 20 L22 22 L20 40 L18 22 L0 20 L18 18 Z"></path></svg>'

# grão para fundo preto: ruído claro em modo "screen"
def grao(fid, opacidade="0.22"):
    return (f'<svg aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%; opacity: {opacidade}; mix-blend-mode: screen; pointer-events: none">'
            f'<filter id="{fid}"><feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="3" stitchTiles="stitch"></feTurbulence>'
            f'<feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1.6 -0.55"></feColorMatrix></filter>'
            f'<rect width="100%" height="100%" filter="url(#{fid})"></rect></svg>')

CSS_COMUM = """.item-t{display:inline-block;padding:4px 6px;margin:-4px -6px;color:#E8E6E1}
.item-t:hover,.item-t:focus-visible{background:#E8E6E1;color:#0E0E0F;outline:none}
.barra-b3{position:relative;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:10px 24px;padding:12px clamp(16px,3vw,32px);font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:#E8E6E1}
.barra-b3 a{color:#E8E6E1;text-decoration:none}
.contatos{display:flex;flex-wrap:wrap;gap:6px 22px;list-style:none;margin:0;padding:0}
@keyframes cursor-b3{0%,49%{opacity:1}50%,100%{opacity:0}}
"""


def barra_topo(pagina):
    return (f'<header class="barra-b3" style="border-bottom: 2px solid #E8E6E1">'
            f'<span>Enrico.Montovanelli / {pagina}</span>'
            f'<span style="display: flex; gap: 22px"><a class="item-t" href="index.html" data-transicao="&gt; voltar /menu">&lt; /menu</a><span id="hora">00:00:00</span></span></header>')


def barra_baixo():
    return ('<footer class="barra-b3" style="border-top: 2px solid #E8E6E1">'
            '<span>&gt; voltar /menu<span class="pisca" aria-hidden="true" style="display: inline-block; width: 0.6em; height: 1em; margin-left: 6px; vertical-align: -2px; background: #E8E6E1; animation: cursor-b3 1s steps(1) infinite"></span></span>'
            '<nav aria-label="Contato"><ul class="contatos">'
            '<li><a class="item-t" href="https://www.linkedin.com/in/enricomontovanelli/" target="_blank" rel="noopener">LinkedIn ↗</a></li>'
            '<li><a class="item-t" href="https://github.com/EnricoMontova" target="_blank" rel="noopener">GitHub ↗</a></li>'
            '<li><a class="item-t" href="carreira.html" data-transicao="&gt; abrir /carreira">Currículo</a></li>'
            '</ul></nav></footer>')


RELOGIO = """<script>
// relógio da barra de cima
(function () {
  var el = document.getElementById('hora'); if (!el) return;
  var p = function (n) { return (n < 10 ? '0' : '') + n; };
  function tick() { var d = new Date(); el.textContent = p(d.getHours()) + ':' + p(d.getMinutes()) + ':' + p(d.getSeconds()); }
  tick(); setInterval(tick, 1000);
})();
</script>
"""


def troca(s, a, b, n=1):
    assert s.count(a) == n, (a[:80], s.count(a))
    return s.replace(a, b)


def capa_preta(s):
    # transição de scanner no negativo: capa preta, texto e barra claros
    s = re.sub(r'(\.tela-scan\{[^}]*?)background:#E8E6E1', r'\1background:#0E0E0F', s)
    s = s.replace('.barra-scan{position:fixed;left:0;right:0;top:0;height:3px;z-index:51;pointer-events:none;background:#2E2E2E;box-shadow:0 -18px 36px rgba(46,46,46,0.22),0 0 0 1px rgba(46,46,46,0.1)}',
                  '.barra-scan{position:fixed;left:0;right:0;top:0;height:3px;z-index:51;pointer-events:none;background:#E8E6E1;box-shadow:0 -18px 36px rgba(232,230,225,0.16),0 0 0 1px rgba(232,230,225,0.1)}')
    i = s.index('id="capa"'); j = s.index('</div>', i)
    capa = s[i:j]
    capa_n = re.sub(r'<svg aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0.5; mix-blend-mode: multiply; pointer-events: none">.*?</svg>',
                    grao("grao-in", "0.18"), capa)
    capa_n = capa_n.replace('color: #2E2E2E', 'color: #E8E6E1').replace('background: #2E2E2E', 'background: #E8E6E1')
    return s[:i] + capa_n + s[j:]


def cabeca_comum(s):
    s = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?[^"]*">', FONTES, s, count=1)
    s = s.replace('<meta name="theme-color" content="#E8E6E1">', '<meta name="theme-color" content="#0E0E0F">')
    s = s.replace('content="Enrico Montovanelli, portfólio: papel de xerox com barras de terminal"', 'content="Enrico Montovanelli, portfólio: fundo preto com grão, nome em letra larga e barras de terminal"')
    s = s.replace("'IBM Plex Mono'", "'JetBrains Mono'")
    return s


def menu():
    s = ler("index.html")
    s = cabeca_comum(s)
    # sem bobinadeira e sem cubinhos (decisão de 25/11/2026)
    s = troca(s, '<!-- bobinadeira e cubinhos: só entre as duas barras -->\n', '')
    s = re.sub(r'<canvas class="entrada" aria-hidden="true" id="cena"[^>]*></canvas>\n', '', s, count=1)
    i = s.index('// bobinadeira da LTQ e cubinhos'); fim = "new Cena(document.getElementById('cena'));\n"
    j = s.index(fim) + len(fim)
    s = s[:i] + s[j:]
    # papel com grão vira preto com grão
    s = re.sub(r'<!-- textura de papel -->\n<svg aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0.75; mix-blend-mode: multiply; pointer-events: none">.*?</svg>',
               '<!-- grão -->\n' + grao("papel", "0.22"), s, count=1, flags=re.S)
    # negativo: troca grafite e papel em tudo (inclui capa e barra do scanner)
    s = s.replace('#2E2E2E', '@@T@@').replace('#E8E6E1', '@@F@@')
    s = s.replace('@@T@@', PAPEL).replace('@@F@@', NOITE)
    s = s.replace('rgba(46,46,46,', 'rgba(232,230,225,')
    i = s.index('id="capa"'); j = s.index('</div>', i)
    capa = re.sub(r'<svg aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0.5; mix-blend-mode: multiply; pointer-events: none">.*?</svg>', grao("grao-in", "0.18"), s[i:j])
    return s[:i] + capa + s[j:]


def carreira():
    s = ler("carreira.html")
    s = cabeca_comum(s)
    s = s.replace('#D4D5D7', NOITE).replace('#1A1B1D', PAPEL)
    s = s.replace('color: #D21A16', f'color: {VERM_TEXTO}').replace('a:hover{color:#D21A16}', f'a:hover{{color:{VERM_TEXTO}}}')
    s = capa_preta(s)
    s = troca(s, '<style>\n', '<style>\n' + CSS_COMUM +
              'img[src^="assets/logos/"]{filter:invert(1) brightness(1.05)}\n'
              "h2[id^=\"t-\"]{font-family:'Marcellus',Georgia,serif !important;font-size:17px !important;letter-spacing:0.12em !important;text-transform:uppercase !important;display:flex;align-items:center;gap:12px}\n"
              'h2[id^="t-"]::before{content:"";width:7px;height:7px;background:#E8E6E1;flex:none}\n')
    # grão da página
    s = re.sub(r'<svg aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0.6; mix-blend-mode: multiply; pointer-events: none"><filter id="grao-pagina">.*?</svg>',
               grao("grao-pagina"), s, count=1)
    # barras de terminal no lugar da ficha do topo
    i = s.index('<!-- topo: ficha técnica e volta ao menu -->'); j = s.index('<header style="display: flex; flex-direction: column;')
    s = s[:i] + s[j:]
    abre = '<div style="max-width: 1200px; margin: 0 auto;'
    s = troca(s, abre, barra_topo("carreira") + '\n' + '<div style="position: relative; max-width: 1200px; margin: 0 auto;')
    # título: Tektur larga com a estrela
    h1 = re.search(r'<h1 style="margin: 0; font-weight: 800; font-size: clamp\(64px, 14vw, 184px\); line-height: 0\.86; letter-spacing: -0\.045em; text-transform: uppercase">Carreira</h1>', s).group(0)
    s = s.replace(h1, '<div style="position: relative; align-self: flex-start; padding-right: 30px"><h1 style="margin: 0; font-family: \'Tektur\', system-ui, sans-serif; font-weight: 500; font-stretch: 125%; font-size: clamp(44px, 8vw, 104px); line-height: 1.02; letter-spacing: 0.01em; text-transform: uppercase">Carreira</h1>' + ESTRELA + '</div>')
    # barra de baixo depois do conteúdo
    fim = '</footer>\n\n</div>\n</div>'
    s = troca(s, fim, '</footer>\n\n</div>\n' + barra_baixo() + '\n</div>')
    s = troca(s, '<script>\n', RELOGIO + '<script>\n')
    return s


def projetos():
    s = ler("projetos.html")
    s = cabeca_comum(s)
    s = s.replace('#0B0B0C', NOITE)
    s = capa_preta(s)
    s = troca(s, '<style>\n', '<style>\n' + CSS_COMUM)
    # barras de terminal no lugar da faixa do topo
    i = s.index('<div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px; font-family: \'JetBrains Mono\'')
    j = s.index('<div class="hero-a"')
    s = s[:i] + s[j:]
    abre = '<div style="position: relative; max-width: 1280px; margin: 0 auto;'
    s = troca(s, abre, barra_topo("projetos") + '\n' + abre)
    # título: Tektur larga com a estrela (sai o listrado da Syncopate)
    h1 = '<h1 class="listrado" style="margin: 0; font-family: \'Syncopate\', \'Inter Tight\', sans-serif; text-transform: uppercase; font-weight: 700; font-size: clamp(46px, 7.4vw, 104px); letter-spacing: 0.04em; line-height: 0.95">Projetos</h1>'
    s = troca(s, h1, '<div style="position: relative; align-self: flex-start; padding-right: 30px"><h1 style="margin: 0; font-family: \'Tektur\', system-ui, sans-serif; font-weight: 500; font-stretch: 125%; font-size: clamp(44px, 7vw, 96px); line-height: 1.02; letter-spacing: 0.01em; text-transform: uppercase">Projetos</h1>' + ESTRELA + '</div>')
    # subtítulos das seções e nomes dos projetos em Marcellus
    s = s.replace("font-family: 'Syncopate', 'Inter Tight', sans-serif; text-transform: uppercase; font-weight: 400; font-size: 14px; letter-spacing: 0.3em",
                  "font-family: 'Marcellus', Georgia, serif; text-transform: uppercase; font-weight: 400; font-size: 17px; letter-spacing: 0.12em")
    s = s.replace("font-family: 'Syncopate', 'Inter Tight', sans-serif; text-transform: uppercase; font-weight: 700; font-size: 26px; letter-spacing: 0.08em; line-height: 1.25",
                  "font-family: 'Marcellus', Georgia, serif; text-transform: uppercase; font-weight: 400; font-size: 24px; letter-spacing: 0.1em; line-height: 1.25")
    assert 'Syncopate' not in s.split('</head>')[1], 'sobrou Syncopate no corpo'
    # barra de baixo no fim do conteúdo
    k = s.index('<div aria-hidden="true" class="tela-scan" id="capa"')
    fecha = s.rindex('</div>\n</div>', 0, k)
    s = s[:fecha] + '</div>\n' + barra_baixo() + '\n</div>' + s[fecha + len('</div>\n</div>'):]
    s = troca(s, '<script>\n', RELOGIO + '<script>\n')
    return s


if __name__ == "__main__":
    (RAIZ / "index.html").write_text(menu(), encoding="utf-8")
    (RAIZ / "carreira.html").write_text(carreira(), encoding="utf-8")
    (RAIZ / "projetos.html").write_text(projetos(), encoding="utf-8")
    print("ok")
