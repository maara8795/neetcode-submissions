class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Since only one valid answer exists

        #for i in range(len(nums)):
        ##    remain = target - nums[i]
        #    for j in range(len(nums)):
        #        if i!=j:
        #            if nums[j]==remain:
        #                return[i, j]

        #maybe can do a hash solution
        hash_remain = {}
        for i in range(len(nums)):
            remain = target-nums[i]
            if remain in hash_remain:
                return [hash_remain[remain], i]
            hash_remain[nums[i]] = i