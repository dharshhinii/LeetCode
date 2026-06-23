class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=[]
        i=0
        while i<len(nums):
            if nums[i] not in l:
                l.append(nums[i])
                i+=1
            else:
                nums.remove(nums[i])
    