class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=[]
        c=0
        v="aeiou"
        for i in range(k):
            l.append(s[i])
            if s[i] in v:
                c+=1
        if c==k:
           return c
        m=c
        for i in range(len(s)-k):
            l.append(s[i+k])
            if s[i+k] in v:
                c+=1
            if l[0] in v:
                c-=1
            l.remove(l[0])
            m=max(c,m)
        return m
        