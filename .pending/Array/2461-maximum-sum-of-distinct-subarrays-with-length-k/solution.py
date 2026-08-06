class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l={}
        m=s=0
        for i in range(k):
          s+=nums[i]
          if nums[i] not in l:
            l[nums[i]]=1
          else:
            l[nums[i]]+=1
        if len(l)==k:
            m=s
        for i in range(len(nums)-k):
            l[nums[i]]-=1
            if l[nums[i]]==0:
                del l[nums[i]]
            if nums[i+k] not in l:
              l[nums[i+k]]=1
            else:
                l[nums[i+k]]+=1
            s=s-nums[i]+nums[i+k]
            if len(l)==k:
              if m<s:
                m=s
        return m