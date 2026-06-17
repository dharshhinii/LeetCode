class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        a=[]
        j=len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
               a.append(i+1)
               a.append(j+1)
               return a
            elif numbers[j]+numbers[i]>target:
                j-=1
            else:
                i+=1
                