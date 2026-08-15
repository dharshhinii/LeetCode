class Solution:
    def smallestPalindrome(self, s: str) -> str:
        f=Counter(s)
        lf=""
        mid=""
        for i  in sorted(f):
            
            lf=lf+(i*(f[i]//2))
            if f[i]%2==1:
                mid=i
        return lf+mid+lf[::-1]

            

    