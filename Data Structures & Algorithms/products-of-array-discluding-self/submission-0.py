class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left product prefix sum
        left = [1]
        for n in nums:
            left.append(n * left[-1])

        right = [1]
        for n in reversed(nums):
            right.append(n * right[-1])

        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[len(nums) - i - 1])
        
        return result
        