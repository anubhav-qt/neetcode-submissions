import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = Counter(nums)
        heap = []

        for key, value in table.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            elif heap[0][0] < value:
                heapq.heappop(heap)
                heapq.heappush(heap, (value, key))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
