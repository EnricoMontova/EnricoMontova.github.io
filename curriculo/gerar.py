"""Gera os curriculos do Enrico (HTML + PDF), um por area, em portugues e ingles.

Uso:
  python curriculo/gerar.py
      Versao publica (sem e-mail e telefone). Saida: curriculo/html/ e assets/curriculo/.

  python curriculo/gerar.py --email nome@exemplo.com --telefone "+55 27 90000-0000"
      Versao para candidaturas, com contato. Saida: docs/privado/curriculo/ (fora do Git).

  --idioma pt | en | todos (padrao: todos)

Precisa do Google Chrome ou do Microsoft Edge instalado (usado para imprimir o PDF).
O texto vem de docs/CURRICULO.md; qualquer mudanca de texto entra nos dois lugares.
"""

import argparse
import html
import os
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "curriculo"

NOME = "Enrico Montovanelli"
LINKS = [
    ("linkedin.com/in/enricomontovanelli", "https://www.linkedin.com/in/enricomontovanelli/"),
    ("github.com/EnricoMontova", "https://github.com/EnricoMontova"),
    ("enricomontova.github.io", "https://enricomontova.github.io"),
]

# ================================================================ portugues

PT_DATACAMP = "DataCamp (2026): Intermediate SQL, Introduction to Databricks, Introduction to Shell, Introduction to SQL, Understanding Cloud Computing, Understanding Data Engineering."
PT_UDEMY = "Udemy (2025): Java COMPLETO: Programação Orientada a Objetos + Projetos (54,5 h); Algoritmos e Lógica de Programação (30,5 h)."
PT_DOC = ("Documentação", "especificações, cadernos de teste, planos de implantação e contingência")

PT = {
    "lang": "pt-BR",
    "arquivo": "enrico-montovanelli-curriculo-{v}",
    "nomes_versao": {"dados": "dados", "software": "software", "automacao": "automacao"},
    "rotulos": {
        "doc": "Currículo", "resumo": "Resumo", "experiencia": "Experiência", "formacao": "Formação",
        "competencias": "Competências", "projetos": "Projetos acadêmicos", "certificacoes": "Certificações",
    },
    "cidade": "Vitória, ES",
    "estagio": {
        "empresa": "ArcelorMittal Tubarão",
        "periodo": "fev. 2026 até o momento",
        "cargo": "Estagiário de Engenharia de Software",
        "nota": "Automação da Laminação de Tiras a Quente (LTQ), sistemas de Nível 2",
    },
    "topicos": {
        "L": "Implemento modificações na lógica do processo da LTQ em C/C++, em servidores Tru64 UNIX do Nível 2.",
        "V": "Mantenho e atualizo as telas de operação da laminação desenvolvidas em VB6.",
        "C": "Participo do desenvolvimento das novas telas de operação em C# com Visual Studio 2022.",
        "D": "Desenvolvo dashboards e análises de BI com dados do processo, em SQL e Databricks, para auditoria e pesquisa.",
        "M": "Mantenho e monitoro o envio de dados do processo ao data lake, em Java e SQL.",
        "R": "Implemento as demandas da rotina de automação da LTQ e acompanho sua implantação em produção.",
        "T": "Elaboro especificações funcionais e técnicas, cadernos de teste e planos de implantação e contingência.",
    },
    "gol": {
        "empresa": "Gol Linhas Aéreas",
        "cargo": "Jovem Aprendiz, Recursos Humanos",
        "periodo": "jul. 2024 a set. 2025",
        "topicos": [
            "Organizei documentos e planilhas e cuidei da emissão e do retorno de credenciais no RH (Excel, Word, PowerPoint).",
            "Apoiei os agentes do serviço de bagagens (LL) no desembarque: recebimento, inspeção e liberação, tratamento de bagagens extraviadas ou danificadas, em conjunto com a segurança e o transporte do aeroporto.",
        ],
    },
    "formacao": {
        "instituicao": "FAESA",
        "curso": "Bacharelado em Engenharia da Computação",
        "periodo": "9º período · conclusão prevista para ago. 2027",
        "tcc": "TCC: sistema digital para rastreabilidade e gestão de análises de risco no ponto de trabalho em plantas siderúrgicas.",
    },
    "idiomas": ("Idiomas", "português nativo, inglês fluente"),
    "projetos": {
        "drone": {
            "nome": "Drone com Sistemas Embarcados",
            "contexto": "FAESA, disciplina Sistemas Embarcados",
            "texto": "Controle de voo e estabilidade com acelerômetro e giroscópio (MPU6050) e controle remoto via ESP32. C/C++, PID.",
        },
        "carrinho": {
            "nome": "Carrinho de Controle Remoto",
            "contexto": "FAESA, apresentado no ESX 2025",
            "texto": "Arduino, sensores ultrassônicos e Bluetooth (HC-05). No ESX 2025, o público pilotava os carrinhos pelo celular.",
        },
        "incendio": {
            "nome": "Detecção de Incêndios IoT",
            "contexto": "FAESA, Projeto Integrador II",
            "texto": "Monitoramento IoT de temperatura e gases em indústrias e recicladoras, com MQ-135, MLX90614, Arduino e C/C++.",
        },
    },
    "versoes": {
        "dados": {
            "rotulo": "Dados",
            "resumo": "Estudante de Engenharia da Computação (9º período, FAESA) e estagiário na automação da Laminação de Tiras a Quente da ArcelorMittal Tubarão, onde desenvolvo dashboards e análises com dados do processo em SQL e Databricks e mantenho o envio desses dados ao data lake. Complemento a formação com a trilha de Engenharia de Dados da DataCamp e busco a efetivação na área de dados.",
            "ordem": "DMLCVT",
            "competencias": [
                ("Tecnologias do estágio", "SQL e Databricks (dashboards e BI), Java e SQL (envio de dados ao data lake), C/C++ em Tru64 UNIX, C# em Windows 10, VB6 em Windows XP (estação remota)"),
                ("Estudos e projetos", "Arduino, trilha de Engenharia de Dados (DataCamp)"),
                PT_DOC,
            ],
            "projetos": ["incendio"],
            "certificacoes": [PT_DATACAMP, PT_UDEMY],
        },
        "software": {
            "rotulo": "Desenvolvimento de Software",
            "resumo": "Estudante de Engenharia da Computação (9º período, FAESA) e estagiário de engenharia de software na ArcelorMittal Tubarão. Desenvolvo e mantenho software de sistemas industriais de Nível 2 em C/C++ sobre Tru64 UNIX, telas de operação em VB6 e as novas telas em C#. Busco a efetivação como desenvolvedor.",
            "ordem": "LCVMDT",
            "competencias": [
                ("Tecnologias do estágio", "C/C++ em Tru64 UNIX, C# (Visual Studio 2022, Windows 10), VB6 em Windows XP (estação remota), Java e SQL (envio de dados ao data lake), Databricks"),
                ("Estudos e projetos", "Arduino, ESP32"),
                PT_DOC,
            ],
            "projetos": ["drone", "incendio"],
            "certificacoes": [PT_UDEMY, PT_DATACAMP],
        },
        "automacao": {
            "rotulo": "Automação Industrial",
            "resumo": "Estudante de Engenharia da Computação (9º período, FAESA) e estagiário na automação da Laminação de Tiras a Quente da ArcelorMittal Tubarão, na lógica de processo e nas telas de operação dos sistemas de Nível 2. Experiência acadêmica com microcontroladores, IoT e controle PID. Busco a efetivação na automação.",
            "ordem": "RLVCMDT",
            "competencias": [
                ("Automação", "sistemas de Nível 2, integração com Níveis 1 e 3"),
                ("Tecnologias do estágio", "C/C++ em Tru64 UNIX, VB6 em Windows XP (estação remota), C# em Windows 10, Java e SQL (envio de dados ao data lake), Databricks"),
                ("Estudos e projetos", "Arduino, ESP32, sensores, controle PID"),
                # Dados e Documentacao sairam em 26/11/2026: repetiam a experiencia e nao cabiam em 1 pagina.
            ],
            "projetos": ["drone", "carrinho", "incendio"],
            # Decisao de 26/11/2026: so as DataCamp ligadas ao estagio, para caber em 1 pagina.
            "certificacoes": [PT_UDEMY, "DataCamp (2026): Intermediate SQL, Introduction to Databricks, Introduction to Shell."],
        },
    },
}

# ================================================================ ingles

EN_DATACAMP = "DataCamp (2026): Intermediate SQL, Introduction to Databricks, Introduction to Shell, Introduction to SQL, Understanding Cloud Computing, Understanding Data Engineering."
EN_UDEMY = "Udemy (2025): Java COMPLETO: Programação Orientada a Objetos + Projetos (54.5 h); Algoritmos e Lógica de Programação (30.5 h)."
EN_DOC = ("Documentation", "specifications, test plans, deployment and contingency plans")

EN = {
    "lang": "en",
    "arquivo": "enrico-montovanelli-resume-{v}",
    "nomes_versao": {"dados": "data", "software": "software", "automacao": "automation"},
    "rotulos": {
        "doc": "Resume", "resumo": "Summary", "experiencia": "Experience", "formacao": "Education",
        "competencias": "Skills", "projetos": "Academic projects", "certificacoes": "Certifications",
    },
    "cidade": "Vitória, ES, Brazil",
    "estagio": {
        "empresa": "ArcelorMittal Tubarão",
        "periodo": "Feb. 2026 to present",
        "cargo": "Software Engineering Intern",
        "nota": "Hot Strip Mill automation, Level 2 systems",
    },
    "topicos": {
        "L": "Implement changes to the Hot Strip Mill process logic in C/C++ on Tru64 UNIX Level 2 servers.",
        "V": "Maintain and update the mill's operator screens built in VB6.",
        "C": "Contribute to the development of the new operator screens in C# with Visual Studio 2022.",
        "D": "Build BI dashboards and analyses from process data in SQL and Databricks for auditing and research.",
        "M": "Maintain and monitor the process data feed to the data lake, in Java and SQL.",
        "R": "Implement Hot Strip Mill automation change requests and follow their deployment to production.",
        "T": "Write functional and technical specifications, test plans, and deployment and contingency plans.",
    },
    "gol": {
        "empresa": "Gol Linhas Aéreas",
        "cargo": "Apprentice, Human Resources",
        "periodo": "Jul. 2024 to Sep. 2025",
        "topicos": [
            "Organized HR documents and spreadsheets; issued and collected staff credentials (Excel, Word, PowerPoint).",
            "Supported baggage service agents at arrivals: receiving, inspecting and releasing bags, and handling lost or damaged baggage together with airport security and transportation teams.",
        ],
    },
    "formacao": {
        "instituicao": "FAESA",
        "curso": "Bachelor of Engineering in Computer Engineering",
        "periodo": "9th semester · expected graduation Aug. 2027",
        "tcc": "Capstone: digital system for traceability and management of point-of-work risk assessments in steel plants.",
    },
    "idiomas": ("Languages", "Portuguese (native), English (fluent)"),
    "projetos": {
        "drone": {
            "nome": "Drone with Embedded Systems",
            "contexto": "FAESA, Embedded Systems course",
            "texto": "Flight control and stabilization with MPU6050 accelerometer/gyroscope and remote control via ESP32. C/C++, PID.",
        },
        "carrinho": {
            "nome": "Remote-Controlled Car",
            "contexto": "FAESA, shown at ESX 2025",
            "texto": "Arduino, ultrasonic sensors and Bluetooth (HC-05). At ESX 2025 (tech fair), visitors drove the cars by phone.",
        },
        "incendio": {
            "nome": "IoT Fire Detection",
            "contexto": "FAESA, Integrative Project II",
            "texto": "IoT monitoring of temperature and gases in industrial and recycling sites (MQ-135, MLX90614, Arduino, C/C++).",
        },
    },
    "versoes": {
        "dados": {
            "rotulo": "Data",
            "resumo": "Computer Engineering student (9th semester, FAESA) and intern in Hot Strip Mill automation at ArcelorMittal Tubarão, where I build dashboards and analyses from process data in SQL and Databricks and maintain the data feed to the data lake. I am building on this with DataCamp's Data Engineering track and seeking a full-time role in data.",
            "ordem": "DMLCVT",
            "competencias": [
                ("Internship stack", "SQL and Databricks (dashboards and BI), Java and SQL (data lake feed), C/C++ on Tru64 UNIX, C# on Windows 10, VB6 on Windows XP (remote station)"),
                ("Studies and projects", "Arduino, DataCamp Data Engineering track"),
                EN_DOC,
            ],
            "projetos": ["incendio"],
            "certificacoes": [EN_DATACAMP, EN_UDEMY],
        },
        "software": {
            "rotulo": "Software Development",
            "resumo": "Computer Engineering student (9th semester, FAESA) and software engineering intern at ArcelorMittal Tubarão. I develop and maintain Level 2 industrial software in C/C++ on Tru64 UNIX, operator screens in VB6 and the new screens in C#. Seeking a full-time developer role.",
            "ordem": "LCVMDT",
            "competencias": [
                ("Internship stack", "C/C++ on Tru64 UNIX, C# (Visual Studio 2022, Windows 10), VB6 on Windows XP (remote station), Java and SQL (data lake feed), Databricks"),
                ("Studies and projects", "Arduino, ESP32"),
                EN_DOC,
            ],
            "projetos": ["drone", "incendio"],
            "certificacoes": [EN_UDEMY, EN_DATACAMP],
        },
        "automacao": {
            "rotulo": "Industrial Automation",
            "resumo": "Computer Engineering student (9th semester, FAESA) and intern in Hot Strip Mill automation at ArcelorMittal Tubarão, working on process logic and operator screens of Level 2 systems. Academic experience with microcontrollers, IoT and PID control. Seeking a full-time role in automation.",
            "ordem": "RLVCMDT",
            "competencias": [
                ("Automation", "Level 2 systems, integration with Levels 1 and 3"),
                ("Internship stack", "C/C++ on Tru64 UNIX, VB6 on Windows XP (remote station), C# on Windows 10, Java and SQL (data lake feed), Databricks"),
                ("Studies and projects", "Arduino, ESP32, sensors, PID control"),
            ],
            "projetos": ["drone", "carrinho", "incendio"],
            "certificacoes": [EN_UDEMY, "DataCamp (2026): Intermediate SQL, Introduction to Databricks, Introduction to Shell."],
        },
    },
}

IDIOMAS = {"pt": PT, "en": EN}

# ================================================================ html

ESTRELA = '<svg class="estrela" aria-hidden="true" viewBox="0 0 40 40"><path d="M20 0 L22 18 L40 20 L22 22 L20 40 L18 22 L0 20 L18 18 Z"/></svg>'

CSS = """
@font-face{font-family:'Tektur';src:url('FONTES/tektur-latin-standard-normal.woff2') format('woff2');font-weight:400 900;font-stretch:75% 100%}
@font-face{font-family:'Marcellus';src:url('FONTES/marcellus-latin-400-normal.woff2') format('woff2')}
@font-face{font-family:'JetBrains Mono';src:url('FONTES/jetbrains-mono-latin-400-normal.woff2') format('woff2');font-weight:400}
@font-face{font-family:'JetBrains Mono';src:url('FONTES/jetbrains-mono-latin-500-normal.woff2') format('woff2');font-weight:500}
@font-face{font-family:'Inter Tight';src:url('FONTES/inter-tight-latin-400-normal.woff2') format('woff2');font-weight:400}
@font-face{font-family:'Inter Tight';src:url('FONTES/inter-tight-latin-500-normal.woff2') format('woff2');font-weight:500}
@font-face{font-family:'Inter Tight';src:url('FONTES/inter-tight-latin-600-normal.woff2') format('woff2');font-weight:600}
@font-face{font-family:'Inter Tight';src:url('FONTES/inter-tight-latin-700-normal.woff2') format('woff2');font-weight:700}
@page{size:A4;margin:15mm 16mm 14mm}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;color:#161617;font-family:'Inter Tight',Arial,sans-serif;font-size:10pt;line-height:1.36}
a{color:inherit;text-decoration:none}
.mono{font-family:'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:.08em}
header{margin-bottom:2mm}
.topo{display:flex;justify-content:space-between;font-size:7.2pt;color:#555;margin-bottom:3mm}
.nome{position:relative;display:inline-block;padding-right:16pt}
h1{margin:0;font-family:'Tektur',sans-serif;font-weight:500;font-stretch:100%;font-size:25pt;line-height:1;text-transform:uppercase;letter-spacing:.01em}
.estrela{position:absolute;right:0;top:-5pt;width:12pt;height:12pt;fill:#161617}
.regua{position:relative;height:0;border-top:1.2pt solid #161617;margin:3.2mm 0 2.4mm}
.regua::before{content:"";position:absolute;left:0;top:-4.1pt;width:7pt;height:7pt;background:#161617}
.contato{font-size:7.8pt;color:#161617}
.contato span+span::before{content:"·";margin:0 6pt;color:#888}
section{margin-top:3.6mm}
.item{break-inside:avoid}
h2{break-after:avoid}
h2{display:flex;align-items:center;gap:6pt;margin:0 0 2mm;font-family:'JetBrains Mono',monospace;font-weight:500;font-size:7.8pt;letter-spacing:.14em;text-transform:uppercase}
h2::before{content:"";width:5pt;height:5pt;background:#D21A16;flex:none}
h2::after{content:"";flex:1;border-top:.6pt solid #161617;margin-left:4pt}
p{margin:0}
.resumo{line-height:1.42}
.item{margin-bottom:2.4mm}
.item:last-child{margin-bottom:0}
.linha{display:flex;justify-content:space-between;align-items:baseline;gap:10pt}
h3{margin:0;font-family:'Marcellus',Georgia,serif;font-weight:400;font-size:10.2pt;letter-spacing:.06em;text-transform:uppercase}
.data{font-family:'JetBrains Mono',monospace;font-size:7.4pt;text-transform:uppercase;letter-spacing:.06em;white-space:nowrap;color:#333}
.sub{font-weight:600;margin-top:.6mm}
.nota{color:#444;font-size:9pt;font-weight:400}
ul{margin:1.2mm 0 0;padding-left:11pt}
li{margin:.6mm 0}
li::marker{color:#D21A16}
.comp p{margin:.5mm 0}
.comp b{font-weight:600}
.cert p{margin:.8mm 0}
"""

def e(t):
    return html.escape(t, quote=False)


def montar(T, chave, contato, pasta_fontes):
    v = T["versoes"][chave]
    r = T["rotulos"]
    est = T["estagio"]
    gol = T["gol"]
    form = T["formacao"]

    partes_contato = [f"<span>{e(T['cidade'])}</span>"]
    if contato.get("email"):
        partes_contato.append(f'<span><a href="mailto:{e(contato["email"])}">{e(contato["email"])}</a></span>')
    if contato.get("telefone"):
        partes_contato.append(f"<span>{e(contato['telefone'])}</span>")
    for texto, url in LINKS:
        partes_contato.append(f'<span><a href="{url}">{e(texto)}</a></span>')

    topicos = "".join(f"<li>{e(T['topicos'][k])}</li>" for k in v["ordem"])
    gol_topicos = "".join(f"<li>{e(t)}</li>" for t in gol["topicos"])
    comp = "".join(f"<p><b>{e(a)}:</b> {e(b)}</p>" for a, b in v["competencias"] + [T["idiomas"]])
    proj = "".join(
        f'<div class="item"><div class="linha"><h3>{e(T["projetos"][p]["nome"])}</h3>'
        f'<span class="data">{e(T["projetos"][p]["contexto"])}</span></div>'
        f'<p>{e(T["projetos"][p]["texto"])}</p></div>'
        for p in v["projetos"]
    )
    cert = "".join(f"<p>{e(c)}</p>" for c in v["certificacoes"])

    css = CSS.replace("FONTES/", pasta_fontes)
    return f"""<!DOCTYPE html>
<html lang="{T['lang']}">
<head>
<meta charset="utf-8">
<title>{e(NOME)} · {e(r['doc'])} · {e(v['rotulo'])}</title>
<meta name="author" content="{e(NOME)}">
<style>{css}</style>
</head>
<body>
<header>
<div class="topo mono"><span>{e(r['doc'])} · {e(v['rotulo'])}</span><span>enrico.montovanelli</span></div>
<div class="nome"><h1>{e(NOME)}</h1>{ESTRELA}</div>
<div class="regua"></div>
<p class="contato">{''.join(partes_contato)}</p>
</header>

<section>
<h2>{e(r['resumo'])}</h2>
<p class="resumo">{e(v['resumo'])}</p>
</section>

<section>
<h2>{e(r['experiencia'])}</h2>
<div class="item">
<div class="linha"><h3>{e(est['empresa'])}</h3><span class="data">{e(est['periodo'])}</span></div>
<p class="sub">{e(est['cargo'])} <span class="nota">· {e(est['nota'])}</span></p>
<ul>{topicos}</ul>
</div>
<div class="item">
<div class="linha"><h3>{e(gol['empresa'])}</h3><span class="data">{e(gol['periodo'])}</span></div>
<p class="sub">{e(gol['cargo'])}</p>
<ul>{gol_topicos}</ul>
</div>
</section>

<section>
<h2>{e(r['formacao'])}</h2>
<div class="item">
<div class="linha"><h3>{e(form['instituicao'])}</h3><span class="data">{e(form['periodo'])}</span></div>
<p class="sub">{e(form['curso'])}</p>
<p class="nota">{e(form['tcc'])}</p>
</div>
</section>

<section class="comp">
<h2>{e(r['competencias'])}</h2>
{comp}
</section>

<section>
<h2>{e(r['projetos'])}</h2>
{proj}
</section>

<section class="cert">
<h2>{e(r['certificacoes'])}</h2>
{cert}
</section>
</body>
</html>
"""


# ================================================================ pdf

def achar_navegador():
    candidatos = [
        shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("chromium-browser"),
        shutil.which("chrome"), shutil.which("msedge"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    for c in candidatos:
        if c and Path(c).exists():
            return c
    sys.exit("Chrome ou Edge não encontrado.")


def imprimir(navegador, origem, destino):
    subprocess.run([
        navegador, "--headless", "--disable-gpu", "--no-sandbox",
        "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={destino}", origem.resolve().as_uri(),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--email")
    ap.add_argument("--telefone")
    ap.add_argument("--idioma", choices=["pt", "en", "todos"], default="todos")
    a = ap.parse_args()
    privado = bool(a.email or a.telefone)

    if privado:
        pasta_html = pasta_pdf = RAIZ / "docs" / "privado" / "curriculo"
    else:
        pasta_html, pasta_pdf = PASTA / "html", RAIZ / "assets" / "curriculo"
    pasta_html.mkdir(parents=True, exist_ok=True)
    pasta_pdf.mkdir(parents=True, exist_ok=True)
    fontes = Path(os.path.relpath(PASTA / "fontes", pasta_html)).as_posix() + "/"

    idiomas = ["pt", "en"] if a.idioma == "todos" else [a.idioma]
    navegador = achar_navegador()
    for idioma in idiomas:
        T = IDIOMAS[idioma]
        for chave in T["versoes"]:
            nome = T["arquivo"].format(v=T["nomes_versao"][chave])
            arq_html = pasta_html / f"{nome}.html"
            arq_html.write_text(montar(T, chave, {"email": a.email, "telefone": a.telefone}, fontes), encoding="utf-8")
            arq_pdf = pasta_pdf / f"{nome}.pdf"
            imprimir(navegador, arq_html, arq_pdf)
            print(arq_pdf.relative_to(RAIZ))


if __name__ == "__main__":
    main()
