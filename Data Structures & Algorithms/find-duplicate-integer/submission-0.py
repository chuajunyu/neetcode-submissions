class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. Sort then loop through and find
        # 2. Quick select
        # 3. Cuckoo sort

        array = [0] * len(nums)
        for n in nums:
            if array[n - 1]:
                return n
            else:
                array[n - 1] = n


        