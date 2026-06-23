class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d=list(pattern)
        f=[]
        for i in d:
            f.append(d.index(i))
        g=[]
        h=s.split()
        for i in h:
            g.append(h.index(i))
        return f==g