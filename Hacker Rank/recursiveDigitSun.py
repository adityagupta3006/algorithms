#!/bin/python3

import sys

def digitSum(n, k):
    n = int(n)*k
    return calc(str(n))

def calc(n):
    n = str(n)
    if len(n) == 1:
        return n
    sum = 0
    for i in n:
        sum = sum + int(i)
    return calc(str(sum))

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = digitSum(n, k)
    print(result)
