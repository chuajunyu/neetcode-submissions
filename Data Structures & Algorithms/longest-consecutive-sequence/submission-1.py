class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        t = {i:i for i in nums}
        count = {}
        for i in t:
            if i in count:
                continue
            
            count[i] = 1
            tmp = i + 1
            while tmp in t:
                count[i] += 1
                count[tmp] = 1
                tmp += 1
            
            tmp = i - 1
            while tmp in t:
                count[i] += 1
                count[tmp] = 1
                tmp -= 1

        return max(count.values())

