class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        for i in range(len(strs)):
            word = strs[i]
            sorted_word = "".join(sorted(word))
            if sorted_word in res.keys():
                existing = res.get(sorted_word)
                existing.append(word)
            else:
                res[sorted_word] = [word]

        final_res = []
        for k, v in res.items():
            final_res.append(v)

        return final_res