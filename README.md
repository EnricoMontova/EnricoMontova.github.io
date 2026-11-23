# Portfólio Enrico Montovanelli

Portfólio pessoal de Enrico Montovanelli, estudante de Engenharia da Computação (FAESA) e estagiário de engenharia de software na automação da Laminação de Tiras a Quente da ArcelorMittal Tubarão.

O site tem um menu de entrada e uma página de Carreira. A página de Projetos está em fase de escolha de modelo (quatro modelos no canvas) e a de Hobbies ainda será criada. O estado atual e as pendências estão em `docs/ESTADO.md`.

## Como ver o site

- **No computador:** abra o `index.html` com dois cliques.
- **Na internet (GitHub Pages):** no GitHub, vá em Settings › Pages, escolha "Deploy from a branch", branch `main`, pasta `/ (root)` e salve. Em alguns minutos o site fica em `https://enricomontova.github.io/montovanelli-portfolio/`.

## Estrutura da pasta

```
index.html            menu (computador e celular na mesma página)
carreira.html         página de carreira (computador e celular na mesma página)
design/canvas/        telas do site no formato do canvas do Claude (.dc.html)
  Main.dc.html          menu principal (computador; vira layout de celular em tela estreita)
  MenuCelular.dc.html   prévia do menu na largura de celular
  Carreira.dc.html      página de carreira (computador; adapta em tela estreita)
  CarreiraCelular.dc.html  prévia da carreira na largura de celular
  MenuPS3.dc.html       versão antiga do menu, guardada (inspirada na abertura do PS3)
  Anterior.dc.html      primeira versão completa do site, só como referência
  ProjetosA..D.dc.html  quatro modelos da página de Projetos, para escolha
  canvas.json           posição e nome de cada tela no canvas
  geradores/            scripts Python que geram os modelos de Projetos
assets/logos/         logos já tratados na cor do site (grafite, fundo transparente)
assets/imagens/       imagens produzidas para o site (foto do Enrico em grafite)
assets/projetos/      fotos dos projetos: faculdade/<projeto>/ e pessoais/
referencias/          referências visuais usadas no projeto (ver referencias/README.md)
docs/                 decisões de design, conteúdo e instruções para trabalhar com o Claude
```

## Onde está o design

O design vive num canvas do Claude (artefato "Portfólio Enrico Montovanelli"). Os arquivos em `design/canvas/` são cópias dessas telas. Eles dependem do runtime do canvas (`support.js`) e apontam para imagens hospedadas no canvas (`/_blob/...`); as mesmas imagens estão em `assets/`.

## Próximos passos

Lista completa e atualizada em `docs/ESTADO.md`. O repositório será renomeado para `EnricoMontova.github.io`; depois disso o site fica em `https://enricomontova.github.io`.

As páginas `index.html` e `carreira.html` foram geradas a partir das telas do canvas. Ao mudar o design, atualize as duas versões.

## Documentos

- `docs/ESTADO.md`: estado atual e pendências. Ler primeiro.
- `docs/DECISOES.md`: o padrão visual do site, decisões com data e o que já foi testado e descartado.
- `docs/ANALISE_REFERENCIA.md`: análise do portfólio de referência e opções apresentadas.
- `docs/CURRICULO.md`: currículo em construção (contato em `docs/privado/`, fora do GitHub).
- `docs/CONTEUDO.md`: os textos e dados que aparecem no site.
- `docs/PROJETO_CLAUDE.md`: sugestão de como organizar um projeto no Claude para continuar o trabalho.
