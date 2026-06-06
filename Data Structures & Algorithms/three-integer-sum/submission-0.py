class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # is the optimal solution O(n^2)

        result = set()
        for i, x in enumerate(nums):
            # solve 2 sum in nums[i:]
            h = {}
            for j, y in enumerate(nums[i+1:]):
                if -(x + y) in h:
                    triplet = [x, y, -(x + y)]
                    triplet.sort()
                    result.add(tuple(triplet))
                h[y] = j
            

        return list(result)    
