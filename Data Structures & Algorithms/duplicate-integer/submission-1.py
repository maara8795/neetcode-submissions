class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for i in range(len(nums)):
            element = nums[i]
            if count_map.get(element, None):
                count_map[element] = count_map[element] + 1
            else:
                count_map[element] = 1
        
        for j in count_map.values():
            if j>1:
                return True
        return False