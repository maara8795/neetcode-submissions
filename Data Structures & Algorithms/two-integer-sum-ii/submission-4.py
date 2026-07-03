class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #brute force is O(n square)
        #then with hashmap can do O(n) time and space

        #To do better can use pointers

        i = 0 
        j = len(numbers)-1
        moving_sum = 0

        while i < j :
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                j-=1


        # maps = {}

        # for i in range(len(numbers)):
        #     index = i
        #     val = numbers[i]
        #     remain = target - val
        #     if remain in maps:
        #         return [maps[remain], index + 1]
        #     else:
        #         maps[val] = index + 1

        