class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter_map = {}
        
        for num in nums:
             counter_map[num] = 1 + counter_map.get(num, 0)

        initialize_freq = [[] for i in range(len(nums)+1)]

        for key, val in counter_map.items():
            initialize_freq[val].append(key)
        print(initialize_freq)

        res = []
        for i in range(len(initialize_freq)-1, 0, -1):
            for num in initialize_freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        # heap = []
        # for num in counter_map.keys():
        #     heapq.heappush(heap, (counter_map[num], num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)

        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

