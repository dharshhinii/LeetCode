class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        while i<j:
            if s[i].isalpha():
                if s[j].isalpha():
                    s[i],s[j]=s[j],s[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        r=""
        for i in s:
            r=r+i
        return r