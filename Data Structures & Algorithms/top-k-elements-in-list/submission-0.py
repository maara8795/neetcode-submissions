class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter_map = {}
        
        for num in nums:
            counter_map[num] = 1 + counter_map.get(num, 0)

        heap = []
        for num in counter_map.keys():
            heapq.heappush(heap, (counter_map[num], num))
            if len(heap)>k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res