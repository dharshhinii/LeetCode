class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while  i<len(arr):
            if arr[i]==0:
                arr.insert(i+1,arr[i])
                arr.pop()
                i+=2
            else: 
                i+=1
        return