class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bal = {}
        for i in range(len(nums)):
            n = nums[i]
            if target - n in bal:
                return [bal[target - n], i]
            else:
                bal[n] = i
        


        