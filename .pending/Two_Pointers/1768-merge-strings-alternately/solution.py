class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=max(len(word1),len(word2))
        n=0
        p=0
        r=""
        for i in range(m):
            if i<len(word1):
                r=r+word1[n]
                n+=1
            if i<len(word2):
               r=r+word2[p]
               p+=1
        return r