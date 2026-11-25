# Análise da referência (Luan Kairo) e plano de migração

Data: 22/11/2026. Estado: decisões tomadas em 22/11/2026 (ver seção 5).

## 1. Referência analisada

### Site: https://luan-k10.github.io/
- Página única com âncoras: Sobre, Projetos, Carreira, Skills, Certificados, Contato. Currículo em página própria (`/curriculo/`).
- Tema escuro com destaque vinho (`theme-color` #6e1423), botão claro/escuro, foto redonda, cards com tags de tecnologia, linha do tempo vertical.
- Topo com nome, cargos, cidade, texto curto e botões: Fale comigo, Currículo, GitHub, LinkedIn.
- Projetos com contexto, prêmio, funcionalidades e stack, com links para código e site.
- Certificados com link de verificação.
- Feito em Astro, publicado no GitHub Pages, com Open Graph (prévia do link em redes sociais).

### GitHub: https://github.com/luan-k10
README do perfil, de cima para baixo: banner em onda (capsule-render), texto animado (readme-typing-svg), selos shields.io (portfólio, LinkedIn, e-mail, seguidores, estrelas), Sobre mim, ícones devicon, tabela de projetos em destaque, prêmios e certificados, streak-stats e gráfico de atividade, banner de rodapé. Tudo na mesma paleta vinho do site.

### Observação
O Luan tem o mesmo cargo do Enrico (estagiário de automação Nível 2 na ArcelorMittal). Copiar o visual dele deixaria os dois portfólios parecidos para quem vir os dois.

## 2. Estado atual do Enrico (conferido em 22/11/2026)

### Site (pasta local, repositório montovanelli-portfolio)
- Feito: menu (xerox com terminal, bobinadeira animada) e página Carreira (estilo suíço), computador e celular. Padrão em `DECISOES.md`.
- Não publicado: https://enricomontova.github.io/montovanelli-portfolio/ retorna 404.
- Faltam em relação à referência:
  - Contato (nenhum link de e-mail, LinkedIn ou GitHub nas páginas).
  - Currículo (ver ou baixar).
  - Projetos pessoais (link do menu aponta para `#projetos`, sem página).
  - Open Graph e favicon (o ícone atual é `data:,`, vazio).
  - Links dos certificados (marcados "a preencher" em `docs/CONTEUDO.md`).
- Já tem e a referência não: trajetória proporcional ao tempo, disciplinas com médias, ferramentas de Nível 2 (Unix Tru64, VB6, C/C++), documentação técnica, inglês fluente.

### GitHub (https://github.com/EnricoMontova)
- README em inglês e desatualizado: diz 21 anos, 6º semestre e emprego atual de Jovem Aprendiz na Gol desde 01/07/2024.
- Selos de JavaScript, Python e C (o selo de JavaScript tem texto alternativo "C"). Não cita Java, C#, C++, VB6, SQL nem Databricks.
- Usa github-readme-stats (instância pública, que costuma sair do ar por limite de uso).
- Repositórios: montovanelli-portfolio, OPTATIVA, projeto_reconhecimento, workshop-springboot3-jpa, EnricoMontova (perfil) e um fork de anuraghazra (modelo antigo de README).
- Fixados: workshop-springboot3-jpa e projeto_reconhecimento.

## 3. Opções apresentadas

### A. Estrutura do site
1. Manter menu + páginas e acrescentar o que falta (Contato, Currículo, Projetos, Open Graph). A favor: preserva o que foi aprovado, menos retrabalho. Contra: o recrutador precisa de um clique para ver qualquer conteúdo.
2. Converter para página única com seções, como a referência. A favor: leitura rápida de cima a baixo. Contra: retrabalho grande; a transição de xerox entre páginas perde o sentido; menu xerox e Carreira suíça ficariam lado a lado na mesma rolagem.
3. Híbrido (sugerido): manter menu + páginas e usar as barras de terminal do menu para uma linha de apresentação e os links de contato e currículo. A favor: resolve o "primeiro clique" sem mudar o padrão. Contra: as barras ficam mais cheias, precisa testar no celular.

### B. Tecnologia
1. Manter HTML estático (sugerido). A favor: já funciona, publica direto no GitHub Pages. Contra: cabeçalhos e rodapés repetidos em cada página.
2. Migrar para Astro, como a referência. A favor: componentes reaproveitáveis. Contra: passo de build, reescrever o que existe.

### C. Endereço
1. Manter o repositório montovanelli-portfolio: endereço `enricomontova.github.io/montovanelli-portfolio/`.
2. Renomear para `EnricoMontova.github.io`: endereço `enricomontova.github.io`, mais curto, como o da referência. Contra: renomear o repositório e atualizar o README.

### D. README do GitHub
1. Identidade do site (sugerido): cabeçalho em SVG ou arte ASCII com papel, grafite e o vermelho #D21A16, texto em letra de máquina, tabela de projetos, link para o site. A favor: coerência com o site e diferenciação. Contra: o GitHub não aceita CSS nem fontes próprias, então o cabeçalho precisa ser imagem SVG feita por nós.
2. Modelo da referência recolorido (capsule-render, digitação, selos, streak). A favor: rápido. Contra: fica parecido com o do Luan e depende de serviços externos.
3. Só texto e tabelas. A favor: nada quebra. Contra: pouco visual.
- Idioma: português, inglês ou bilíngue (a decidir).

## 4. Informações que dependem do Enrico
- URL do LinkedIn e e-mail para contato.
- Currículo em PDF (ou gerar um a partir de `docs/CONTEUDO.md`).
- Quais projetos mostrar e o que são: OPTATIVA, projeto_reconhecimento, workshop-springboot3-jpa, TCC, outros.
- Foto no site: sim ou não.
- Links de verificação dos certificados.
- O que fazer com o fork anuraghazra (apagar é ação do Enrico).

## 5. Decisões (22/11/2026)
- A: opção 3, híbrido.
- B: opção 1, HTML estático.
- C: opção 2, renomear para `EnricoMontova.github.io`.
- D: opção 1, visual do site, em português e inglês.
- Seção 4: LinkedIn informado; currículo será montado junto, por perguntas; projetos serão os 4 do LinkedIn (não os repositórios listados); foto no site; apagar o fork anuraghazra.

## 6. Observações técnicas (22/11/2026)
- A pasta local não tem repositório remoto configurado (`.git/config` sem `[remote "origin"]`).
- `index.html`, `carreira.html`, `README.md`, `docs/CONTEUDO.md` e `DECISOES.md` foram alterados depois do último commit local. Correção após clonar o GitHub (22/11/2026): esses arquivos são idênticos aos do GitHub (commit 897c98f, 15/11/2026). O que ficou para trás foi só o histórico do `.git` local.
- O navegador embutido do Claude não está logado no GitHub.
