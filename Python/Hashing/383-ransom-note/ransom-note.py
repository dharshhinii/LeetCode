class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      r=Counter(ransomNote)
      s=Counter(magazine)
      for i,j in r.items():
         if s[i]<j:
            return False
      return True