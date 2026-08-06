class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            if len(str(i))%2==0:
                s+=1
        return s