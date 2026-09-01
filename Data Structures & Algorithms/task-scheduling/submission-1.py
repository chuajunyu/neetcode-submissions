import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # minheap of the next thing that can be inserted
        # Greedily always pick the thing that can be done the earliest?

        counts = [0] * 26
        offset = ord('A')

        for t in tasks:
            counts[ord(t) - offset] += 1
        
        # ready heap: store -count, char
        max_heap = [(-count, chr(i + ord('A'))) for i, count in enumerate(counts) if count > 0]
        heapq.heapify(max_heap)

        # waiting heap: store time, char
        min_heap = []
        heapq.heapify(min_heap)

        t = 1
        while max_heap or min_heap:
            if max_heap:
                count, task = heapq.heappop(max_heap)
                count += 1
                if count < 0:
                    heapq.heappush(min_heap, (t + n + 1, (count, task)))

            t += 1
            while min_heap: 
                time, (count, task) = min_heap[0]
                if time <= t:
                    heapq.heappop(min_heap)
                    heapq.heappush(max_heap, (count, task))
                elif not max_heap:
                    t = time
                    heapq.heappop(min_heap)
                    heapq.heappush(max_heap, (count, task))
                else:
                    break
        
        return t - 1
        
        