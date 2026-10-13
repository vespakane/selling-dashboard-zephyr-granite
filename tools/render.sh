#!/bin/zsh
# usage: render.sh <scroll> <outname>
mkdir -p "$(dirname "$0")/render"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --window-size=402,874 --force-device-scale-factor=3 --virtual-time-budget=3000 \
  --screenshot="$(dirname "$0")/render/$2.png" \
  "file://$(cd "$(dirname "$0")/.." && pwd | sed "s/ /%20/g")/index.html?scroll=$1" 2>/dev/null
