class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        f=[]
        for i in nums:
            f.append(i*i)
        
        f.sort()
        return f