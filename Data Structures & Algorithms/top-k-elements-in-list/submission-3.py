class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #First solution is sorting.

        cnt_map = {}
        for i in nums:
            cnt_map[i] = cnt_map.get(i, 0) + 1

        res = []
        for cnt, val in cnt_map.items():
            res.append([val, cnt])
        
        res.sort()
        final_result = []
        while len(final_result) < k:
            final_result.append(res.pop()[1])

        return final_result