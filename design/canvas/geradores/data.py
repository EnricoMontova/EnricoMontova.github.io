P0=[
 dict(n="01",titulo="Drone com Sistemas Embarcados",curto="Drone",ctx="Disciplina de Sistemas Embarcados",
  desc="Drone controlado por microcontrolador, com controle de voo e estabilidade por acelerômetro e giroscópio e controle remoto sem fio via ESP32.",
  hw=["ESP32","MPU6050","Motores e hélices"],img="/_blob/2a88d5f937183687928c5371716eb1dc",alt="Estrutura do drone com quatro motores e hélices, ligada a uma protoboard e a uma bateria, com multímetro na bancada",sw=["C/C++","Controle PID","Firmware embarcado"],dest=None,
  apr="Integração de hardware e software para controle em tempo real."),
 dict(n="02",titulo="Carrinho de Controle Remoto",curto="Carrinho",ctx="Apresentado no ESX 2025",
  desc="Veículo controlado remotamente com Arduino, sensores ultrassônicos e comunicação sem fio. No estande da FAESA no ESX 2025, os visitantes controlavam os carrinhos pelo celular numa arena de futebol de robôs.",
  hw=["Arduino","Bluetooth HC-05","Motores DC","Sensores ultrassônicos"],sw=["C/C++"],dest="Apresentado no ESX 2025, Espírito Santo Innovation Experience",img="/_blob/91f431831a592875852f0318446f9fcc",alt="Carrinho com rodas amarelas e carenagem decorada com o nome Macarena Racing, sobre uma mesa de vidro",
  apr=None),
 dict(n="03",titulo="Detecção de Incêndios IoT",curto="Incêndios IoT",ctx="Projeto Integrador II",
  desc="Monitoramento de temperatura e gases em ambientes industriais e recicladoras, com sensores de chama e de gás, para prevenção de focos de incêndio.",
  hw=["Arduino","MQ-135","MLX90614"],img="/_blob/2ed4a68b0720300c77aa98dd02766a70",alt="Montagem em protoboard com módulos de sensores de gás e temperatura ligados a um Arduino UNO conectado ao notebook",sw=["C/C++","IoT"],dest=None,
  apr="Prevenção e monitoramento automatizado de focos de incêndio."),
 dict(n="04",titulo="Balança Digital com Arduino",curto="Balança",ctx="Projeto Integrador, 1º período",
  desc="Balança digital funcional que aplica a Lei de Hooke e conceitos de física, automação e programação.",
  hw=["Arduino UNO","HC-SR04","Display LCD 16x2"],img="/_blob/4d13a81d802c92c9e676fad8afc1943b",alt="Balança em caixa de acrílico com molas, com um peso metálico sobre a plataforma e o display LCD marcando Peso KG 4.494",sw=["C/C++"],dest=None,
  apr="Integração de hardware e software, controle de medições e cálculos físicos automatizados."),
]
GAL={
 "Drone":[("/_blob/9a6935ebf9621170701246c87ad79b1d","Placa do drone vista por uma lupa, sobre um suporte com garras","Placa, fornecida pelo professor"),
          ("/_blob/11e83af2be48600ddf4f84fdca0eec12","Placa do drone na mão, com as trilhas de cobre aparentes","Trilhas da placa")],
 "Carrinho":[("/_blob/7f0c1b31e201857f4fca7ccf48eea844","Carrinho visto de frente, com o nome Macarena Racing na carenagem","Vista de frente"),
             ("/_blob/5487a8a01f8d0407411dadf3a5094259","Modelo 3D do chassi com dois motores, rodas e placas eletrônicas","Modelo 3D do chassi")],
 "Incêndios IoT":[("/_blob/4c77c9841d42cd0821696eb4c0f08fc5","Tela da IDE do Arduino com o monitor serial mostrando leitura do sensor e a mensagem Gás tóxico detectado","Monitor serial")],
 "Balança":[("/_blob/6e1662ccb9b9853fd00dc863e160df4a","Mão pressionando a plataforma da balança, com o display ligado","Teste na plataforma")],
}
P=[dict({'img':None,'alt':''},**p) for p in P0]
for p in P: p['gal']=[{'img':a,'alt':b,'leg':c} for a,b,c in GAL.get(p['curto'],[])]
def thumbs(p, borda, legcss):
    if not p['gal']: return ''
    n=len(p['gal'])
    itens=''.join(f'<figure style="margin: 0; display: flex; flex-direction: column; gap: 4px"><img src="{g["img"]}" alt="{g["alt"]}" style="display: block; width: 100%; aspect-ratio: 1 / 1; object-fit: cover; border: {borda}"><figcaption style="{legcss}">{g["leg"]}</figcaption></figure>' for g in p['gal'])
    return f'<div style="display: grid; grid-template-columns: repeat({max(n,2)}, minmax(0, 1fr)); gap: 8px">{itens}</div>'
INTRO="Projetos de sistemas embarcados, IoT e automação desenvolvidos na graduação em Engenharia da Computação, na FAESA."
PESSOAIS="Em desenvolvimento."
GRAO='<svg aria-hidden="true" style="position: absolute; inset: 0; width: 100%%; height: 100%%; opacity: %s; mix-blend-mode: %s; pointer-events: none"><filter id="%s"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"></feTurbulence><feColorMatrix type="saturate" values="0"></feColorMatrix></filter><rect width="100%%" height="100%%" filter="url(#%s)"></rect></svg>'
def grao(op,mode,id): return GRAO%(op,mode,id,id)
def page(title,fonts,style,body,h,script=None,props=None):
    import json
    pr={"$preview":{"width":1440,"height":h}}
    if props: pr.update(props)
    script = script or "class Component extends DCLogic {\nrenderVals() {\nreturn {};\n}\n}"
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&amp;display=swap">
<style>
{style}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{json.dumps(pr)}'>
{script}
</script>
</body>
</html>
'''
