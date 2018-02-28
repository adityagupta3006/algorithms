a,b,n = raw_input().split()
for m in range(int(n)-2):
    s = int(a) + pow(int(b),2)
    a = int(b)
    b = s
print s
