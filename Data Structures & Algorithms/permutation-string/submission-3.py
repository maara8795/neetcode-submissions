class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_map = {}

        for i in s1:
            s1_map[i]=s1_map.get(i,0)+1

        need = len(s1_map)
        
        for i in range(len(s2)):
            window_map = {}
            curr = 0

            for j in range(i, len(s2)):
                window_map[s2[j]] = window_map.get(s2[j],0)+1
                if s1_map.get(s2[j],0) < window_map.get(s2[j],0):
                    break
                if s1_map.get(s2[j],0) == window_map.get(s2[j],0): 
                    curr = curr+1
                if curr == need:
                    return True

        return False
                

            