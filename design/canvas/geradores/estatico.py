# Gera projetos.html (site) a partir de ProjetosA.dc.html (canvas).
# Uso: python3 estatico.py <ProjetosA.dc.html> <pasta do repositório>
import sys, os
dc=open(sys.argv[1]).read(); repo=sys.argv[2]
car=open(os.path.join(repo,"carreira.html")).read()
helmet=dc[dc.index("<helmet>")+8:dc.index("</helmet>")]
links="\n".join(l for l in helmet.split("\n") if l.startswith("<link"))
style=helmet[helmet.index("<style>")+7:helmet.index("</style>")].strip()
body=dc[dc.index("</helmet>")+9:dc.index("</x-dc>")].strip()
css_scan="\n".join(l for l in car[car.index("<style>"):car.index("</style>")].split("\n") if "scan" in l)
blobs={"2a88d5f937183687928c5371716eb1dc":"drone/drone-01-grafite.jpg","4d13a81d802c92c9e676fad8afc1943b":"balanca/balanca-01-grafite.jpg",
"6e1662ccb9b9853fd00dc863e160df4a":"balanca/balanca-02-grafite.jpg","91f431831a592875852f0318446f9fcc":"carrinho/carrinho-04-grafite.jpg",
"2ed4a68b0720300c77aa98dd02766a70":"incendio/incendio-01-grafite.jpg","9a6935ebf9621170701246c87ad79b1d":"drone/drone-03-grafite.jpg",
"11e83af2be48600ddf4f84fdca0eec12":"drone/drone-05-grafite.jpg","7f0c1b31e201857f4fca7ccf48eea844":"carrinho/carrinho-03-grafite.jpg",
"5487a8a01f8d0407411dadf3a5094259":"carrinho/carrinho-02-grafite.jpg","4c77c9841d42cd0821696eb4c0f08fc5":"incendio/incendio-02-grafite.jpg"}
for k,v in blobs.items():
    body=body.replace(f'src="/_blob/{k}"',f'src="assets/projetos/faculdade/{v}" loading="lazy"')
assert "/_blob/" not in body
body=body.replace('<a href="Main.dc.html"','<a href="index.html" data-transicao="&gt; voltar /menu"')
assert "data-transicao" in body
i=car.index('<div aria-hidden="true" class="tela-scan"'); tail=car[i:car.rindex("</body>")]
tail=tail.replace('<span id="capa-msg">&gt; /carreira</span>','<span id="capa-msg">&gt; /projetos</span>')
html=f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<title>Projetos, Enrico Montovanelli</title>
{links}
<style>
{style}
{css_scan}
</style>
</head>
<body>
{body}
{tail}</body>
</html>
'''
open(os.path.join(repo,"projetos.html"),"w").write(html)
print("projetos.html", len(html), "imgs", html.count("<img"))
