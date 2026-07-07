class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        #window shrinking condition is 
        #window size r-l+1 - max freq in window > k 

        l = 0 
        window_freq = {}
        maxFreq = 0
        longest = 0

        for r in range(len(s)):
            window_freq[s[r]] = window_freq.get(s[r],0)+1
            maxFreq = max(maxFreq, window_freq[s[r]])

            while (r-l+1) - maxFreq > k :
                window_freq[s[l]] = window_freq.get(s[l],0) - 1
                l+=1

            longest = max(longest, r-l+1)

        return longest