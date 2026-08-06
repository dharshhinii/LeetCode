class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s=0
        for i in range(k):
            if blocks[i]=='W':
                s+=1
        m=s
        for i in range(len(blocks)-k):
            if blocks[i]=='W':
                s-=1
            if blocks[i+k]=='W':
                s+=1
            m=min(s,m)
        return m