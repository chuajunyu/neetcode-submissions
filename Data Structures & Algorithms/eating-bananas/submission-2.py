class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # what is the thing we want to binary search? -> eating rate k
        # how to test each k -> write a test function

        def test_k(k):
            # loop through the pile, calculate how many hours to go through that pile
            count = 0
            for p in piles:
                count += p // k
                if p % k:
                    count += 1
            return count <= h

        # what's the maximum and minimum?
        # max k is the MAXIMUM pile size
        right = max(piles)

        # min k is the sum of pile size / h?
        left = sum(piles) // h or 1

        best = None
        while left <= right:
            middle = (left + right) // 2

            if test_k(middle):
                best = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return best