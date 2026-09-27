class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=0
        for i in range(k):
           s+=arr[i]
        t=0
        if s/k >=threshold:
            t+=1
        for i in range(len(arr)-k):
            s=s-arr[i]+arr[i+k]
            if s/k >=threshold:
                t+=1
        return t