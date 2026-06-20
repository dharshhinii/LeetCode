class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums)
        l=[]
        for  i in sorted(a,reverse=True,key=a.get):
            if k!=0:
                l.append(i)
                k-=1
        return l