# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPower(p):
    if p == 1:
        return True
    elif p%2 == 0:
        p = p/2
        return isPower(p)
    else:
        return False

def countNearest(c):
    ct = 0
    while c != 1:
        c = c/2
        ct = ct + 1
    return pow(2, ct)

def function(f):
    count = 1
    while f != 1:
        ans = isPower(f)
        if ans == False:
            f = f-countNearest(f)   
            count = count + 1
        else:
            f = f/2
            count = count + 1
    if count%2 != 0:
        return "Richard"
    else:
        return "Louise"
    
n = input()
for num in range(n):
    a = input()
    final = function(a)
    print final
