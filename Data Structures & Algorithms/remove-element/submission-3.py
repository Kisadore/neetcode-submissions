class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0 , 0
        for j in range(len(nums)):
            if nums[i] == val:
                if nums[j] !=val:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    i += 1
            else:
                i += 1
        return i 









        