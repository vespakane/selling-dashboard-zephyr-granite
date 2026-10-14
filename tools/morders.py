# Orders screen: compare tools/render/o06.png (rorders.sh 0 o06) and o07.png (rorders.sh 47.33 o07 07)
# against screenshots/06.png and 07.png. Same d(x,y,w,h) read-out as mall.py.
import sys, os
from measure import *
SH = os.path.join(os.path.dirname(__file__), '..', 'screenshots') + '/'
sets = {
'06': [
 ('back circle',(8,52,72,118),notwhite),('back chev',(8,52,72,118),dark),('title',(65,65,160,100),dark),
 ('dots circle',(278,52,336,118),notwhite),('dots',(278,52,336,118),dark),('cart circle',(336,52,398,118),notwhite),('cart',(336,52,398,118),dark),
 ('Active',(10,135,75,165),dark),('Orders',(95,135,160,159),dark),('underline',(95,159,160,175),dark),('Inactive',(185,135,255,165),dark),('Drafts',(280,135,345,165),dark),('Sche',(365,135,402,165),dark),
 ('search circle',(10,168,54,206),notwhite),('search icon',(10,168,54,206),dark),
 ('actions pill',(50,166,160,210),notwhite),('Actions text',(65,178,118,205),dark),('actions chev',(118,178,150,205),dark),
 ('refine pill',(290,166,395,210),notwhite),('refine icon',(300,178,330,205),dark),('Refine text',(330,178,385,205),dark),
 ('All chip',(10,212,91,257),notwhite),('All text',(20,222,85,248),dark),('Post chip',(91,212,204,257),notwhite),('Post text',(105,222,195,248),dark),
 ('Await chip',(203,212,402,257),notwhite),('Await text',(215,222,402,248),dark),
 ('banner',(10,280,395,345),grey),('banner red',(25,295,55,335),red),('Post by text',(55,300,250,330),dark),('banner chev',(350,300,385,330),dark),
 ('img box',(10,350,145,490),notwhite),('rm badge',(15,352,40,380),red),
 ('Buyer paid',(145,358,228,385),dark),('van circle',(228,350,275,392),notwhite),('van icon',(228,350,275,392),dark),
 ('title1',(145,390,395,407),dark),('title2',(145,407,395,428),dark),('tag',(145,428,345,452),notwhite),('tag text',(150,431,340,450),dark),
 ('price',(145,455,196,472),dark),('Subtotal',(196,455,260,472),dark),
 ('postage',(145,473,380,489),dark),('Sold',(145,489,260,501),dark),('Buyer paid line',(145,502,260,517),dark),('Buyer line',(145,517,280,532),dark),
 ('info',(10,533,40,556),blue),('Funds text',(40,533,150,556),dark),('divider',(100,575,300,600),notwhite),('banner2',(10,610,395,670),grey),
 ('img box2',(10,675,145,805),notwhite),('Buyer paid2',(145,683,228,710),dark),('title1b',(145,715,395,733),dark),('title2b',(145,733,395,752),dark),('Quantity',(145,752,260,770),dark),
],
'07': [
 ('banner',(10,235,395,300),grey),('img box',(10,303,145,440),notwhite),('Buyer paid',(145,312,228,340),dark),('van circle',(228,303,275,345),notwhite),
 ('title1',(145,343,395,360),dark),('title2',(145,360,395,380),dark),('Quantity',(145,380,260,398),dark),('tag',(145,398,345,423),notwhite),('tag text',(150,401,340,421),dark),
 ('price',(145,425,215.5,443),dark),('Subtotal',(215.5,425,270,443),dark),
 ('postage',(145,444,380,459),dark),('Sold',(145,459,260,472),dark),('Buyer paid line',(145,473,260,488),dark),('Buyer line',(145,488,280,503),dark),
 ('info',(10,503,40,526),blue),('Funds text',(40,503,150,526),dark),('divider',(100,545,300,570),notwhite),('banner2',(10,580,395,640),grey),
 ('img box2',(10,645,145,775),notwhite),('Buyer paid2',(145,655,228,681),dark),('title1b',(145,685,395,703),dark),('title2b',(145,703,395,723),dark),('Colour',(145,723,260,740),dark),('tag2',(145,740,345,765),notwhite),
],
}
for k in sys.argv[1:]:
    print('=== screen', k)
    run(sets[k], SH + k + '.png', os.path.join(os.path.dirname(__file__), 'render', 'o' + k + '.png'))
