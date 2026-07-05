class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix and postfix array 

        res = [1]* len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix*=nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]

        return res
        
        #Division O(n) and O(n)
        # prod = 1
        # zero_cnt=0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         prod*=nums[i]
        #     else:
        #         zero_cnt+=1
        
        # if zero_cnt > 1:
        #     return [0]*len(nums)

        # res = [1]*len(nums)

        # for i in range(len(nums)):

        #     if zero_cnt:
        #         if nums[i]:
        #             res[i] = 0 
        #         else:
        #             res[i] = prod
        #     else:
        #         res[i] = prod // nums[i]
        # return res
        #Brute force is O(n square) and sc o(n)
        # res = []
        
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     res.append(prod)

        # return res
