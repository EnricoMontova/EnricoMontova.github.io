# Currículo

Iniciado em 22/11/2026. Montado por perguntas e respostas. Base: `docs/CONTEUDO.md` e as respostas do Enrico em 22/11/2026 (rodada 1) e 26/11/2026 (rodada 2).

Texto final em português (26/11/2026, aguardando aprovação do Enrico): está em `curriculo/gerar.py`, que gera `curriculo/html/` e os PDFs em `assets/curriculo/`. Este arquivo guarda os critérios, a base e o histórico das perguntas; o texto encurtado para caber em 1 página está só no gerador.

Telefone e e-mail ficam em `docs/privado/CONTATO.md`, que não vai para o GitHub (o repositório é público). O PDF público sai sem os dois; a versão com contato é gerada na máquina com `python curriculo/gerar.py --email ... --telefone ...` e fica em `docs/privado/curriculo/`.

## Critérios usados

- Uma página por versão.
- Texto selecionável, sem colunas nem tabelas complexas, para os sistemas de triagem (ATS) lerem bem.
- Tópicos começam por verbo de ação. Nenhum número inventado: entram só números que o Enrico informar.
- Três versões, uma por área: Dados, Desenvolvimento de Software, Automação Industrial. Muda o resumo, a ordem dos tópicos, os projetos e a ordem das competências. Experiência e formação são as mesmas.
- Objetivo: efetivação.
- Sem foto, idade, estado civil, CPF ou endereço completo.
- Versão em inglês depois que o português estiver aprovado.

## Partes comuns

### Cabeçalho

Enrico Montovanelli
Vitória, ES · [e-mail e telefone só na versão privada] · linkedin.com/in/enricomontovanelli · github.com/EnricoMontova · enricomontova.github.io

### Experiência

**ArcelorMittal Tubarão** · Estagiário de Engenharia de Software · fev. 2026 até o momento
Automação da Laminação de Tiras a Quente (LTQ), sistemas de Nível 2

Tópicos disponíveis (cada versão usa a sua ordem):
- (L) Implemento modificações e atualizações na lógica do processo da LTQ em C/C++, em servidores Tru64 UNIX do sistema de Nível 2.
- (V) Mantenho e atualizo as telas de operação da laminação desenvolvidas em VB6.
- (C) Participo do desenvolvimento das novas telas de operação em C# com Visual Studio 2022.
- (D) Desenvolvo dashboards e análises de BI com dados do processo, em SQL e Databricks, para auditoria e pesquisa.
- (R) Implemento as demandas da rotina de automação da LTQ e acompanho sua implantação em produção.
- (M) Mantenho e monitoro o envio de dados do processo ao data lake, em Java e SQL. (26/11/2026)
- (T) Elaboro documentação técnica: especificações funcionais e técnicas, cadernos de teste e planos de implantação e contingência.

**Gol Linhas Aéreas** · Jovem Aprendiz, Recursos Humanos · jul. 2024 a set. 2025
- Organizei documentos e planilhas e cuidei da emissão e do retorno de credenciais no RH (Excel, Word, PowerPoint).
- Apoiei os agentes do serviço de bagagens (LL) no desembarque: recebimento, inspeção e liberação, tratamento de bagagens extraviadas ou danificadas, em conjunto com a segurança e o transporte do aeroporto.

Texto enviado pelo Enrico em 26/11/2026 (base dos dois tópicos acima, adaptado para caber):
"Durante meu período na GOL, atuei no setor de RH, cuidando da organização de documentos, emissão e retorno de credenciais e apoio nas rotinas operacionais de serviço de bagagens (LL).
• Apoio ao setor de Recursos Humanos, com organização de documentos, controle de planilhas e suporte em rotinas administrativas. Principais ferramentas: Excel, PowerPoint e Word;
• Apoio aos agentes de aeroporto, recebendo, inspecionando e liberando bagagens no desembarque, resolvendo incidentes como bagagens perdidas ou danificadas, trabalhando coordenadamente com os setores de segurança e transporte do aeroporto, garantindo que as bagagens fossem entregas corretamente;
• Desenvolvimento de competências em trabalho em equipe, comunicação, trabalho sob pressão e processos administrativos."

### Formação

**FAESA** · Bacharelado em Engenharia da Computação · 9º período · conclusão prevista para ago. 2027
TCC: Desenvolvimento de um sistema digital para rastreabilidade e gestão de análises de risco no ponto de trabalho em plantas siderúrgicas.

### Idiomas

Português nativo · Inglês fluente

### Certificações

- DataCamp: Intermediate SQL (nov. 2026), Introduction to Databricks (ago. 2026), Introduction to Shell (abr. 2026), Introduction to SQL (abr. 2026), Understanding Cloud Computing (abr. 2026), Understanding Data Engineering (abr. 2026)
- Udemy: Java COMPLETO, Programação Orientada a Objetos + Projetos (54,5 h, nov. 2025); Algoritmos e Lógica de Programação (30,5 h, jul. 2025)

## Versão 1: Dados

**Resumo**
Estudante de Engenharia da Computação (9º período, FAESA) e estagiário na automação da Laminação de Tiras a Quente da ArcelorMittal Tubarão, onde desenvolvo dashboards e análises com dados do processo em SQL e Databricks. Complemento a formação com a trilha de Engenharia de Dados da DataCamp e busco a efetivação na área de dados.

**Ordem dos tópicos da ArcelorMittal:** D, L, C, V, T

**Competências**
- Dados: SQL, Databricks, dashboards e BI
- Linguagens: C, C++, C#, Java, VB6
- Sistemas: Unix Tru64, Windows
- Documentação técnica

**Projetos:** Detecção de Incêndios IoT (monitoramento de temperatura e gases por sensores).

**Certificações:** DataCamp primeiro.

## Versão 2: Desenvolvimento de Software

**Resumo**
Estudante de Engenharia da Computação (9º período, FAESA) e estagiário de engenharia de software na ArcelorMittal Tubarão. Desenvolvo e mantenho software de sistemas industriais de Nível 2 em C/C++ sobre Tru64 UNIX, telas de operação em VB6 e as novas telas em C#. Busco a efetivação como desenvolvedor.

**Ordem dos tópicos da ArcelorMittal:** L, C, V, D, T

**Competências**
- Linguagens: C, C++, C#, Java, VB6
- Ferramentas: Visual Studio 2022
- Sistemas: Unix Tru64, Windows
- Dados: SQL, Databricks
- Documentação técnica

**Projetos:** Drone com Sistemas Embarcados; Detecção de Incêndios IoT.

**Certificações:** Udemy (Java, Algoritmos) primeiro, depois DataCamp.

## Versão 3: Automação Industrial

**Resumo**
Estudante de Engenharia da Computação (9º período, FAESA) e estagiário na automação da Laminação de Tiras a Quente da ArcelorMittal Tubarão, atuando na lógica de processo e nas telas de operação dos sistemas de Nível 2, que ligam o controle da planta à gestão da produção. Experiência acadêmica com microcontroladores, IoT e controle PID. Busco a efetivação na automação.

**Ordem dos tópicos da ArcelorMittal:** R, L, V, C, D, T

**Competências**
- Automação: sistemas de Nível 2, integração com Níveis 1 e 3
- Linguagens: C, C++, C#, VB6
- Embarcados: Arduino, ESP32, sensores, controle PID
- Sistemas: Unix Tru64, Windows XP, 10 e 11
- (Dados e Documentação saíram em 26/11/2026: repetiam a experiência e não cabiam em 1 página.)

**Projetos:** Drone com Sistemas Embarcados; Carrinho de Controle Remoto (apresentado no ESX 2025, com controle pelo celular pelos visitantes); Detecção de Incêndios IoT.

**Certificações:** Udemy (Java, Algoritmos) e DataCamp Intermediate SQL, Introduction to Databricks e Introduction to Shell (26/11/2026).

## Competências (26/11/2026)

As listas de cada versão acima são o rascunho original. A versão final troca "Linguagens", "Ferramentas" e "Dados" por "Tecnologias do estágio" e "Estudos e projetos" (escolha do Enrico, opção 2); o texto exato está em `curriculo/gerar.py`.

## Ambiente do estágio (informado pelo Enrico em 26/11/2026)

- VB6: programação numa estação remota com Windows XP.
- C# e Visual Studio 2022 (telas novas): Windows 10.
- Sistema CDP: envio de dados ao data lake, em Java e SQL, em Windows 10. Papel do Enrico: "Mantenho e monitoro".
- Windows 11: não citado no estágio; saiu do currículo.
- Ordem dos tópicos com o novo tópico M: Dados D, M, L, C, V, T; Software L, C, V, M, D, T; Automação R, L, V, C, M, D, T.

## Rodada 2 (respondida em 26/11/2026)

1. Documentação técnica (tópico T) no estágio? Resposta: "Sim, faço os documentos". Tópico mantido.
2. Participação nas demandas (tópico R)? Resposta: "Implemento e implanto" (recebe a demanda definida). Tópico reescrito.
3. Números divulgáveis? Resposta: "Sem números divulgáveis". Tópicos ficam qualitativos.
4. Mudanças e Fretes no currículo? Resposta: fica fora (continua na página Carreira).
5. Formato final? Resposta: PDF no repositório, gerado de HTML, com link na página Carreira.
6. Contato no PDF público (conflito com a decisão de 25/11)? Resposta: duas versões, pública sem e-mail e telefone e privada com os dois.
7. Certificações da versão Automação? Resposta: Udemy e as três DataCamp ligadas ao estágio.

## Próximos passos

- Enrico revisa os três PDFs em português.
- Depois da aprovação: link de download na página Carreira e versão em inglês.
