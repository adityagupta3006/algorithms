def longestPalindrome(s):
    l = len(s)
    result = ""
    for i in range(l):
        result = max(findPermut(s, i, i), findPermut(s, i, i+1), result, key = len)
    return result

def findPermut(s, left, right):
    while left>=0 and right<len(s) and s[left] == s[right]:
        left -= 1; right += 1
    return s[left+1: right]

s = "babad"
print longestPalindrome(s)