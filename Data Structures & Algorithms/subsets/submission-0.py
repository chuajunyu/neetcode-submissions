class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # The classic pick one or not pick one approach
        # We want to avoid array concatenation
        final = []
        def helper(nums, index, result=[]):
            if index >= len(nums):
                final.append(result)
                return
            
            curr = nums[index]
            helper(nums, index+1, result)
            helper(nums, index+1, result + [curr])
        
        helper(nums, 0)
        return final

        