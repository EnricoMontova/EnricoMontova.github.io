# Portfólio Enrico Montovanelli

Portfólio pessoal de Enrico Montovanelli, estudante de Engenharia da Computação (FAESA) e estagiário de engenharia de software na automação da Laminação de Tiras a Quente da ArcelorMittal Tubarão.

O site tem um menu de entrada, uma página de Carreira e uma de Projetos (pessoais primeiro, depois os da faculdade), todas no sistema visual B3: fundo preto com grão e barras de terminal. A de Hobbies ainda será criada. O estado atual e as pendências estão em `CONTEXTO.md`.

## Como ver o site

- **No computador:** abra o `index.html` com dois cliques.
- **Na internet (GitHub Pages):** no GitHub, vá em Settings › Pages, escolha "Deploy from a branch", branch `main`, pasta `/ (root)` e salve. Em alguns minutos o site fica em `https://enricomontova.github.io/montovanelli-portfolio/`.

## Estrutura da pasta

```
index.html            menu (computador e celular na mesma página)
carreira.html         página de carreira (computador e celular na mesma página)
projetos.html         página de projetos, modelo A (computador e celular na mesma página)
design/canvas/        telas do site no formato do canvas do Claude (.dc.html)
  Main.dc.html          menu principal (computador; vira layout de celular em tela estreita)
  MenuCelular.dc.html   prévia do menu na largura de celular
  Carreira.dc.html      página de carreira (computador; adapta em tela estreita)
  CarreiraCelular.dc.html  prévia da carreira na largura de celular
  MenuPS3.dc.html       versão antiga do menu, guardada (inspirada na abertura do PS3)
  Anterior.dc.html      primeira versão completa do site, só como referência
  ProjetosA.dc.html     página de Projetos (modelo A, escolhido)
  ProjetosCelular.dc.html  prévia de Projetos na largura de celular
  ProjetosB..D.dc.html  modelos não escolhidos, guardados
  canvas.json           posição e nome de cada tela no canvas
  geradores/            scripts Python: modelos de Projetos, modelos da direção B (sistema_b.py) e a conversão das páginas para o sistema B3 (aplicar_b3.py)
assets/               favicon (favicon.svg, favicon-32.png, apple-touch-icon.png) e imagem de prévia do link (og.jpg)
assets/logos/         logos já tratados na cor do site (grafite, fundo transparente)
assets/imagens/       imagens produzidas para o site (foto do Enrico em grafite)
assets/projetos/      fotos dos projetos: faculdade/<projeto>/ e pessoais/
referencias/          referências visuais usadas no projeto (ver referencias/README.md)
docs/                 decisões de design, conteúdo e instruções para trabalhar com o Claude
versoes/              versões anteriores do site, que abrem sozinhas (2026-11-25-tres-estilos: antes do sistema B3)
```

## Onde está o design

O design vive num canvas do Claude (artefato "Portfólio Enrico Montovanelli"). Os arquivos em `design/canvas/` são cópias dessas telas. Eles dependem do runtime do canvas (`support.js`) e apontam para imagens hospedadas no canvas (`/_blob/...`); as mesmas imagens estão em `assets/`.

## Próximos passos

Lista completa e atualizada em `CONTEXTO.md`. O repositório será renomeado para `EnricoMontova.github.io`; depois disso o site fica em `https://enricomontova.github.io`.

As páginas atuais foram geradas por `design/canvas/geradores/aplicar_b3.py` a partir da versão anterior. Daqui em diante, edite as páginas da raiz direto; o modelo de referência no canvas são as telas "B3, ESCOLHIDA".

## Documentos

- `CONTEXTO.md`: caminhos (local, Drive, GitHub), estado atual e próximos passos. Ler primeiro.
- `CHANGELOG.md`: data e descrição de cada mudança.
- `DECISOES.md`: o padrão visual do site, decisões com data e o que já foi testado e descartado.
- `docs/ANALISE_REFERENCIA.md`: análise do portfólio de referência e opções apresentadas.
- `docs/CURRICULO.md`: currículo em construção (contato em `docs/privado/`, fora do GitHub).
- `docs/CONTEUDO.md`: os textos e dados que aparecem no site.
- `docs/PROJETO_CLAUDE.md`: sugestão de como organizar um projeto no Claude para continuar o trabalho.
