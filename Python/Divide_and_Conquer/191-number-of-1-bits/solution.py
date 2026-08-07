class Solution:
    def hammingWeight(self, n: int) -> int:
        c=bin(n)[2::].count('1')
        return c