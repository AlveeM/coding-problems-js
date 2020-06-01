class StockSpanner:

    def __init__(self):
        self.spans = []
        self.prices = []

    def next(self, price: int) -> int:
        idx = len(self.prices) - 1
        while idx >= 0 and self.prices[idx] <= price:
            span = self.spans[idx]
            idx = idx - span

        self.prices.append(price)
        span = len(self.prices) - 1 - idx
        self.spans.append(span)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)