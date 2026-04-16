class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1+count.get(n,0)
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        res = []
        for item in sorted_count[0:k]:
            res.append(item[0])
        return res
        