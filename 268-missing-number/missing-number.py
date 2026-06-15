class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=len(nums)
        es=(m*(m+1))//2
        s=sum(nums)
        return es-s