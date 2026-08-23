class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        print(map)

        res = []
        for item, freq in map.most_common(k):
            res.append(item)
        return res