class Solution:
    def reverseWords(self, s: str) -> str:
        d=s.split()
        r=""
        for i in d:
            r=r+i[::-1]+" "
        return r.strip()