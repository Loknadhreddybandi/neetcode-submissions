class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for item in sorted_count[0:k]:
            res.append(item[0])
        return res
        