class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        l = 0 
        maxP = 0

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxP = max(maxP, r-l+1)


        return maxP