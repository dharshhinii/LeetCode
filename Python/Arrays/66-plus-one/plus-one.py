class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        for i in digits:
           n=n*10+i
        n+=1
        r=[]
        while n>0:
         d=n%10
         r.insert(0,d)
         n=n//10
        return r
