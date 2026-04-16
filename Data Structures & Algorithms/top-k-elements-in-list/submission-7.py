class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1+count.get(n,0)
        arr = []
        for key,value in count.items():
            arr.append([value,key])
        arr.sort()
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
        