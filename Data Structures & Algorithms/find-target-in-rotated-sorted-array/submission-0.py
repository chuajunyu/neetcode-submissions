class Solution:
    def search(self, nums: List[int], target: int) -> int:
        is_first_part = target > nums[-1]
        
        left, right = 0, len(nums) - 1
        while left <= right and left < len(nums) and right >= 0:
            middle = (left + right) // 2
            value = nums[middle]
            if value == target:
                return middle
            if value > nums[-1]:
                # we are in the first part of the array
                if not is_first_part or target > value:
                    left = middle + 1  # move to second part
                    continue
                else:
                    right = middle - 1
            else:
                # we are in the second part of the array
                if is_first_part or target < value:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1
        