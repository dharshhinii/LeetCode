class Solution:
    def maxArea(self, height: List[int]) -> int:
        c=0
        i=0
        j=len(height)-1
        while i<j:
            m=min(height[i],height[j])*abs(j-i)
            print(m)
            if c<m:
                c=m
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return c
