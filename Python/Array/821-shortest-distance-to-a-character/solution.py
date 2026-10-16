class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ss=[]
        for i in range(len(s)):
            if c==s[i]:
                ss.append(i)
        a=[]
        for i in range(len(s)):
            m=[]
            for j in ss:
               m.append(abs(i-j))
            a.append(min(m))
        return a