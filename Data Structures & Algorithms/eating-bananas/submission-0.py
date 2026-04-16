from math import ceil
from typing import List

class Solution:
    def maximum(self, piles: List[int]) -> int:
        
        maxi = float('-inf')
        for pile in piles:
            maxi = max(pile, maxi)
        return maxi

    def TotalHours(self, piles: List[int], speed: int) -> int:
        
        total_hours = 0
        for pile in piles:
            total_hours += ceil(pile / speed)
        return total_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = self.maximum(piles)  # Maximum bananas in a single pile
        while low <= high:
            mid = (low + high) // 2  # Midpoint of the current range
            total_hours = self.TotalHours(piles, mid)  # Total hours needed at speed mid
            
            if total_hours <= h:
                high = mid - 1  
            else:
                low = mid + 1  
                
        return low  
