class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [1] * len(nums)
        right_arr = [1] * len(nums) # this is the result
        for i in range(1, len(nums)):
            left_arr[i] = left_arr[i-1]* nums[i-1]
        print(left_arr)

        for j in range(len(nums)-2, -1, -1):
            right_arr[j] = right_arr[j+1] * nums[j+1]
        print(right_arr)
        res = []
        for k in range(len(nums)):
            res.append(left_arr[k]*right_arr[k])
        return res
        