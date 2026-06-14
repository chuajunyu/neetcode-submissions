class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we only need to keep track of a monotonically decreasing set of elements
        # rationale: if a larger element enters the set, there is no need to keep the smaller elements before it in the window
        
        if len(nums) <= k:
            return [max(nums)]

        result = []
        window = []
        # build the initial list
        for i in range(k):
            n = nums[i]
            while window and window[-1][0] <= n:
                window.pop()
            window.append((n, i))
        
        result.append(window[0][0])
        

        # iterate while popping
        for i in range(k, len(nums)):
            
            n = nums[i]
            while window and window[0][1] <= i - k:
                window.pop(0)

            while window and window[-1][0] <= n:
                window.pop()
            window.append((n, i))
            result.append(window[0][0])
        
        return result
        