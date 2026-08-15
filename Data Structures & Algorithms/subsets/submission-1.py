class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # The classic pick one or not pick one approach
        # We want to avoid array concatenation
        final = []
        result = []
        def helper(index):
            if index >= len(nums):
                final.append(result.copy())
                return
            
            curr = nums[index]
            helper(index+1)
            result.append(curr)
            helper(index+1)
            result.pop()
        
        helper(0)
        return final

        