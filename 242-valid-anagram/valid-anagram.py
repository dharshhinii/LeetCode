class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i=list(s)
        n=list(t)
        i.sort()
        n.sort()
        return i==n
                  