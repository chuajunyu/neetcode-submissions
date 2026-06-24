class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # for each thing figure out the lowest thing from the right and from the left

        right_lower = [len(heights)] * len(heights)  # first index to the right that is LOWER
        stack = []
        for i, h in enumerate(heights):
            while stack and h < stack[-1][0]:
                _, x = stack.pop()
                right_lower[x] = i
            stack.append((h, i))
        
        left_lower = [-1] * len(heights)
        stack = []
        for i in range(len(heights) - 1,-1,-1):
            h = heights[i]
            while stack and h < stack[-1][0]:
                _, x = stack.pop()
                left_lower[x] = i
            stack.append((h, i))

        result = []
        for i, h in enumerate(heights):
            left = left_lower[i]
            right = right_lower[i]

            print(left, right)

            size = h * (right - left - 1)
            result.append(size)
        
        return max(result)

        