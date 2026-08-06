class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        p=[0] * n
        s=[0] * n

        pv=sv= 0

        for i in range(n):
            p[i]=pv
            pv+=nums[i]

        for i in range(n-1,-1,-1):
            s[i]=sv
            sv+=nums[i]

        for i in range(n):
            if p[i]==s[i]:
                return i

        return -1