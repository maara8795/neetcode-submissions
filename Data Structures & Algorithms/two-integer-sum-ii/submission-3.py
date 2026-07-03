class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #brute force is O(n square)
        #then with hashmap can do O(n) time and space

        maps = {}

        for i in range(len(numbers)):
            index = i
            val = numbers[i]
            remain = target - val
            if remain in maps:
                return [maps[remain], index + 1]
            else:
                maps[val] = index + 1

        