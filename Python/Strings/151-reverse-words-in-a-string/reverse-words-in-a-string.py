class Solution:
    def reverseWords(self, s: str) -> str:
        d=s.split()
        return " ".join(d[::-1])