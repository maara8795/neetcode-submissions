class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # THis is also maybe hash dict and counts
        string_s = {}
        for i in range(len(s)):
            if string_s.get(s[i]):
                string_s[s[i]] = string_s[s[i]]+1
            else:
                string_s[s[i]] = 1

        string_t = {}
        for i in range(len(t)):
            if string_t.get(t[i]):
                string_t[t[i]] = string_t[t[i]]+1
            else:
                string_t[t[i]] = 1

        if len(s)!=len(t):
            return False
            
        for i in range(len(s)):
            if string_s.get(s[i]) != string_t.get(s[i]):
                return False
        return True
            