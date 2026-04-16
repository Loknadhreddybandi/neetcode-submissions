import bisect
class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
        

    def findMedian(self) -> float:
        n = len(self.nums)
        if n%2==1:
            return float(self.nums[n//2])
        else:
             return (self.nums[(n - 1) // 2] + self.nums[n // 2]) / 2.0
        
        