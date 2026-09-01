import math
import heapq

class Solution:

    def euclid_dist(self, point: List[int]) -> int:
        x, y = point
        return math.sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_with_dist = [(self.euclid_dist(p), p) for p in points]
        result = heapq.nsmallest(k, points_with_dist)
        return [p[1] for p in result]