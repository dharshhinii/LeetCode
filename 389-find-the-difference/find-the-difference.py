class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
            a=Counter(s)
            b=Counter(t)
            r=""
            for i,j in b.items():
                if i not in a:
                    r=i
                if j!=a[i]:
                    r=i
            return r