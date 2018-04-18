import sys

def powerSum(X, N):
    return powerSumRec(X, N, 1)

def powerSumRec(X, N, num):
    rem = X - num**N
    if rem<0:
        return 0
    elif rem == 0:
        return 1
    else:
        return powerSumRec(rem, N, num+1) + powerSumRec(X, N, num+1)  
        

if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    result = powerSum(X, N)
    print(result)
