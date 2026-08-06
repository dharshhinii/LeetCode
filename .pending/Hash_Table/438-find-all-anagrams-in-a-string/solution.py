class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        else:
            pp=Counter(p)
            l=len(p)
            ss=Counter(s[:l])
            h=[]
            if pp==ss:
               h.append(0)
            for i in range(len(s)-l):
                ss[s[i]]-=1
                if ss[s[i]]==0:
                    del ss[s[i]]
                ss[s[i+l]]+=1
                if ss==pp:
                    h.append(i+1)
            return h