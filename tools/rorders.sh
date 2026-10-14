#!/bin/zsh
# usage: rorders.sh <scroll> <outname> [set]   — renders the orders screen with tools/fixture.js
mkdir -p "$(dirname "$0")/render"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --window-size=402,874 --force-device-scale-factor=3 --virtual-time-budget=3000 \
  --screenshot="$(dirname "$0")/render/$2.png" \
  "file://$(cd "$(dirname "$0")/.." && pwd | sed "s/ /%20/g")/index.html?view=orders&fixture=tools/fixture.js&scroll=$1${3:+&set=$3}" 2>/dev/null
