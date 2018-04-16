# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from datetime import datetime
import time

def solution(S):
    minutes = int(S[3:5])
    hours = int(S[0:2])
    h_max = 23
    min_max = 59
    
    time = ("".join(S.split(":")))
    d = (sorted(time))
    
    while(True):
        if minutes<min_max:
            minutes += 1
        else:
            minutes = 0
            if hours<h_max:
                hours += 1
            else:
                hours = 0
        
        m = str(minutes)
        h = str(hours)
        
        time = h+m
        l = len(time)
        temp = time
        
        if l<4:
            temp = temp + '0'*(4-l)

    
        if d == sorted(temp):
            if len(h) == 1:
                h = '0' + h
            if len(m) == 1:
                m = '0' + m
            return (h + ":" + m)