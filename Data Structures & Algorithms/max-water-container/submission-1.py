class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Given a bar, always move the smaller side of the container
        left, right = 0, len(heights) - 1

        max_area = min(heights[left], heights[right]) * (right - left)
        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            max_area = max(
                max_area, 
                min(heights[left], heights[right]) * (right - left)
            )

        return max_area
        