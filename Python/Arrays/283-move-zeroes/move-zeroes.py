class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                c.append(nums[i])
                nums[i]=0
        for i in range(len(c)):
            nums[i]=c[i]