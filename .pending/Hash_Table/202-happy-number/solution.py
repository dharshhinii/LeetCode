class Solution:
    def isHappy(self, n: int) -> bool:
        def f(n):
            s=0
            while n>0:
                s+=(n%10)*(n%10)
                n//=10
            return s
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = f(n)

        return n == 1