#!/usr/bin/env python3
"""Builds the standalone (GitHub Pages / iPad home screen) copy of Best Tree Friends
from talking-tree/index.html (the claude.ai artifact source).
Run from anywhere after every change to talking-tree/index.html:
    python3 talking-tree/build-ipad.py      -> writes index.html at the repo root (the live Pages site)"""
import os,re
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,"index.html"),encoding="utf-8").read()
src=re.sub(r"the weather \w+ sees outside","the weather you see outside",src)   # keep the kid's name out of the public page
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Tree Friends">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#eaf8ff">
<meta name="format-detection" content="telephone=no">
<link rel="apple-touch-icon" href="icon.png">
<link rel="icon" href="icon.png">
<link rel="manifest" href="manifest.json">
'''
# everything up to and including </style> belongs in <head>; the rest is the body
i=src.index("</style>")+len("</style>")
extra='''<style>
/* standalone app: keep clear of the iPad's rounded corners and home bar */
body{padding:max(16px,env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) max(16px,env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));margin:0;-webkit-text-size-adjust:100%}
*{box-sizing:border-box}
</style>
'''
out=head+src[:i]+"\n"+extra+"</head>\n<body>"+src[i:]+"\n</body>\n</html>\n"
dest=os.path.join(here,"..","index.html")
open(dest,"w",encoding="utf-8").write(out)
print("wrote",os.path.normpath(dest),len(out))
