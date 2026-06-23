class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        l= ['a','e','i','o','u','A','E','I','O','U']
        while i<j:
            if s[i] not in l:
                i+=1
            if s[j] not in l:
                j-=1
            if s[i] in l and s[j] in l:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        r=""
        for i in s:
            r=r+i
        return r