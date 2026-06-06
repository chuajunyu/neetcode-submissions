class Solution:
    def trap(self, height: List[int]) -> int:
        # For each bar, I want to look back to see the tallest thing i can see
        # 2 pointer
        # to know the height of place, we need to know the max height of the left and max height of the right
        right = [0]
        for h in height[::-1]:    
            right.append(max(h, right[-1]))
        right = list(reversed(right[1:]))

        print(right)

        result = 0
        left = 0
        # ignore the first because thats the sum of all
        for i in range(len(height)):
            r = right[i]
            result += max(0, min(left, r) - height[i])
            left = max(left, height[i])
        
        return result


        