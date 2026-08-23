class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsToCheck = {}
        
        for i, num in enumerate(nums):
            if target - num in numsToCheck:
                return [numsToCheck[target - num], i]
            numsToCheck[num] = i
