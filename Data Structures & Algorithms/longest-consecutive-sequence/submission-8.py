class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        longest = 0
        for num in lookup:
            if num-1 not in lookup:
                length = 1
                while(num + length) in lookup:
                    length = length + 1
                longest = max(length, longest)
        return longest
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
        # lookup = set(nums)
        # res = 0 

        # for num in lookup:
        #     streak = 0 
        #     curr = num
        #     while curr in lookup:
        #         curr = curr+1
        #         streak =streak+1
        #     res = max(streak, res)

        # return res