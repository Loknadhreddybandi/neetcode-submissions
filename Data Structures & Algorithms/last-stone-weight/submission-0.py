class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            first = stones[-1]
            second = stones[-2]
            # so already sorted (first is always greater than second)
            stones.remove(first)
            stones.remove(second)
            if first>second:
                stones.append(first-second)
        #if stones length is 1 then this is answer else return 0
        if stones:
            return stones[0]
        else:
            return 0
        