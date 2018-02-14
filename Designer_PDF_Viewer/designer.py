#!/bin/python
import sys
h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()
height = 0
l = len(word)
for a in word:
    if h[ord(a)-97]>height:
        height = h[ord(a)-97]
area = l*height
print area
