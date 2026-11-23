# Decisões de design

Registro do padrão visual aprovado e do que já foi testado e descartado. Antes de mudar qualquer coisa, conferir aqui.

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

Pendentes: escolher o modelo de Projetos, formato final do currículo, renomear o repositório e apagar o fork (no GitHub, pelo Enrico ou com login no navegador).

## Como pedir mudanças

- Mudar só o que foi pedido e manter os padrões acima.
- Se a forma de fazer não estiver clara, perguntar antes.
- Testar nas duas larguras (computador e celular).
