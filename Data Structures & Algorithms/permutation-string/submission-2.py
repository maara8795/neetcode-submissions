class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        map_s1 = {}

        for s in s1:
            map_s1[s] = 1 + map_s1.get(s, 0)

        need = len(map_s1)

        for i in range(len(s2)):
            map_s2 = {}
            curr = 0

            for j in range(i, len(s2)):
                map_s2[s2[j]] = 1 + map_s2.get(s2[j], 0)
                if map_s1.get(s2[j], 0) < map_s2.get(s2[j]):
                    break
                if map_s1.get(s2[j], 0) == map_s2.get(s2[j]):
                    curr = curr + 1
                if curr == need:
                    return True
        return False


