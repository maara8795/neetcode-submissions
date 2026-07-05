class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #can try the ord ones this will be O(1) and O(n+m)

        if len(s) != len(t):
            return False

        val = [0]*26

        for ind in range(len(s)):
            val[ord(s[ind]) - ord('a')] +=1
            val[ord(t[ind]) - ord('a')] -=1

        for v in val:
            if v!=0:
                return False

        return True