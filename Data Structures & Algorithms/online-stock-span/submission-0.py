class StockSpanner:

    def __init__(self):
        self.StockSpanner = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.StockSpanner and self.StockSpanner[-1][0]<=price:
            span += self.StockSpanner[-1][-1]
            self.StockSpanner.pop()
        
        self.StockSpanner.append((price,span))
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)