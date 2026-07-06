class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0 
        maxFreq = 0
        hash_map = {}
        longest = 0

        for r in range(len(s)):
            hash_map[s[r]] = hash_map.get(s[r], 0) +1
            maxFreq = max(maxFreq, hash_map[s[r]])

            while (r-l+1) - maxFreq > k : #shrinking
                hash_map[s[l]]-=1
                l+=1
            longest = max(longest, r-l+1)
                
        return longest