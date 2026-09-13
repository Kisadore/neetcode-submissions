class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currCount = 0
        max_num = 0
        for num in nums:
            if num == 1:
                currCount += 1
                max_num = max(max_num, currCount)
            else: currCount = 0
        return max_num