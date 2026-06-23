class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i=j=0
        c=0
        while i<len(s) and j<len(g):
            if s[i]>=g[j]:
                c+=1
                i+=1
                j+=1
            else:
                i+=1
        return c