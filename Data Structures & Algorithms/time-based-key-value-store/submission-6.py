class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr_key = self.store.get(key, [])
        curr_key.append((timestamp, value))
        self.store[key] = curr_key

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.store.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            middle = (l + r) // 2
            time, value = values[middle]
            if time <= timestamp:
                res = value
                l = middle + 1
            else:
                r = middle - 1
        return res
                







