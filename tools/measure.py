import sys
from PIL import Image
S=3
def bb(im, box_pt, pred):
    x0,y0,x1,y1=[int(v*S) for v in box_pt]
    xs=[];ys=[]
    for y in range(y0,min(y1,im.size[1])):
        for x in range(x0,min(x1,im.size[0])):
            if pred(im.getpixel((x,y))): xs.append(x); ys.append(y)
    if not xs: return None
    return (round(min(xs)/S,1), round(min(ys)/S,1), round((max(xs)-min(xs)+1)/S,1), round((max(ys)-min(ys)+1)/S,1))
dark=lambda c: sum(c)<360
bright=lambda c: sum(c)>700
notwhite=lambda c: c!=(255,255,255)
grey=lambda c: c==(0xf7,0xf7,0xf7)
blue=lambda c: c[2]>200 and c[0]<80
red=lambda c: c[0]>150 and c[1]<80
green=lambda c: c[1]>c[0]+20 and c[1]>c[2]+20
lgrey=lambda c: 0x80<c[0]<0xa0 and abs(c[0]-c[2])<6
def run(tests, A, B):
    a=Image.open(A).convert('RGB'); b=Image.open(B).convert('RGB')
    for name, box, pred in tests:
        ra=bb(a,box,pred); rb=bb(b,box,pred)
        if ra and rb:
            d=tuple(round(rb[i]-ra[i],1) for i in range(4))
            flag='' if max(abs(v) for v in d)<=1 else '  <<<'
            print(f'{name:26s} orig={ra}  mine={rb}  d(x,y,w,h)={d}{flag}')
        else: print(f'{name:26s} orig={ra} mine={rb}  MISSING')
