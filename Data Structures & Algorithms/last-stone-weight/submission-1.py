class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            first_heaviest = stones.pop()
            second_heaviest = stones.pop()
            if first_heaviest != second_heaviest:
                stones.append(first_heaviest-second_heaviest)
        if stones:
            return stones[0]
        return 0