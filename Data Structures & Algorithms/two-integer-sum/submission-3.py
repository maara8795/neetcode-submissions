class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #remain
        remain_map = {}

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in remain_map:
                return [remain_map[remain], i]
            else:
                remain_map[nums[i]] = i

        return []