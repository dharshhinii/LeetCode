class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s=str(n)
        ss=0
        ds=0
        for i in s:
           ss+=int(i)*int(i)
           ds+=int(i)
        return (ss-ds)>=50