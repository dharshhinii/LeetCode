class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       m=prices[0]
       p=0
       for i in prices:
        m=min(i,m)
        pp=i-m
        p=max(pp,p)
       return p