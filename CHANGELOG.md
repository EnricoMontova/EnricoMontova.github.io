# Changelog

Data e descrição de cada mudança. Mais recente primeiro. Detalhe técnico de cada item: `git log`.

## 26/11/2026

- Sessão feita só pelo GitHub (sem a máquina do Enrico).
- Currículo, rodada 2 respondida (`docs/CURRICULO.md`): tópico T confirmado; tópico R reescrito ("Implemento as demandas da rotina de automação da LTQ e acompanho sua implantação em produção."); sem números; Mudanças e Fretes fora; formato PDF + link no site; contato em duas versões; certificações da versão Automação definidas.
- Currículo: gerador `curriculo/gerar.py` (HTML + PDF pelo Chrome ou Edge), fontes do site embutidas em `curriculo/fontes/` (licença OFL), HTML em `curriculo/html/`, PDFs públicos em `assets/curriculo/` (Dados, Software, Automação), cada um com 1 página.
- Currículo: textos encurtados para caber em 1 página: tópico L ("Implemento modificações na lógica do processo da LTQ em C/C++, em servidores Tru64 UNIX do Nível 2."), tópico T sem o prefixo "documentação técnica:", resumo da Automação sem "que ligam o controle da planta à gestão da produção", TCC sem "Desenvolvimento de um", descrições dos três projetos, competência Documentação resumida, certificações agrupadas por plataforma e ano, Idiomas como linha das Competências.
- Currículo: tópico da Gol no passado ("Apoiei as rotinas administrativas do RH, com controle de planilhas."), seguindo o critério de verbo de ação.
- `DECISOES.md`: decisões de 26/11/2026.
- Currículo: VB6 em Windows XP (estação remota), C# em Windows 10 e Java e SQL (envio ao data lake) na linha "Tecnologias do estágio"; Windows 11 removido; tópico novo sobre o envio de dados ao data lake nas três versões.
- Currículo (Automação): Windows XP, 10 e 11 passam para "Tecnologias do estágio" (confirmado pelo Enrico); linha "Sistemas" removida.
- Currículo: Competências reorganizadas nas três versões, com "Tecnologias do estágio" e "Estudos e projetos" no lugar de "Linguagens", "Ferramentas", "Dados" e parte de "Sistemas".
- Currículo: GOL com o texto novo do Enrico em dois tópicos (RH com credenciais e ferramentas; serviço de bagagens LL); tópico de competências comportamentais fora.
- Currículo: carrinho em uma linha ("o público pilotava os carrinhos pelo celular"); versão Automação sem as competências "Dados" e "Documentação" para caber em 1 página.

## 25/11/2026

- Canvas: passa a abrir no menu da B3 (antes abria o menu antigo); telas da B3 ligadas entre si (menu, Carreira, Projetos, "< /menu", Currículo).
- Site: sistema B3 aplicado às três páginas (`index.html`, `carreira.html`, `projetos.html`) por `design/canvas/geradores/aplicar_b3.py`. Fundo preto com grão, barras de terminal em todas as páginas, títulos em Tektur com estrela, subtítulos em Marcellus, rótulos em JetBrains Mono, logos invertidos.
- Menu: bobinadeira e cubinhos retirados do fundo (código da animação removido).
- Versão anterior guardada em `versoes/2026-11-25-tres-estilos/`; no canvas, telas antigas marcadas como "versão anterior, salva".
- Favicon e imagem de prévia refeitos no preto.
- Canvas: B3 e B4 refeitas com a tipografia da B1 (o Enrico tinha escrito B2 por engano).
- Canvas: modelos B3 (tudo preto) e B4 (tudo preto com barras de papel). Gerador `sistema_b.py` passou a aceitar paletas; vermelho de texto sobre preto ajustado para `#EA3E34` (também nas telas de Projetos da B1 e da B2).
- Canvas: modelos da direção B ("dia e noite") em duas variantes, B1 (Tektur larga + Marcellus) e B2 (Antonio condensada com ponto vermelho), cada uma com menu, Carreira e Projetos. Gerador em `design/canvas/geradores/sistema_b.py`.
- Referências: 7 imagens novas em `referencias/estetica/`, descritas no `referencias/README.md`.
- Menu: linha de apresentação na barra de cima; LinkedIn, GitHub e Currículo (aponta para a Carreira) na barra de baixo, no lugar do "2026" (`index.html`, telas Main e MenuCelular no canvas).
- Menu: animação da bobinadeira presa entre as barras (antes invadia a barra de baixo).
- Favicon e prévia do link (Open Graph) nas três páginas: `assets/favicon.svg`, `assets/favicon-32.png`, `assets/apple-touch-icon.png`, `assets/og.jpg`.
- Foto do Enrico retirada dos planos do site; e-mail fora do site (`DECISOES.md`, `docs/CONTEUDO.md`).
- Objetivo do projeto atualizado no `CONTEXTO.md` e registrado no `DECISOES.md`: site único (currículo, site pessoal, vitrine) e GitHub com a mesma identidade visual; referência luan-k10 adaptada; princípios prático, bonito e único.
- Envio ao GitHub feito depois da autorização do Enrico (a primeira tentativa de ligar o repositório à sessão foi bloqueada).
- Tentativa de mover os itens obsoletos para `_apagar` pelo controle remoto do computador, sem sucesso (Explorador limitado a cliques). Pendência registrada no `CONTEXTO.md`, item 7.
- Documentação reorganizada conforme as novas instruções do projeto: `CONTEXTO.md` (substitui `docs/ESTADO.md`), `DECISOES.md` (movido de `docs/`) e este `CHANGELOG.md`, todos na raiz.
- Espelho do projeto criado no Google Drive (pastas e arquivos de texto).
- Pasta local sincronizada com as mudanças de 25/11.
- Menu: link "Projetos pessoais" renomeado para "Projetos", abrindo `projetos.html` com a transição de scanner (`index.html`, telas Main e MenuCelular).
- Projetos: seção de projetos pessoais passou para o topo; fotos retiradas da página; texto de abertura passou a citar as duas seções.
- Projetos: modelo A escolhido; versão de celular (tela "Projetos, celular"); página `projetos.html` gerada; script `estatico.py`.

## 22/11/2026

- Projetos: separação entre faculdade e pessoais; galeria de fotos por projeto; fotos movidas para `assets/projetos/faculdade/`.
- Projetos: fotos do drone, da balança, do carrinho e do sistema de incêndios em grafite nos quatro modelos; texto do drone sem tipo de motor; carrinho no ESX 2025, controlado pelo celular pelos visitantes; fotos com pessoas fora do repositório.
- Quatro modelos da página de Projetos no canvas (A arquivo, B monitor, C ficha, D painel), a partir das referências 10 a 13.
- Docs: análise do portfólio de referência, decisões de 22/11, conteúdo dos projetos, currículo em construção, estado do projeto; foto do Enrico em grafite.

## 15/11/2026

- Site em HTML: `index.html` (menu) e `carreira.html`, com transição do scanner.
- Avisos de rolagem e contagens removidos.
- Celular com o mesmo conteúdo do computador.
- Carreira: Tubarão Aços Planos, Mudanças e Fretes; transição do scanner quadro a quadro.
- Primeira versão: menu xerox com terminal, Carreira, referências e documentação.
