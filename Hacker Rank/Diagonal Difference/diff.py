import sys
def diff(r, c):
    sum = 0
    for i in range(r):
        sum += c[i][i] - c[i][r-i-1]
    return abs(sum)
    
n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
print diff(n, a)
