class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #I can sor tthe strings and compare character by character this 
        # would be O(nlongn) time and O(n) memory 
        # Or use hashmap again individually to count then compare count 
        # Time is O(n) and O(n)

        if len(s) != len(t):
            return False

        #sorted_s = sorted(s)
        #sorted_t = sorted(t)

        hash_s = {}
        for i in s:
            if hash_s.get(i,0):
                hash_s[i]+=1
            else:
                hash_s[i]=1

        hash_t = {}
        for j in t:
            if hash_t.get(j,0):
                hash_t[j]+=1
            else:
                hash_t[j]=1
        print(hash_s)
        print(hash_t)
        for k,v in hash_s.items():
            if hash_t.get(k) == v:
                continue
            else:
                return False

        return True