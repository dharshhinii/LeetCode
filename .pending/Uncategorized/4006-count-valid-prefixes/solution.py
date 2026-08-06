class Solution:
    def countValidPrefixes(self, s: str) -> int:
        z=c=0
        for i in s:
            if i=="0":
                z+=1
            else:
                z-=1
            if -1<=z<=1:
                c+=1
        return c