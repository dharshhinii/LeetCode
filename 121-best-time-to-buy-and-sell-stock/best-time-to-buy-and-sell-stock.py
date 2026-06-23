class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        p=0
        for i in prices:
            m=min(i,m)
            p=max(p,i-m)
        return p