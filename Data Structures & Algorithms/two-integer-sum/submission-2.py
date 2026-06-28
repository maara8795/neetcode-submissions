class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Have to iterate atleast once

        sum_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sum_map:
                return [sum_map[diff], i]
            sum_map[nums[i]] = i