num, times = raw_input().split()
length = len(num)
def superDigit(l,n,k):
    total = 0
    for a in range(l):
        total = total + int(n[a])
    n = str(total * int(k))
    return n
while len(num)>1:
    num = superDigit(length,num,times)
    times = 1
    length = len(num)
print num
