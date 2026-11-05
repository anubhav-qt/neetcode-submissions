class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        
        count = list(set(nums))
        new_count = [(-count_map[num], num) for num in count]

        heapq.heapify(new_count)
        output = []
        for _ in range(k):
            output.append(heapq.heappop(new_count)[1])
        
        return output
