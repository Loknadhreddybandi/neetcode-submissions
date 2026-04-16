class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [0] * len(target)
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                result[0] = max(result[0], t[0])
                result[1] = max(result[1], t[1])
                result[2] = max(result[2], t[2])
        
        if result == target:
            return True
        return False
        