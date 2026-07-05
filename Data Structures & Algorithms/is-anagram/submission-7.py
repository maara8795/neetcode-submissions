class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #can sort and then compare char by char which 
        #which could be O(nlogn) based on sorting algo
        if len(s) != len(t):
            return False
        #can use hashmap to do O(n)

        map_s = {}
        for i in s:
            map_s[i] = map_s.get(i,0) + 1

        map_t = {}
        for j in t:
            map_t[j] = map_t.get(j,0) + 1
        print(map_s)
        print(map_t)
        for k, v in map_s.items():
            if map_t.get(k) == v:
                continue
            else:
                return False
        return True