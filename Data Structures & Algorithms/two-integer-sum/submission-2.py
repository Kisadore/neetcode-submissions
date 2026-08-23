class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             ans.append(i)
        #             ans.append(j)
        #             return ans

         map ={}
         ans = []
         for i in range(len(nums)):
            if nums[i] in map:
                ans.append(map[nums[i]])
                ans.append(i)
                return ans
            diff = target - nums[i]
            map[diff] = i