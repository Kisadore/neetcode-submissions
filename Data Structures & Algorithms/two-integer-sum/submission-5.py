class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            lookFor = target - nums[i]
            if lookFor in map:
                return [map[lookFor], i]
            map[nums[i]] = i