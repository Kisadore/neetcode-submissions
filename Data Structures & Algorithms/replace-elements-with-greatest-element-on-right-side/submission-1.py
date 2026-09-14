class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                return arr
            maxVal = float('-inf')
            for j in range(i + 1, len(arr)):
                maxVal = max(maxVal, arr[j]) 
            arr[i] = maxVal
                           