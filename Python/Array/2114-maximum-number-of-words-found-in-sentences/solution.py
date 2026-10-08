class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        p=0
        for s in sentences:
            p=max(p,len(s.split()))
        return p