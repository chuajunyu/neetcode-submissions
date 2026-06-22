class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # keep a monotonically decreasing stack
        # this is the same as the mountain stack problem!!!

        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack:
                x, top = stack[-1]
                if t > top:
                    result[x] = i - x
                    stack.pop()
                else:
                    break
            stack.append((i, t))
        return result

