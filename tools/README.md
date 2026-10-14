# Pixel comparison tools

Renders `index.html` in headless Chrome at the iPhone's 402x874pt / 3x scale and
measures element positions against the screenshots in `../screenshots`.

    cd tools
    ./render.sh 0 r01; ./render.sh 509 r02; ./render.sh 840 r03; ./render.sh 1398 r04; ./render.sh 1404 r05
    python3 mall.py 01 02 03 04 05        # prints d(x,y,w,h) in points; <<< marks anything over 1pt

The number passed to render.sh is the scroll offset that lines the render up with each screenshot.

Orders screen (captures 06.png, 07.png; product crops for the fixture go in `render/`):

    ./rorders.sh 0 o06; ./rorders.sh 47.33 o07 07
    python3 morders.py 06 07
