import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1, s2 = -heapq.heappop(stones), -heapq.heappop(stones)
            if s1 == s2:
                continue
            else:
                new_stone = max(s1, s2) - min(s1, s2)
                heapq.heappush(stones, -new_stone)
        
        if stones:
            return -stones[0]
        else:
            return 0
