class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        else:
           s=Counter(s1)
           ss=Counter(s2[:len(s1)])
           l=len(s1)
           if s==ss:
             return True
           for i in range(len(s2)-l):
             ss[s2[i]]-=1
             if ss[s2[i]]==0:
                del ss[s2[i]]
             ss[s2[i+l]]+=1
             if s==ss:
                return True
           return False
          