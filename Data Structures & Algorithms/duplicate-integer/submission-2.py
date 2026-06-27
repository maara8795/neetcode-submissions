class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Goign to use hashmap so O(n) and O(n) time complexity 
        #can i do better than this probably not

        hashmap = {}
        for num in nums:
            if hashmap.get(num, 0):
                return True
            else:
                hashmap[num] = 1
        return False