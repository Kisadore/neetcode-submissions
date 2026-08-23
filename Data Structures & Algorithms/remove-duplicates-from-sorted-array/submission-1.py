class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        length = len(nums)
        
        while right < length:
            nums[left] = nums[right]
            while right < length and nums[right] == nums[left]:
                right += 1
            left += 1
        return left

