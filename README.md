# Portfólio Enrico Montovanelli

Portfólio pessoal de Enrico Montovanelli, estudante de Engenharia da Computação (FAESA) e estagiário de engenharia de software na automação da Laminação de Tiras a Quente da ArcelorMittal Tubarão.

O site tem um menu de entrada e uma página de Carreira. As páginas de Projetos pessoais e Hobbies ainda serão criadas.

## Estrutura da pasta

```
design/canvas/        telas do site no formato do canvas do Claude (.dc.html)
  Main.dc.html          menu principal (computador; vira layout de celular em tela estreita)
  MenuCelular.dc.html   prévia do menu na largura de celular
  Carreira.dc.html      página de carreira (computador; adapta em tela estreita)
  CarreiraCelular.dc.html  prévia da carreira na largura de celular
  MenuPS3.dc.html       versão antiga do menu, guardada (inspirada na abertura do PS3)
  Anterior.dc.html      primeira versão completa do site, só como referência
  canvas.json           posição e nome de cada tela no canvas
assets/logos/         logos já tratados na cor do site (grafite, fundo transparente)
assets/imagens/       imagens produzidas para o site
referencias/          referências visuais usadas no projeto (ver referencias/README.md)
docs/                 decisões de design, conteúdo e instruções para trabalhar com o Claude
```

## Onde está o design

O design vive num canvas do Claude (artefato "Portfólio Enrico Montovanelli"). Os arquivos em `design/canvas/` são cópias dessas telas. Eles dependem do runtime do canvas (`support.js`) e apontam para imagens hospedadas no canvas (`/_blob/...`); as mesmas imagens estão em `assets/`.

## Próximos passos

1. Converter o menu e a Carreira em HTML estático (`index.html` e `carreira.html`) para publicar no GitHub Pages.
2. Preencher os links reais de LinkedIn, GitHub e dos certificados.
3. Criar as páginas de Projetos pessoais e Hobbies no mesmo padrão.

## Documentos

- `docs/DECISOES.md`: o padrão visual do site e o que já foi testado e descartado.
- `docs/CONTEUDO.md`: os textos e dados que aparecem no site.
- `docs/PROJETO_CLAUDE.md`: sugestão de como organizar um projeto no Claude para continuar o trabalho.
