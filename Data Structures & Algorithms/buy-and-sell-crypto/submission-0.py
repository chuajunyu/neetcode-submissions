class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # track cheapest price before this day
        cheap = prices[0]
        best = 0
        for p in prices[1:]:
            best = max(best, p - cheap)
            cheap = min(p, cheap)
        return best
