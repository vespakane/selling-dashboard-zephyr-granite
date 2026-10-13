import sys
from measure import *
SH=__import__('os').path.join(__import__('os').path.dirname(__file__),'..','screenshots')+'/'
white=lambda c:c==(255,255,255)
lblue=lambda c:c==(0xf5,0xf8,0xfe)
sets={
'01':[
 ('cart circle',(330,55,402,118),notwhite),('cart icon',(330,55,402,118),dark),
 ('Selling title',(10,60,120,110),dark),
 ('grey band',(100,100,300,420),grey),
 ('YTD label',(10,150,150,185),dark),('info icon',(145,150,180,185),dark),
 ('£291',(10,180,120,235),dark),
 ('stat card1 white',(10,240,120,340),white),
 ('ACTIVE',(30,255,70,282),dark),('stat 4',(30,282,70,312),dark),
 ('ORDERS',(130,255,200,282),dark),('INACTIVE',(230,255,300,282),dark),
 ('Tasks title',(10,395,120,435),dark),
 ('task row1',(100,430,300,508),grey),('task row2',(100,508,300,590),grey),
 ('Buyer text',(30,455,200,495),dark),('badge',(320,445,380,500),red),
 ('count 1',(330,525,375,565),dark),
 ('Payments',(10,615,120,655),dark),
 ('wallet circle',(12,660,60,720),lambda c: c==(0xf7,0xf7,0xf7)),('wallet icon',(10,660,64,720),dark),
 ('Your total funds',(60,668,250,689),dark),('£235',(60,690,250,715),dark),('chevron',(360,670,395,715),dark),
 ('blue btn',(10,715,395,790),blue),('List text',(140,735,280,768),bright),
 ('home icon',(45,795,85,830),dark),('Home label',(45,826,85,846),dark),
 ('account badge',(120,790,170,815),red),('selling icon',(310,795,370,830),dark),('Selling label',(310,826,370,846),dark),
 ('selected pill',(290,785,402,870),lambda c: 0xe0<=c[0]<=0xee and abs(c[0]-c[2])<10),
],
'02':[
 ('Payments',(10,100,120,140),dark),('wallet circle',(12,150,60,210),grey),('Your total funds',(60,160,250,181),dark),('£235',(60,181,250,205),dark),('chevron',(360,160,395,205),dark),
 ('blue card',(0,230,402,420),lblue),('Find title',(30,262,372,292),dark),('See line1',(30,293,372,309),dark),('See line2',(30,309,372,330),dark),
 ('research box',(20,330,390,400),lgrey),('research icon',(40,345,76,385),dark),('research text',(78,345,230,385),dark),
 ('Sell title',(10,440,340,505),dark),('close circle',(340,436,402,482),notwhite),('close X',(340,436,402,482),dark),
 ('sub line1',(10,505,340,523),dark),('sub line2',(10,523,340,545),dark),
 ('cat card',(0,548,402,712),grey),('cat image',(18,556,146,700),lambda c: c!=(0xf7,0xf7,0xf7) and c!=(255,255,255)),
 ('trend icon',(144,568,166,592),green),('#1 text',(166,568,260,592),green),('CCG name',(144,590,330,610),dark),('5.7m',(144,610,330,626),dark),('£1.97',(144,626,330,646),dark),
 ('start btn',(140,648,300,700),blue),('start text',(182,655,290,695),blue),('start icon',(148,655,181,695),blue),
],
'03':[
 ('Sell title',(10,110,340,180),dark),('close circle',(340,105,402,150),notwhite),
 ('sub line1',(10,175,340,194),dark),('sub line2',(10,194,340,215),dark),
 ('card1',(0,220,402,372),grey),('card2',(0,372,402,526),grey),('card3',(0,526,402,680),grey),
 ('img1',(18,224,146,370),lambda c: c!=(0xf7,0xf7,0xf7) and c!=(255,255,255)),('img2',(18,378,146,524),lambda c: c!=(0xf7,0xf7,0xf7) and c!=(255,255,255)),('img3',(18,530,146,678),lambda c: c!=(0xf7,0xf7,0xf7) and c!=(255,255,255)),
 ('#2 text',(166,390,260,412),green),('Wrist name',(144,412,330,432),dark),('3.7m',(144,432,330,448),dark),('£210',(144,448,330,468),dark),('start2',(140,470,300,520),blue),
 ('#3 text',(166,544,260,566),green),('Dresses',(144,566,330,586),dark),('start3',(140,624,300,674),blue),
 ('show more',(0,690,402,740),lgrey),('show more text',(140,700,240,740),dark),
],
'04':[
 ('show more',(0,125,402,195),lgrey),('show more text',(140,140,240,180),dark),('show chevron',(240,140,270,180),dark),
 ('Selling tools',(10,225,200,262),dark),
 ('tool1 circle',(10,265,70,330),grey),('tool1 icon',(10,265,70,330),dark),('tool2 circle',(80,265,150,330),grey),('tool3 circle',(170,265,250,330),grey),('tool4 circle',(270,265,350,330),grey),('tool5 circle',(360,265,402,330),grey),
 ('Offers',(10,325,70,352),dark),('Bundles',(80,325,150,352),dark),('Performance',(160,325,260,352),dark),('Research',(270,325,350,352),dark),
 ('Selling details',(10,385,200,425),dark),
 ('Feedback label',(10,440,200,465),dark),('fb icons',(10,465,150,492),dark),('fb chevron',(360,440,395,495),dark),
 ('Remaining label',(10,505,200,531),dark),('£377',(10,531,250,558),dark),('lim chevron',(360,505,395,560),dark),
 ('tell card',(0,600,402,690),grey),('tell icon',(100,620,142,665),dark),('tell text',(142,620,300,665),dark),
],
}
sets['05']=[(n,(b[0],b[1]-6,b[2],b[3]-6),p) for n,b,p in sets['04']]
for k in sys.argv[1:]:
    print('=== screen',k)
    run(sets[k], SH+k+'.png', __import__('os').path.join(__import__('os').path.dirname(__file__),'render',f'r{k}.png'))
