from bisect import bisect_right

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

        i = bisect_right(self.store[key], timestamp, key=lambda x: x[0]) - 1
        
        return self.store[key][i][1] if i >=0 else ""
