class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # is the optimal solution O(n^2)
        nums.sort()
        result = []

        i = 0
        while i < len(nums):
            # solve 2 sum in nums[i:]
            x = nums[i]
            
            h = {}
            j = i + 1
            while j < len(nums):
                y = (nums[j])
                if -(x + y) in h:
                    triplet = [x, y, -(x + y)]
                    result.append(triplet)
                    h[y] = j
                    # increment j until it's a new element
                    j += 1
                    while j < len(nums) and nums[j] == y:
                        j += 1 
                else:
                    h[y] = j
                    j += 1

            n = i + 1
            while n < len(nums) and nums[n] == x:
                n += 1
            i = n
            

        return result    
