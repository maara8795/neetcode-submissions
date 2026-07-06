class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        map_t = {}

        for i in range(len(t)):
            map_t[t[i]] = map_t.get(t[i],0)+1
        print(map_t)
        res = [-1,-1]
        resLen = float('infinity')
        l = 0 
        window = {}
        need = len(map_t)
        have = 0

        for r in range(len(s)):

            window[s[r]]=window.get(s[r],0)+1

            if s[r] in map_t and map_t.get(s[r]) == window.get(s[r]):
                have+=1

            while need == have:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]]-=1
                if s[l] in map_t and window.get(s[l]) < map_t.get(s[l]):
                    have-=1
                l+=1
        
        l, r = res

        if resLen != float('infinity'):
            return s[l:r+1]
        else:
            return ""
        
