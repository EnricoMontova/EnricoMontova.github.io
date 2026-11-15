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

## Como pedir mudanças

- Mudar só o que foi pedido e manter os padrões acima.
- Se a forma de fazer não estiver clara, perguntar antes.
- Testar nas duas larguras (computador e celular).
