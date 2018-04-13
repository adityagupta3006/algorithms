def rev(data):
    print data.strip().split()[::-1]

s = "the sky is blue"
rev(s)

'''class Solution(object):
    def reverseWords(self, data):
        if data.strip() == '':
            return ''
        s = []
        word = ''
        for i in data:
            if i == ' ':
                s.append(word)
                word = ''
                continue
            word = word + i
        s.append(word)
        l = len(s)
        for i in range(l/2):
            s[i], s[l-i-1] = s[l-i-1], s[i]
        a = ' '
        return a.join(s)'''