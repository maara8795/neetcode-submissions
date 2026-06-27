class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        res = 0 

        for num in lookup:
            streak = 0 
            curr = num
            while curr in lookup:
                curr = curr+1
                streak =streak+1
            res = max(streak, res)

        return res