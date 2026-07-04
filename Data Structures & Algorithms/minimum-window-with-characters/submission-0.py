class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        map_t = {}
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1

        res = [-1, -1]
        resLen = float('infinity')
        need = len(map_t)
        have = 0
        window = {}
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            
            if s[r] in map_t and window.get(s[r]) == map_t.get(s[r]):
                have +=1

            while need == have:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                window[s[l]]-=1
                if s[l] in map_t and window.get(s[l]) < map_t.get(s[l]):
                    have-=1
                l+=1
        l, r = res
        return s[l: r+1] if resLen != float('infinity') else ''

                