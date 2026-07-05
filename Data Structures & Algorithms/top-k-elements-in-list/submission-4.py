class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        cnt_map = {}
        for i in nums:
            cnt_map[i] = cnt_map.get(i, 0) + 1
        
        heap = []

        for num, cnt in cnt_map.items():
            heapq.heappush(heap, [cnt, num])
            if len(heap) > k :
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        
        #First solution is sorting. o(nlogn) and o(n)

        # cnt_map = {}
        # for i in nums:
        #     cnt_map[i] = cnt_map.get(i, 0) + 1

        # res = []
        # for cnt, val in cnt_map.items():
        #     res.append([val, cnt])
        
        # res.sort()
        # final_result = []
        # while len(final_result) < k:
        #     final_result.append(res.pop()[1])

        # return final_result