class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        candidates.sort()
        ans=[]
        l=[]
        v=[0]*n
        cs=0
        def f(i,cs,v):
            if i>n:
                return 
            if cs==target:
                ans.append(l[:])
                return 
            if i==n or cs>target:
                return 
            v[i]=1
            l.append(candidates[i])
            f(i+1,cs+candidates[i],v)
            v[i]=0
            l.pop()
            while i+1<n and  candidates[i]==candidates[i+1]:
                i+=1
            f(i+1,cs,v)
            return
        f(0,cs,v)
        return ans