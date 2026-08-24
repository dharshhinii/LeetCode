class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       r=ll=0
       m=0
       l=[]
       while r<len(s):
         while s[r] in l:
                l.remove(s[ll])
                ll+=1
         l.append(s[r])
         ss=len(l)
         m=max(m,ss)
         r+=1
       return m