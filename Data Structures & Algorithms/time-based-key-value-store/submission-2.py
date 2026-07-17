class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr_key = self.store.get(key, [])
        curr_key.append((timestamp, value))
        self.store[key] = curr_key

    def get(self, key: str, timestamp: int) -> str:
        search_space = self.store.get(key, [])

        if not search_space:
            return ""

        l, r = 0, len(search_space) - 1
        while l < r:
            middle = (l + r + 1) // 2
            time, value = search_space[middle]

            if time == timestamp:
                return value
            elif time > timestamp:
                r = middle - 1
                continue
            else:
                l = middle
        time, value = search_space[l]
        if time <= timestamp:
            return value
        else:
            return ""







