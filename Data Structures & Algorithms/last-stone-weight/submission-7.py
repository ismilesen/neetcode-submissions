class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y = abs(heapq.heappop(max_heap))
            x = abs(heapq.heappop(max_heap))
            if y != x:
                if y > x:
                    value = -(y - x)
                else:
                    value = -(x - y)
                heapq.heappush(max_heap, value) 

        if not max_heap:
            return 0

        return abs(max_heap[0])
