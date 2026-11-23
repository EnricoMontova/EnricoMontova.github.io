import math, random
def star(cx,cy,r,ri=None,color="#E8E6E1"):
    ri = ri or r*0.12
    pts=[]
    for i in range(8):
        a=math.pi/2*i/2 - math.pi/2
        rr = r if i%2==0 else ri
        pts.append(f"{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}")
    # curved concave star via quadratic segments
    d=""
    outer=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
    d=f"M{outer[0][0]:.1f},{outer[0][1]:.1f}"
    for k in range(4):
        x2,y2=outer[(k+1)%4]
        d+=f" Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}"
    return f'<path d="{d} Z" fill="{color}"></path>'
def particles(cx,cy,r0,r1,n,seed,color,a0=-60,a1=120):
    rnd=random.Random(seed); out=[]
    for _ in range(n):
        a=math.radians(rnd.uniform(a0,a1)); rr=rnd.uniform(r0,r1)
        x=cx+rr*math.cos(a); y=cy+rr*math.sin(a); s=rnd.choice([1,1,1.5,2,2.5])
        op=max(0.15,1-(rr-r0)/(r1-r0))
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{s}" height="{s}" fill="{color}" opacity="{op:.2f}"></rect>')
    return "".join(out)
def globe(cx,cy,r,color,sw=1,tilt=0.0):
    o=[f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{sw}"></circle>']
    for k in range(1,6):
        rx=r*abs(math.cos(math.pi*k/12)); o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx:.1f}" ry="{r}" fill="none" stroke="{color}" stroke-width="{sw}"></ellipse>')
    o.append(f'<line x1="{cx}" y1="{cy-r}" x2="{cx}" y2="{cy+r}" stroke="{color}" stroke-width="{sw}"></line>')
    for k in range(-4,5):
        y=cy+r*math.sin(math.pi*k/10); w=r*math.cos(math.pi*k/10)
        o.append(f'<ellipse cx="{cx}" cy="{y:.1f}" rx="{w:.1f}" ry="{w*0.18:.1f}" fill="none" stroke="{color}" stroke-width="{sw}"></ellipse>')
    return "".join(o)
def mesh(w,h,color,cols=26,rows=16,dip=(0.5,0.55),depth=70):
    o=[]
    def pt(u,v):
        # perspective: rows closer at top
        y=h*0.08 + (h*0.9)*(v**1.35)
        spread=0.55+0.45*v
        x=w/2 + (u-0.5)*w*1.25*spread
        dx=u-dip[0]; dv=v-dip[1]; d=math.exp(-((dx*2.2)**2+(dv*2.6)**2)*3)
        return x, y + depth*d*(0.4+v)
    for j in range(rows+1):
        v=j/rows; o.append('<polyline fill="none" stroke="%s" stroke-width="0.8" points="%s"></polyline>'%(color," ".join("%.1f,%.1f"%pt(i/cols,v) for i in range(cols+1))))
    for i in range(cols+1):
        u=i/cols; o.append('<polyline fill="none" stroke="%s" stroke-width="0.8" points="%s"></polyline>'%(color," ".join("%.1f,%.1f"%pt(u,j/rows) for j in range(rows+1))))
    return "".join(o)
def barcode(text,h,color,unit=2):
    x=0;o=[]
    for ch in text:
        c=ord(ch)
        for b in range(6):
            w=unit*(1+((c>>b)&1))
            if b%2==0: o.append(f'<rect x="{x}" y="0" width="{w}" height="{h}" fill="{color}"></rect>')
            x+=w
    return x,"".join(o)
