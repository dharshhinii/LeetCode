class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        r=0
        n=len(nums)
        m=0
        for i in range(n):
            m1=nums[i]
            for j  in range(i+1,n):
                m2=nums[j]
                r=math.gcd(m1,m2)
                m=max(m,(m1*m2)//(r*r))
        return  m