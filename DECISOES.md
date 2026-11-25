# Decisões

Registro com data, decisão, motivo e alternativas descartadas, mais o padrão visual aprovado. Antes de mudar qualquer coisa, conferir aqui.

## Menu (xerox com terminal)

- **Fundo:** papel off-white `#E8E6E1` com grão forte (ruído de textura por cima de tudo).
- **Tinta:** grafite `#2E2E2E`.
- **Barras de terminal:** uma no topo e uma no rodapé, borda de 2 px, letra de máquina (JetBrains Mono, caixa alta, espaçada).
  - Topo: `ENRICO.MONTOVANELLI / PORTFÓLIO` e relógio ao vivo (hh:mm:ss).
  - Rodapé: `SELECIONE UMA SEÇÃO` com cursor piscando; ao passar o mouse num link vira `> ABRIR /CARREIRA` etc.
- **Nome:** Tektur larga, caixa alta, uma linha no computador (quebra no celular), estrela de quatro pontas no fim e colchete fino embaixo.
- **Links:** Marcellus em caixa alta, numa linha, depois de um código de barras gerado a partir das letras do nome, e uma linha que segue até a borda direita. Ao passar o mouse, o link inverte (bloco grafite, texto claro). Sem números nos links.
- **Animação de fundo:** bobinadeira (coilbox) da LTQ em tinta de xerox, em homenagem ao estágio. Uma bobina no alto à direita, outra embaixo à esquerda, a chapa passando entre elas pela tangente com rolos prensadores; a chapa vai de uma bobina para a outra e depois volta. Cubinhos cinza (pixels numa grade de 8 px) piscando de leve.
- **Limite:** nada da animação passa das barras do topo e do rodapé.

## Carreira (suíço com minimalismo técnico)

- **Fundo:** cinza claro `#D4D5D7` com grão. Tinta `#1A1B1D`. Um único destaque vermelho `#D21A16`, usado para o que é atual (estágio, disciplinas em curso).
- **Fontes:** Inter Tight (títulos e texto) e IBM Plex Mono (rótulos, datas, avisos).
- **Padrões que se repetem:**
  - Linha fina com quadradinho de 7 px na ponta abrindo cada bloco.
  - Rótulos em letra de máquina, caixa alta.
  - Quadrados de borda fina para certificados e disciplinas, sempre com a mesma estrutura: topo (logo ou semestre, data ou carga horária), nome, rodapé (carga horária e link, média, "cursando" ou "aproveitada").
  - Listas roláveis com barra fina grafite, sem aviso de rolagem e sem contagem: o site deve ser intuitivo pelo próprio design.
  - Logos sempre na cor da tinta, ao lado do texto (nunca em cima), e a empresa vem antes da função.
- **Ordem no computador:** título CARREIRA e frase de abertura, trajetória em cota (horizontal, trechos proporcionais ao tempo), certificados ao lado dos cargos (estágio, fretes, jovem aprendiz), formação FAESA embaixo com as disciplinas roláveis para baixo, ferramentas (grade 4 colunas com linhas finas), rodapé.
- **Ordem em tela estreita / celular:** cargos, formação, certificados (rolando para o lado, quadrados do mesmo tamanho do computador), ferramentas. A trajetória continua horizontal e rola para o lado.

## Transição entre menu e Carreira

Escaneamento de xerox: a tela de destino nasce coberta pelo papel com a mensagem (`> ABRIR /CARREIRA`, `> VOLTAR /MENU`) e uma barra de scanner desce revelando a página. O movimento é feito quadro a quadro em JavaScript (requestAnimationFrame), porque o canvas congela animações CSS que começam junto com a página. A capa some sozinha em no máximo 3 s. Nada de visibilidade pode depender de animação CSS de entrada.

## Testado e descartado

- Versões de menu: PS3 com onda (guardada como MenuPS3), vidro verde-água, malha de linhas pretas, tela dividida com o Mestre Álvaro e fumaça, cyberbrutalista com torres de cubos (elementos de terminal foram aproveitados).
- No fundo do menu: emblemas circulares tipo engrenagem, atrator de Lorenz.
- Na Carreira: diagrama dos níveis 1, 2 e 3, etiqueta "EM PORTFÓLIO", código como textura, linha "TÉCNICA : NÍVEL 2", números nos links do menu, nome com desfoque.
- Logos redesenhados: não fazer; usar os arquivos oficiais em uma cor só.

## Computador e celular

O conteúdo é sempre o mesmo nas duas versões (textos, links, dados). Só muda a forma de mostrar: layout, tamanho e direção de rolagem.

## Decisões de 22/11/2026 (análise da referência luan-k10)

Detalhes e opções descartadas em `docs/ANALISE_REFERENCIA.md`.

| Tema | Escolhido | Motivo | Descartado |
|---|---|---|---|
| Estrutura | Híbrido: manter menu + páginas; barras de terminal do menu recebem uma linha de apresentação e os links de contato e currículo | Resolve o primeiro clique sem mudar o padrão aprovado | Só acrescentar páginas; página única como a referência |
| Tecnologia | Continuar em HTML estático | Já funciona e publica direto no GitHub Pages | Migrar para Astro |
| Endereço | Renomear o repositório para `EnricoMontova.github.io` (site em `enricomontova.github.io`) | Endereço mais curto | Manter `montovanelli-portfolio` |
| README do GitHub | No visual do site (papel, grafite, vermelho #D21A16), cabeçalho em SVG | Coerência com o site e diferenciação da referência | Modelo da referência recolorido; só texto |
| Idioma do README | Português e inglês | Pedido do Enrico | Só um idioma |
| Projetos | Os 4 projetos do LinkedIn (balança, carrinho ESX, drone, detecção de incêndios) | Escolha do Enrico | OPTATIVA, projeto_reconhecimento, workshop-springboot3-jpa |
| Foto | Usar foto no site | Escolha do Enrico | Sem foto |
| Fork anuraghazra | Apagar | Escolha do Enrico | Manter |
| Currículo | Montar junto, por perguntas, em `docs/CURRICULO.md` | Pedido do Enrico | |

| Tratamento da foto | A, grafite com grão (`assets/imagens/foto-A.png`) | Escolha do Enrico (22/11/2026) | B, pontilhado xerox |
| Lugar da foto | Na Carreira, ao lado do título e da frase de abertura | Escolha do Enrico (22/11/2026) | No menu; nas duas páginas |
| Publicação no GitHub | Repositório ligado à sessão do Claude com permissão de envio; Claude publica por git | Escolha do Enrico (22/11/2026) | Enrico executa tudo; Claude pelo navegador logado |
| Página de Projetos | Quatro modelos no canvas (A arquivo, B monitor, C ficha, D painel), um por referência nova (10 a 13) | Enrico enviou as referências e pediu modelos para escolher | Padrão suíço da Carreira; xerox do menu; estética nova sem referência |
| Currículo | Uma versão por área (Dados, Software, Automação), objetivo efetivação, sem foto | Respostas do Enrico (22/11/2026) | Currículo único |
| Dados de contato | Telefone e e-mail em `docs/privado/` (fora do GitHub) | O repositório é público | Telefone no repositório |

| Fotos dos projetos | Tratamento grafite com grão em todas; quadro vertical 9:16; drone usa só a foto 01 | Coerência com a foto do Enrico; "Adapte" (fotos verticais e pequenas); a placa das fotos 02 a 06 foi entregue pronta pelo professor | Fotos coloridas; usar as fotos da placa como trabalho do grupo |
| Motores do drone | Texto neutro "Motores e hélices" | Resposta "A descrição certa" não deixou claro qual tipo; nada sem confirmação | "Motores brushless com ESCs" (LinkedIn); "coreless" (leitura da foto) |
| ESX no site | "Apresentado no ESX 2025" | Confirmado pelo Enrico (a foto mostra #ESX2025; o LinkedIn diz 2024 e está errado) | "ESX 2024"; sem ano |
| Fotos com pessoas | Ficam só na pasta local (`.gitignore`) e fora do site: grupo na arena, entrada do ESX, visitantes com crianças | Rostos de terceiros e de crianças; o repositório é público. Confirmado pelo Enrico em 22/11/2026 | Publicar todas; publicar a do grupo com consentimento |
| Tipos de projeto | Duas seções na mesma página: "Projetos da faculdade" (os 4 atuais) e "Projetos pessoais" (em desenvolvimento) | Pedido do Enrico (22/11/2026): os 4 projetos são da faculdade; os pessoais ainda vão ser feitos | Misturar tudo como "projetos pessoais" |
| Pastas das fotos | `assets/projetos/faculdade/<projeto>/` e `assets/projetos/pessoais/` | Pedido do Enrico: pasta nova e separação faculdade/pessoais | Uma pasta por projeto sem separar o tipo |
| Fotos por projeto | Foto principal vertical + 1 ou 2 fotos extras em miniatura com legenda | Pedido do Enrico: usar mais de uma imagem por projeto | Uma foto só |

## Decisões de 25/11/2026

| Tema | Escolhido | Motivo | Descartado |
|---|---|---|---|
| Modelo da página de Projetos | Modelo A, arquivo (ref. 10): fundo preto, estrela de quatro pontas se desfazendo em partículas, título listrado em Syncopate | Escolha do Enrico (25/11/2026) | B monitor, C ficha, D painel (guardados no canvas, marcados como não escolhidos) |
| Celular | Mesma página, adaptada: uma coluna, título com mínimo de 46 px, fotos com até 300 px de largura, estrela com até 340 px | Regra do site: mesmo conteúdo no computador e no celular | Página separada para celular |
| Página estática | `projetos.html`, gerada do modelo A, com as fotos de `assets/projetos/faculdade/`, carregamento sob demanda das fotos e a mesma transição de scanner das outras páginas | Padrão das páginas existentes (B: HTML estático) | |
| Link no menu | "Projetos" (antes "Projetos pessoais"), abrindo `projetos.html` com a transição de scanner | Escolha do Enrico (25/11/2026): opção 1 | Dois links, "Faculdade" e "Pessoais" |
| Ordem das seções | Projetos pessoais primeiro (Setor 01), faculdade depois (Setor 02) | Pedido do Enrico (25/11/2026) | Faculdade primeiro |
| Fotos na página | Fora por enquanto (`FOTOS=False` em `design/canvas/geradores/a.py`); arquivos continuam em `assets/projetos/faculdade/` | O Enrico achou que as fotos quebravam demais a tela (25/11/2026) | Foto principal vertical com miniaturas |
| Texto de abertura | "Projetos pessoais e projetos da graduação em Engenharia da Computação, na FAESA." | A página agora cobre as duas seções | Texto só sobre a graduação |
| Organização da documentação | `CONTEXTO.md`, `DECISOES.md` e `CHANGELOG.md` na raiz; `docs/ESTADO.md` vira `CONTEXTO.md` | Novas instruções do projeto (25/11/2026) | Manter `docs/ESTADO.md` e `docs/DECISOES.md` |
| Espelho no Google Drive | Pasta `portfolio-enrico-montovanelli` em Meu Drive, com todas as pastas e os arquivos de texto (docs, HTML, scripts); imagens ficam na pasta local e no GitHub | Escolha do Enrico (25/11/2026): rápido e suficiente para continuar pelo celular | Espelho completo com imagens (cerca de 100 envios a mais); só os três documentos da raiz |
| Objetivo do projeto | Dois objetivos: (1) site único que serve de currículo, site pessoal e vitrine de projetos; (2) GitHub atualizado com a mesma identidade visual. Referência: luan-k10 (GitHub e site), adaptada ao estilo próprio. Princípios: prático, bonito e único | Pedido do Enrico (25/11/2026) | Objetivo restrito ao site; copiar a referência como está |
| Foto no site | Sem foto | Escolha do Enrico (25/11/2026); substitui a decisão de 22/11 ("Usar foto no site", "Na Carreira, ao lado do título") | Foto na Carreira ao lado do título |
| Contato no site | Só LinkedIn e GitHub, na barra de baixo do menu | Escolha do Enrico (25/11/2026): nada pessoal exposto | Mostrar o e-mail; e-mail montado só no clique |
| Link "Currículo" | Aponta para a Carreira por enquanto; quando o questionário do currículo for respondido, o conteúdo entra na Carreira (mesclado ou como bloco novo) | Escolha do Enrico (25/11/2026) | Deixar o link fora até o currículo ficar pronto; fazer o currículo antes |
| Linha de apresentação | "Eng. de Software na automação · ArcelorMittal Tubarão · Eng. da Computação · Vitória, ES", centralizada na barra de cima; abaixo de 1100 px vai para uma segunda linha, quebrando sempre depois do "·" | Escolha do Enrico (25/11/2026) | Cargo + cidade; área + cidade |
| Barra de baixo do menu | Status à esquerda; à direita LinkedIn ↗, GitHub ↗ e Currículo, que invertem ao passar o mouse (bloco grafite) e escrevem no status, como os links do menu. Substitui o "2026" | Decisão A3 de 22/11 | |
| Favicon | Estrela de quatro pontas do menu, grafite, num quadrado de papel com borda (`assets/favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`) | A estrela já é a assinatura do nome | Iniciais "EM" |
| Prévia do link (Open Graph) | Imagem 1200×630 no visual do menu (`assets/og.jpg`), mesma imagem nas três páginas; endereço absoluto `https://enricomontova.github.io/assets/og.jpg` | Coerência com o menu | Uma imagem por página |
| Animação do menu | A bobinadeira fica presa entre as duas barras (canvas na linha 2 da grade) | Corrige a regra "nada da animação passa das barras": a animação invadia a barra de baixo | |
| Unificação visual | Direção B, "dia e noite": um só sistema (papel com grão e grafite nas páginas claras, Projetos como negativo em preto com grão, barras de terminal em todas as páginas, um único vermelho #D21A16, estrela de quatro pontas, linhas finas com quadradinho, letra de máquina JetBrains Mono). Modelos B1 e B2 no canvas, a escolher | Escolha do Enrico (25/11/2026): as três páginas tinham três "vibes" (xerox, suíço, preto) | A. Papel técnico (tudo claro); C. Sinal (série numerada); D. Arquivo escuro (tudo preto) |
| Tipografia e tom da unificação | Tipografia da B2 (Antonio condensada em caixa alta, ponto vermelho no fim dos títulos, números de seção grandes com traço) e estética preta, como a página de Projetos. Modelos B3 (as três páginas pretas) e B4 (pretas, com as barras de terminal em papel claro) no canvas, a escolher | Escolha do Enrico (25/11/2026): "prefiro o estilo da B2, e também prefiro a estética mais preta" | B1 (Tektur larga + Marcellus); menu e Carreira em papel claro |
| Vermelho sobre preto | Texto pequeno vermelho sobre preto usa `#EA3E34` (contraste de pelo menos 4,5:1); formas e o ponto dos títulos continuam `#D21A16` | Legibilidade do texto de 10 a 12 px | `#D21A16` em todo lugar |

Pendentes: ver `CONTEXTO.md`.

## Como pedir mudanças

- Mudar só o que foi pedido e manter os padrões acima.
- Se a forma de fazer não estiver clara, perguntar antes.
- Testar nas duas larguras (computador e celular).
