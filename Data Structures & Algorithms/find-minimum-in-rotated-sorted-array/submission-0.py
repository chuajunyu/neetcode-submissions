class Solution:
    def findMin(self, nums: List[int]) -> int:
        # We know which section of the array we are on

        # is it monotonic?
        if nums[-1] > nums[0]:
            return nums[0]

        # Otherwise
        left, right = 0, len(nums) - 1
        while left < right and left < len(nums) and right >= 0:
            middle = (left + right) // 2
            value = nums[middle]

            if value > nums[-1]:
                # it's in the first part of the array
                left = middle + 1
            else:
                right = middle
        
        return nums[left]