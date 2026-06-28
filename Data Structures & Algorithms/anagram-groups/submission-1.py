class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        overall_map = {}
        for i in range(len(strs)):
            word = strs[i]
            sorted_word = "".join(sorted(word))
            if sorted_word in overall_map:
                existing = overall_map.get(sorted_word)
                existing.append(word)
            else:
                overall_map[sorted_word] = [word]

        res = []
        for k, v in overall_map.items():
            res.append(v)

        return res
