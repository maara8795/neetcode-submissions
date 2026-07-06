class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isalphanum(c):
            return (ord('a') <= ord(c) <= ord('z') or
                    ord('A') <= ord(c) <= ord('Z') or
                    ord('0') <= ord(c) <= ord('9'))

        l = 0 
        r = len(s)-1

        while(l<r):

            if not isalphanum((s[l])):
                l+=1
            elif not isalphanum((s[r])):
                r-=1
            elif isalphanum((s[l])) and isalphanum((s[r])):
                if s[l].lower() == s[r].lower():
                    l+=1
                    r-=1
                else:
                    return False

            
        return True

            
