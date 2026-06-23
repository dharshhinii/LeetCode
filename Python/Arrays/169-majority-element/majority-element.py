class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        u=set(nums)
        p=0
        for i in u:
                if nums.count(i)>p:
                    k=i
                    p=nums.count(i)
        return k