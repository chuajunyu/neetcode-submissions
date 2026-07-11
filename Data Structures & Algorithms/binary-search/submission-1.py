class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Invariant: target is always within left and right (inclusive)

        left, right = 0, len(nums)
        while left <= right and left < len(nums) and right >= 0:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
            
        return -1