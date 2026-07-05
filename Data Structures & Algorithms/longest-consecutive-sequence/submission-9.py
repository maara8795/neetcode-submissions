class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        sorted_arr = sorted(nums)
        streak = 1
        i = 0
        while i < len(sorted_arr)-1:
            if sorted_arr[i+1] - sorted_arr[i] == 1:
                streak = streak + 1
            elif sorted_arr[i+1] - sorted_arr[i] == 0:
                pass
            else:
                streak = 1
            i = i + 1
            res = max(res, streak)
        return res
        # if len(nums)==0:
        #     return 0
        # lookup = sorted(nums)
        # res = 1
        # i = 0
        # streak = 1
        # while i < len(lookup)-1:
        #     if lookup[i+1]-lookup[i]==1:
        #         streak = streak + 1
        #     elif lookup[i+1] - lookup[i] == 0:
        #         pass        # duplicate, skip silently
        #     else:
        #         streak = 1
        #     i = i + 1 
        #     res = max(res, streak)
        # return res

        # res = 0
        # lookup = set(nums)
        # for num in lookup:
        #     curr = num
        #     streak = 0
        #     while curr in lookup:
        #         curr = curr + 1
        #         streak = streak + 1 
        #     res = max(res, streak)
        # return res