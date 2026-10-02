class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        d=[]
        l=[]
        v=[0]*n
        cs=0
        def f(i,cs,v):
            if i>n:
                return 
            if cs==target:
                d.append(l[:])
                return
            if i==n or cs>target:
                return
            v[i]=1
            l.append(candidates[i])
            f(i,cs+candidates[i],v)
            l.pop()
            v[i]=0
            f(i+1,cs,v)
            return
        f(0,cs,v)
        return d