class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        c=[]
        for i in accounts:
            c.append(sum(i))
        return max(c)