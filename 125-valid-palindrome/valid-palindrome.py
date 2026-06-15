class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        for i in s:
            if i.isalnum():
                r=r+i
        return r[::-1].lower()==r.lower()