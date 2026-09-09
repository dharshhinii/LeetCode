class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        r=l=0
        m=c=0
        ll=[]
        while r<len(fruits):
          
            if fruits[r] not in ll:
                    c+=1
            ll.append(fruits[r])
                 
            while c>2:
                k=ll[0]
                ll.remove(k)
                if k not in ll:
                    c-=1
                l+=1
            s=len(ll)
            m=max(m,s)


            r+=1
        return m
            
