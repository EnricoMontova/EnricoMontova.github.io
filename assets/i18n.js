/* Troca de idioma PT/EN do site (decisão de 26/11/2026).
   As páginas continuam escritas em português; este arquivo troca os textos na hora.
   Ordem de escolha do idioma: ?lang=en|pt no endereço, depois a última escolha salva, depois português.
   Para traduzir um texto novo: acrescentar a linha em EN, com o texto exato que aparece na página. */
(function () {
  'use strict';

  var EN = {
    // ---------------------------------------------------------------- barras e menu
    'Enrico.Montovanelli / portfólio': 'Enrico.Montovanelli / portfolio',
    'Enrico.Montovanelli / carreira': 'Enrico.Montovanelli / career',
    'Enrico.Montovanelli / projetos': 'Enrico.Montovanelli / projects',
    'Eng. de Software na automação': 'Software Eng. in automation',
    'Eng. da Computação': 'Computer Eng.',
    'Vitória, ES': 'Vitória, ES, Brazil',
    'Carreira': 'Career',
    'Projetos': 'Projects',
    'Selecione uma seção': 'Select a section',
    'Currículo': 'Resume',
    'Seções': 'Sections',
    'Contato': 'Contact',
    'Carreira, Enrico Montovanelli': 'Career, Enrico Montovanelli',
    'Projetos, Enrico Montovanelli': 'Projects, Enrico Montovanelli',
    'Portfólio de Enrico Montovanelli: estudante de Engenharia da Computação (FAESA) e estagiário de Engenharia de Software na automação da ArcelorMittal Tubarão.':
      'Portfolio of Enrico Montovanelli: Computer Engineering student (FAESA) and Software Engineering intern in automation at ArcelorMittal Tubarão.',
    'Enrico Montovanelli, portfólio: fundo preto com grão, nome em letra larga e barras de terminal':
      'Enrico Montovanelli, portfolio: grainy black background, name in wide letters and terminal bars',

    // ---------------------------------------------------------------- carreira
    'Estudante de Engenharia da Computação no 9º período, pela FAESA. Hoje sou estagiário de engenharia de software na automação da Laminação de Tiras a Quente da ArcelorMittal Tubarão.':
      'Computer Engineering student in the 9th semester at FAESA. I am currently a software engineering intern in Hot Strip Mill automation at ArcelorMittal Tubarão.',
    'Trajetória': 'Timeline',
    '14 meses': '14 months',
    'Jovem aprendiz, RH': 'Apprentice, HR',
    'Fretes': 'Freight',
    'Ajudante de mudanças': 'Moving helper',
    'hoje': 'today',
    'Estagiário de Engenharia de Software': 'Software Engineering Intern',
    'Certificados': 'Certificates',
    'Certificado': 'Certificate',
    '4 a 6 h': '4 to 6 h',
    '30 min a 1 h': '30 min to 1 h',
    '54,5 h': '54.5 h',
    '30,5 h': '30.5 h',
    'Estágio': 'Internship',
    'Atuo na automação da LTQ, em sistemas de Nível 2: a camada que liga o controle da planta (Nível 1) à gestão da produção (Nível 3).':
      'I work in Hot Strip Mill automation, on Level 2 systems: the layer that connects plant control (Level 1) to production management (Level 3).',
    'Mudanças e Fretes': 'Moving and Freight',
    'Trabalhei ao lado do meu pai em fretes e mudanças, no carregamento e transporte de móveis.':
      'I worked alongside my father in freight and moving services, loading and transporting furniture.',
    'Jovem aprendiz': 'Apprentice',
    'Recursos Humanos': 'Human Resources',
    'Apoiei o setor de RH com controle de planilhas e suporte às rotinas administrativas.':
      'I supported the HR department with spreadsheet control and administrative routines.',
    'Formação': 'Education',
    'até ago. 2027 (previsão)': 'until Aug. 2027 (expected)',
    'Engenharia da Computação': 'Computer Engineering',
    'No 9º período, com o TCC em andamento. Em paralelo, estudo Engenharia de Dados na DataCamp.':
      '9th semester, with the capstone project in progress. Alongside it, I study Data Engineering on DataCamp.',
    'Disciplinas': 'Courses',
    'Disciplinas da FAESA': 'FAESA courses',
    'cursando': 'in progress',
    'aproveitada': 'credit transferred',
    'Ferramentas': 'Tools',
    'Linguagens': 'Languages',
    'C, C++, C#, Java e VB6.': 'C, C++, C#, Java and VB6.',
    'Sistemas': 'Systems',
    'Unix Tru64 e Windows XP, 10 e 11.': 'Unix Tru64 and Windows XP, 10 and 11.',
    'Dados': 'Data',
    'SQL e Databricks.': 'SQL and Databricks.',
    'Documentação': 'Documentation',
    'Especificação funcional e técnica, caderno de testes, planos de implantação e contingência.':
      'Functional and technical specifications, test plans, deployment and contingency plans.',
    'Automação': 'Automation',
    'Automação / Software / Dados': 'Automation / Software / Data',
    'Inglês fluente': 'Fluent English',
    'Baixar currículo de Dados em português (PDF)': 'Download the Data resume in Portuguese (PDF)',
    'Baixar currículo de Dados em inglês (PDF)': 'Download the Data resume in English (PDF)',
    'Baixar currículo de Software em português (PDF)': 'Download the Software resume in Portuguese (PDF)',
    'Baixar currículo de Software em inglês (PDF)': 'Download the Software resume in English (PDF)',
    'Baixar currículo de Automação em português (PDF)': 'Download the Automation resume in Portuguese (PDF)',
    'Baixar currículo de Automação em inglês (PDF)': 'Download the Automation resume in English (PDF)',

    // disciplinas da FAESA
    'Controle Dinâmico de Sistemas': 'Dynamic Systems Control',
    'Redes Industriais e IIoT': 'Industrial Networks and IIoT',
    'Projeto do Trabalho de Conclusão de Curso': 'Capstone Project Proposal',
    'Organização do Trabalho Científico': 'Scientific Writing and Methods',
    'Sociedade, Cidadania e Diversidade': 'Society, Citizenship and Diversity',
    'Processamento Digital de Sinais': 'Digital Signal Processing',
    'Processos Estocásticos e Simulações': 'Stochastic Processes and Simulation',
    'Robótica e Sistemas Inteligentes': 'Robotics and Intelligent Systems',
    'Teoria da Informação e Codificação': 'Information Theory and Coding',
    'Sustentabilidade e Gestão Ambiental': 'Sustainability and Environmental Management',
    'Bancos de Dados e Big Data': 'Databases and Big Data',
    'Empreendedorismo e Inovação': 'Entrepreneurship and Innovation',
    'Processamento de Imagens': 'Image Processing',
    'Projeto Integrador Engenharia de Computação IV': 'Computer Engineering Integrative Project IV',
    'Sistemas de Comunicação': 'Communication Systems',
    'Sistemas Embarcados': 'Embedded Systems',
    'Ética e Pensamento Crítico': 'Ethics and Critical Thinking',
    'Eletrônica Analógica e Aplicações': 'Analog Electronics and Applications',
    'Engenharia de Software e Agilidade': 'Software Engineering and Agile',
    'Machine Learning': 'Machine Learning',
    'Microprocessadores e Microcontroladores': 'Microprocessors and Microcontrollers',
    'Projeto Integrador Engenharia de Computação III': 'Computer Engineering Integrative Project III',
    'Sistemas Operacionais': 'Operating Systems',
    'Habilidades de Estudo e Comunicação': 'Study and Communication Skills',
    'Circuitos Elétricos Avançados': 'Advanced Electric Circuits',
    'Eletrônica': 'Electronics',
    'Linguagem de Programação': 'Programming Language',
    'Pesquisa e Ordenação': 'Searching and Sorting',
    'Projeto Integrador Engenharia da Computação II': 'Computer Engineering Integrative Project II',
    'Teoria da Computação': 'Theory of Computation',
    'Arquitetura de Computadores': 'Computer Architecture',
    'Circuitos Elétricos': 'Electric Circuits',
    'Estrutura de Dados': 'Data Structures',
    'Projeto Integrador Engenharia da Computação I': 'Computer Engineering Integrative Project I',
    'Técnicas Avançadas de Programação': 'Advanced Programming Techniques',
    'Visão Empresária': 'Business Vision',
    'Design em Engenharia': 'Engineering Design',
    'Fenômenos de Transporte': 'Transport Phenomena',
    'Matemática Aplicada III': 'Applied Mathematics III',
    'Modelos Físicos III': 'Physical Models III',
    'Projeto Integrador Engenharias II': 'Engineering Integrative Project II',
    'Resistência dos Materiais': 'Strength of Materials',
    'Matemática Aplicada II': 'Applied Mathematics II',
    'Mecânica Estática': 'Statics',
    'Modelos Físicos II': 'Physical Models II',
    'Desenho Técnico': 'Technical Drawing',
    'Circuitos Digitais': 'Digital Circuits',
    'Ciência e Tecnologia dos Materiais': 'Materials Science and Technology',
    'Probabilidade e Estatística': 'Probability and Statistics',
    'Matemática Aplicada I': 'Applied Mathematics I',
    'Modelos Físicos I': 'Physical Models I',
    'Projeto Integrador Engenharias I': 'Engineering Integrative Project I',
    'Química Geral': 'General Chemistry',
    'Técnicas de Programação': 'Programming Techniques',
    'Pensamento Matemático': 'Mathematical Thinking',

    // ---------------------------------------------------------------- projetos
    'Projetos pessoais e projetos da graduação em Engenharia da Computação, na FAESA.':
      'Personal projects and projects from my Computer Engineering degree at FAESA.',
    'Setor / 01 · Pessoais': 'Sector / 01 · Personal',
    'Setor / 02 · Faculdade': 'Sector / 02 · University',
    'Projetos pessoais': 'Personal projects',
    'Em desenvolvimento.': 'In development.',
    'Projetos da faculdade': 'University projects',
    'Disciplina de Sistemas Embarcados': 'Embedded Systems course',
    'Drone com Sistemas Embarcados': 'Drone with Embedded Systems',
    'Drone controlado por microcontrolador, com controle de voo e estabilidade por acelerômetro e giroscópio e controle remoto sem fio via ESP32.':
      'Microcontroller-driven drone with flight control and stabilization by accelerometer and gyroscope, and wireless remote control via ESP32.',
    'ESP32 • MPU6050 • Motores e hélices • C/C++ • Controle PID • Firmware embarcado':
      'ESP32 • MPU6050 • Motors and propellers • C/C++ • PID control • Embedded firmware',
    'Apresentado no ESX 2025': 'Shown at ESX 2025',
    'Carrinho de Controle Remoto': 'Remote-Controlled Car',
    'Veículo controlado remotamente com Arduino, sensores ultrassônicos e comunicação sem fio. No estande da FAESA no ESX 2025, os visitantes controlavam os carrinhos pelo celular numa arena de futebol de robôs.':
      'Remote-controlled vehicle with Arduino, ultrasonic sensors and wireless communication. At the FAESA booth at ESX 2025, visitors drove the cars from their phones in a robot soccer arena.',
    'Apresentado no ESX 2025, Espírito Santo Innovation Experience': 'Shown at ESX 2025, Espírito Santo Innovation Experience',
    'Arduino • Bluetooth HC-05 • Motores DC • Sensores ultrassônicos • C/C++': 'Arduino • Bluetooth HC-05 • DC motors • Ultrasonic sensors • C/C++',
    'Projeto Integrador II': 'Integrative Project II',
    'Detecção de Incêndios IoT': 'IoT Fire Detection',
    'Monitoramento de temperatura e gases em ambientes industriais e recicladoras, com sensores de chama e de gás, para prevenção de focos de incêndio.':
      'Temperature and gas monitoring for industrial and recycling sites, with flame and gas sensors, to prevent fire outbreaks.',
    'Projeto Integrador, 1º período': 'Integrative Project, 1st semester',
    'Balança Digital com Arduino': 'Arduino Digital Scale',
    'Balança digital funcional que aplica a Lei de Hooke e conceitos de física, automação e programação.':
      'Working digital scale that applies Hooke\'s law and concepts of physics, automation and programming.',
    'Arduino UNO • HC-SR04 • Display LCD 16x2 • C/C++': 'Arduino UNO • HC-SR04 • 16x2 LCD display • C/C++',
    'Sistemas embarcados • IoT • Automação': 'Embedded systems • IoT • Automation',
    'Estrela de quatro pontas se desfazendo em partículas': 'Four-pointed star dissolving into particles'
  };

  var CAMINHOS = { '/carreira': '/career', '/projetos': '/projects', '/currículo': '/resume' };
  var MESES = { 'jan.': 'Jan.', 'fev.': 'Feb.', 'mar.': 'Mar.', 'abr.': 'Apr.', 'mai.': 'May', 'jun.': 'Jun.',
                'jul.': 'Jul.', 'ago.': 'Aug.', 'set.': 'Sep.', 'out.': 'Oct.', 'nov.': 'Nov.', 'dez.': 'Dec.' };

  function caminho(c) { return CAMINHOS[c] || c; }
  function data(d) { return d.replace(/\b(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)\./g, function (m) { return MESES[m]; }); }

  // texto em portugues -> ingles (ou null se nao houver traducao)
  function traduzir(t) {
    if (Object.prototype.hasOwnProperty.call(EN, t)) return EN[t];
    var m;
    if ((m = t.match(/^Média (\d+),(\d+)$/))) return 'Grade ' + m[1] + '.' + m[2];
    if ((m = t.match(/^(\d{2})\/(\d{2})\/(\d{4})$/))) return parseInt(m[1], 10) + ' ' + ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][parseInt(m[2], 10) - 1] + ' ' + m[3];
    if ((m = t.match(/^Arquivo \/ (.+)$/))) return 'File / ' + m[1];
    if ((m = t.match(/^> abrir (.+)$/))) return '> open ' + caminho(m[1]);
    if ((m = t.match(/^> voltar (.+)$/))) return '> back ' + caminho(m[1]);
    if ((m = t.match(/^> (\/\S+)$/))) return '> ' + caminho(m[1]);
    if ((m = t.match(/^(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)\. \d{4}$/))) return data(t);
    if ((m = t.match(/^(.+) até (hoje|.+)$/)) && /\d{4}/.test(m[1])) return data(m[1]) + ' to ' + (m[2] === 'hoje' ? 'today' : data(m[2]));
    if (CAMINHOS[t]) return CAMINHOS[t];
    return null;
  }

  var ATRIBUTOS = ['aria-label', 'alt', 'title', 'data-transicao', 'data-alvo'];
  var originaisTexto = [];   // [no, texto original]
  var originaisAttr = [];    // [elemento, atributo, valor original]
  var originaisHref = [];    // [link, href original]
  var idiomaAtual = 'pt';

  function aplicarEN() {
    var anda = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        var p = n.parentNode && n.parentNode.nodeName;
        return (p === 'SCRIPT' || p === 'STYLE') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });
    var n;
    while ((n = anda.nextNode())) {
      var bruto = n.nodeValue, limpo = bruto.replace(/\s+/g, ' ').trim();
      if (!limpo) continue;
      var en = traduzir(limpo);
      if (en !== null && en !== limpo) {
        originaisTexto.push([n, bruto]);
        n.nodeValue = bruto.replace(/\S[\s\S]*\S|\S/, en);
      }
    }
    var els = document.querySelectorAll('[' + ATRIBUTOS.join('],[') + '],meta[name="description"],meta[property="og:description"],meta[property="og:title"],meta[property="og:image:alt"],meta[name="twitter:image:alt"]');
    for (var i = 0; i < els.length; i++) {
      var attrs = els[i].nodeName === 'META' ? ['content'] : ATRIBUTOS;
      for (var j = 0; j < attrs.length; j++) {
        var v = els[i].getAttribute(attrs[j]);
        if (!v) continue;
        var t = traduzir(v.trim());
        if (t !== null && t !== v) { originaisAttr.push([els[i], attrs[j], v]); els[i].setAttribute(attrs[j], t); }
      }
    }
    // links internos levam ?lang=en, para o idioma seguir mesmo sem armazenamento no navegador
    var links = document.querySelectorAll('a[href]');
    for (var k = 0; k < links.length; k++) {
      var h = links[k].getAttribute('href');
      if (!/^[a-z0-9_-]+\.html(#.*)?$/i.test(h)) continue;
      originaisHref.push([links[k], h]);
      var partes = h.split('#');
      links[k].setAttribute('href', partes[0] + '?lang=en' + (partes[1] !== undefined ? '#' + partes[1] : ''));
    }
    var tt = traduzir(document.title);
    if (tt) { originaisAttr.push([document, 'title', document.title]); document.title = tt; }
    document.documentElement.setAttribute('lang', 'en');
  }

  function voltarPT() {
    var i;
    for (i = 0; i < originaisTexto.length; i++) originaisTexto[i][0].nodeValue = originaisTexto[i][1];
    for (i = 0; i < originaisAttr.length; i++) {
      if (originaisAttr[i][0] === document) document.title = originaisAttr[i][2];
      else originaisAttr[i][0].setAttribute(originaisAttr[i][1], originaisAttr[i][2]);
    }
    for (i = 0; i < originaisHref.length; i++) originaisHref[i][0].setAttribute('href', originaisHref[i][1]);
    originaisTexto = []; originaisAttr = []; originaisHref = [];
    document.documentElement.setAttribute('lang', 'pt-BR');
  }

  // textos que os scripts das paginas trocam depois (status do menu e mensagem da transicao)
  function vigiar(id) {
    var el = document.getElementById(id);
    if (!el || !window.MutationObserver) return;
    new MutationObserver(function () {
      if (idiomaAtual !== 'en') return;
      var t = el.textContent.trim(), en = traduzir(t);
      if (en !== null && en !== t) el.textContent = en;
    }).observe(el, { childList: true, characterData: true, subtree: true });
  }

  function marcarBotoes() {
    var bs = document.querySelectorAll('.idioma button');
    for (var i = 0; i < bs.length; i++) bs[i].setAttribute('aria-pressed', bs[i].getAttribute('data-lang') === idiomaAtual ? 'true' : 'false');
  }

  function definir(idioma, salvar) {
    if (idioma === idiomaAtual) return;
    if (idioma === 'en') aplicarEN(); else voltarPT();
    idiomaAtual = idioma;
    marcarBotoes();
    if (salvar) { try { localStorage.setItem('idioma', idioma); } catch (e) {} }
    try {
      var u = new URL(location.href);
      if (idioma === 'en') u.searchParams.set('lang', 'en'); else u.searchParams.delete('lang');
      history.replaceState(null, '', u.toString());
    } catch (e) {}
  }

  function criarBotoes() {
    var estilo = document.createElement('style');
    estilo.textContent =
      '.idioma{display:inline-flex;align-items:center;gap:2px;font:inherit;letter-spacing:inherit;text-transform:uppercase}' +
      '.idioma button{font:inherit;letter-spacing:inherit;text-transform:inherit;color:#E8E6E1;background:none;border:0;padding:4px 6px;margin:-4px 0;cursor:pointer}' +
      '.idioma button[aria-pressed="true"]{background:#E8E6E1;color:#0E0E0F}' +
      '.idioma button:hover,.idioma button:focus-visible{outline:1.5px solid #E8E6E1;outline-offset:1px}' +
      '.idioma span{opacity:.6}';
    document.head.appendChild(estilo);
    var hora = document.getElementById('hora');
    if (!hora) return;
    var grupo = document.createElement('span');
    grupo.className = 'idioma';
    grupo.setAttribute('role', 'group');
    grupo.setAttribute('aria-label', 'Idioma / Language');
    grupo.innerHTML = '<button type="button" data-lang="pt" lang="pt-BR">PT</button><span aria-hidden="true">/</span><button type="button" data-lang="en" lang="en">EN</button>';
    hora.parentNode.insertBefore(grupo, hora);
    grupo.addEventListener('click', function (ev) {
      var b = ev.target.closest('button');
      if (b) definir(b.getAttribute('data-lang'), true);
    });
  }

  function idiomaInicial() {
    var p = null;
    try { p = new URL(location.href).searchParams.get('lang'); } catch (e) {}
    if (p === 'en' || p === 'pt') { try { localStorage.setItem('idioma', p); } catch (e) {} return p; }
    try { var s = localStorage.getItem('idioma'); if (s === 'en' || s === 'pt') return s; } catch (e) {}
    return 'pt';
  }

  criarBotoes();
  vigiar('status');
  vigiar('capa-msg');
  marcarBotoes();
  definir(idiomaInicial(), false);
})();
