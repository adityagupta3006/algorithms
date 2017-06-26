class Solution(object):
    def isValid(self, s):
        l = len(s)
        if l == 0:
            return True
        
        if l%2 != 0:
            return False
        
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        return len(s)==0
