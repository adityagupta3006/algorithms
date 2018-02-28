def game(k):
    a = (k)%7
    if a in [0,1]:
        return 'Second'
    else:
        return 'First'
    
n = int(raw_input())
for a in range(n):
    m = int(raw_input())
    print game(m)
