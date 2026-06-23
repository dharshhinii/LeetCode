class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      n=Counter(nums1)
      m=Counter(nums2)
      l=[]
      for i,j in n.items():
        if i  in m:
            if j==m[i]:
              for ij in range(j):
                l.append(i)
            else:
                d=min(j,m[i])
                for o in range(d):
                    l.append(i)
      return l