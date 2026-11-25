# Contexto do projeto: Portfolio Enrico Montovanelli

## Caminhos

- Pasta local: `C:\Users\Enrico\OneDrive\Área de Trabalho\portfolio-enrico-montovanelli`
- Google Drive: https://drive.google.com/drive/folders/1uD--Xj6kuKmcDx4ax23zRj7zIJmuMdku (espelho de pastas e arquivos de texto; imagens ficam na pasta local e no GitHub)
- GitHub: https://github.com/EnricoMontova/montovanelli-portfolio (público; será renomeado para `EnricoMontova.github.io`)
- Canvas de design (Claude): https://claude.ai/artifact/UUWC6XVBm9Aggep8TgM7YU

Última atualização: 25/11/2026.

## Objetivo

Um único site que sirva de currículo, site pessoal e vitrine dos projetos do Enrico, com identidade visual própria (minimalista, artística, atmosférica). Páginas: menu (xerox com terminal), Carreira (suíço), Projetos (arquivo, fundo preto) e Hobbies (a fazer).

## Como retomar

1. Ler este arquivo.
2. Conferir `DECISOES.md` antes de mudar qualquer padrão visual.
3. Conteúdo do site (textos, projetos, fotos): `docs/CONTEUDO.md`. Currículo: `docs/CURRICULO.md`.
4. Registrar cada mudança em `CHANGELOG.md`.
5. Ao final da sessão: enviar arquivos alterados para o GitHub e para o Drive, incluindo os três documentos da raiz.

## Estado atual

- Site em HTML estático: `index.html` (menu), `carreira.html`, `projetos.html`. Ainda não publicado (GitHub Pages desativado).
- Projetos: modelo A escolhido em 25/11/2026. Projetos pessoais primeiro (em desenvolvimento), depois os 4 da faculdade. Sem fotos na página por enquanto (`FOTOS=False` em `design/canvas/geradores/a.py`); fotos guardadas em `assets/projetos/faculdade/`.
- Telas de design no canvas, com cópias em `design/canvas/`. Geradores Python da página de Projetos em `design/canvas/geradores/` (`a.py` gera a tela; `estatico.py` gera `projetos.html`).
- Dados pessoais fora do GitHub: `docs/privado/` e as fotos listadas no `.gitignore`.
- O `.git` da pasta local não tem remoto e está atrás do GitHub. Os arquivos da pasta são sincronizados pelo Claude, mas o histórico local não.

## Próximos passos

### Decisões do Enrico
1. Currículo, rodada 2 (perguntas no fim de `docs/CURRICULO.md`): documentação técnica no estágio, papel nas demandas, números divulgáveis, fretes, formato final.
2. Tipo de motor do drone (brushless com ESC ou coreless). Hoje o site diz "Motores e hélices".
3. Período ou disciplina do carrinho e qual Projeto Integrador II é o de incêndios.

### Ações do Enrico
4. GitHub: renomear o repositório para `EnricoMontova.github.io` e ativar o Pages (Settings, Pages, branch `main`, pasta `/ (root)`).
5. GitHub: apagar o fork `EnricoMontova/anuraghazra` (não tem volta).
6. LinkedIn: corrigir o ano do ESX (2024 para 2025).
7. Pasta local: apagar as pastas antigas `assets/projetos/drone`, `carrinho`, `incendio` e `balanca` (o conteúdo já está em `assets/projetos/faculdade/`) e os arquivos `docs/ESTADO.md` e `docs/DECISOES.md` (substituídos por `CONTEXTO.md` e `DECISOES.md` na raiz; o Claude não consegue apagar arquivos na máquina).
8. Pasta local: para ter o histórico do git, clonar o repositório de novo (ou ligar o remoto e fazer pull).

### Trabalho do Claude
9. Menu (decisão A3 de 22/11): linha de apresentação e links de contato e currículo nas barras de terminal.
10. Foto do Enrico na Carreira, ao lado do título (decisão de 22/11).
11. E-mail e links (LinkedIn, GitHub) visíveis no site.
12. Open Graph (prévia do link) e favicon.
13. README do perfil do GitHub no visual do site, em português e inglês (depois do passo 4).
14. Currículo: texto final, versão em inglês e formato escolhido.

### Conteúdo faltando
- Links de verificação dos certificados.
- Página de Hobbies.
- Projetos pessoais (ainda vão ser desenvolvidos).

## Google Drive: IDs das pastas

Para atualizar um arquivo no Drive: procurar pelo título dentro da pasta (parentId), enviar a versão nova e mandar a antiga para a lixeira.

| Pasta | ID |
|---|---|
| (raiz) portfolio-enrico-montovanelli | 1uD--Xj6kuKmcDx4ax23zRj7zIJmuMdku |
| assets | 1YQzZXyvl8unub6NR6U2sBpyXeV7GeyIp |
| assets/imagens | 1n0ImDJ9JLhSMplZPh1qSevpaj9ljvHpH |
| assets/logos | 1x6lz950bobnO52XbA_yj9WaiaxHj-d_H |
| assets/projetos | 10eLK1Zomzo9xmQ4EMqj69zX5DA9ZaNIQ |
| assets/projetos/faculdade | 1acZmgs7itjAS55mNP5DAUGHItUpmjFhh |
| assets/projetos/faculdade/balanca | 1fkg-KjuNd2x83TenOYQfN9WZa5-FkQ6T |
| assets/projetos/faculdade/carrinho | 1oAGyyoc186kfUqnKs_pCAVbINAfZklgq |
| assets/projetos/faculdade/drone | 18XuM3U6D5rg1dzeBClJ6Ecl5FKzNvBO_ |
| assets/projetos/faculdade/incendio | 1k_oe9zXkhn3ZYcBcgyU5kW6qv-_r-jkI |
| assets/projetos/pessoais | 1-lV6_XDV2oNwxdma-n4xfBURkbBqfm4p |
| design | 1N14pfM764JN44x1zJP-7xP2ghI6vciNi |
| design/canvas | 1gaLGFmY79uQt6ioGn3Jo5-tScsP04BY9 |
| design/canvas/geradores | 1nG52A-y_pAEVvjorNDEMgUxJnoPB9uBI |
| docs | 15ZyCKQntXanm5ukP7u43PO3Xlx0fHbko |
| docs/privado | 1gO-M_80rc3M0L1xT9ZrWNmsWPkzku9Gb |
| referencias | 13za36F_TIgw9izOv38JcxjaANenDfvl9 |
| referencias/estetica | 1hbRWwyOyzdM5PY57qXydvpnM19xO-LTb |
| referencias/logos-originais | 1TUHicIF10qvBedW1f-H8ORQGZKUE8YwF |

As pastas de imagens existem no Drive, mas ficam vazias (decisão de 25/11/2026).

## Pendências de sincronização

Nenhuma em 25/11/2026 (pasta local, GitHub e Drive atualizados nesta data).
