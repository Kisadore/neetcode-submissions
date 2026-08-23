class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) == 0:
        #     return False
        # mySet = set()
        # mySet.add(nums[0])
        # for i in range(1, len(nums)):
        #     if nums[i] in mySet:
        #         return True
        #     mySet.add(nums[i])
        # return False

        unique = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False