class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=Counter(s)
        for i,j in a.items():
            if j==1:
                return s.index(i)

        return -1        