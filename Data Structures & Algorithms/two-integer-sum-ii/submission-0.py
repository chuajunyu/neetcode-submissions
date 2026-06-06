class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i, n in enumerate(numbers):
            if target - n in h:
                return [h[target - n] + 1, i + 1]
            else:
                h[n] = i
