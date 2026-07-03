class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanum(char):
            print("here")
            return (ord('A') <= ord(char) <= ord('Z') or
                   ord('a') <= ord(char) <= ord('z') or
                   ord('0') <= ord(char) <= ord('9'))
        i = 0 
        j = len(s)-1

        while i<j:
            if not isalphanum(s[i]):
                i+=1
            elif not isalphanum(s[j]):
                j-=1
            elif isalphanum(s[i]) and isalphanum(s[j]):
                if s[i].lower() == s[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
        return True



        