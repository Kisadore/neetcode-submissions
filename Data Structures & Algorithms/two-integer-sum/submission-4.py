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
        #  ans = []
         
         for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                # ans.append(map[diff])
                # ans.append(i)
                # return ans
                return [map[diff], i]
            map[n] = i