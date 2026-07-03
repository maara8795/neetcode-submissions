class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        max_freq = 0
        l = 0
        result = 0

        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            max_freq = max(max_freq, hashmap[s[r]])

            while (r-l+1) - max_freq > k :
                hashmap[s[l]] -=1
                l+=1
            result = max(result, r-l+1)
        return result