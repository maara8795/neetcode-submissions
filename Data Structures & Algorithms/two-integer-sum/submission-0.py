class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Since only one valid answer exists

        for i in range(len(nums)):
            remain = target - nums[i]
            for j in range(len(nums)):
                if i!=j:
                    if nums[j]==remain:
                        return[i, j]