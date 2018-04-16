# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(flowers, k):
    # write your code in Python 3.6
    n = len(flowers)
    f = [0] * (n + 1)
    i = n+1
    for x in reversed(flowers):
        i -= 1
        if isValid(x, k, n, f): return i
    
    return -1
    
def isValid(x, k, n, f):
    f[x] = 1
    if x + k + 1 <= n and f[x + k + 1] == 1:
        valid = True
        for i in range(k):
            if f[x + i + 1] == 1: 
                valid = False
                break
        if valid: return True
    if x - k - 1 > 0 and f[x - k - 1] == 1:
        for i in range(k):
            if f[x - i - 1] == 1:
                return False
        return True
    return False