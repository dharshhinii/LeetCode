class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=[]
        for i in s:
            a.append(s.index(i))
        b=[]
        for j in t:
            b.append(t.index(j))
        return a==b