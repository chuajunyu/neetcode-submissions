class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we can transform this into a mountain stack like problem

        pairs = [(position[i], speed[i]) for i in range(len(position))]
        pairs.sort(key=lambda x: x[0])

        time = [(target - p) / s for p, s in pairs]
        
        # now, to find a fleet, we just need to track find the first car after that is travelling faster
        stack = []
        for t in time:
            # whilst the previous car is travelling faster
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)  # monotonically increasing
        return len(stack)