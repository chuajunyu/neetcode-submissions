def upper_bound(x, target, key=lambda x: x):
    # Find the index of the largest element <= target
    l, r = 0, len(x) - 1
    res = None
    while l <= r:
        m = (l + r) // 2
        curr = key(x[m])
        if curr <= target:
            res = m
            l = m + 1
        else:
            r = m - 1
    return res

class TimeMap:

    def __init__(self):
        self.store = {}  # dictionary of list

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        i = upper_bound(self.store[key], timestamp, key=lambda x: x[0])
        
        return self.store[key][i][1] if i is not None else ""
    
