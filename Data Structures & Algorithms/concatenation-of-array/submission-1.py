class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        con = []
        for i in range(2):
            for num in nums:
                con.append(num)
        return con