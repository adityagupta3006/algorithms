#!/bin/python
import sys
# function checks whether the alternate character pattern.
def chk(st, m, n):
    for a in range(len(st)-1):
        if st[a] == st[a+1]:
            return 0
    return len(st)


s_len = int(raw_input().strip())
s = raw_input().strip()
arr = []
max_len = 0
# array with disctinct characters
for a in range(s_len):
    if s[a] not in arr:
        arr.append(s[a])
        
for a in range(len(arr)-1):
    for b in range(a+1, len(arr)):
        cpy = [c for c in s if c==arr[a] or c==arr[b]] #made a substring
        chk_len = chk(cpy, a, b)
        if chk_len>max_len:
            max_len = chk_len
print max_len
