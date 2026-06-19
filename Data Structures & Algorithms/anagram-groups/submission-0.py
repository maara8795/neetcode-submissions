class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        overall = {}
        for i in range(len(strs)):
            word = strs[i]
            sorted_word = ''.join(sorted(word))
            if sorted_word in overall:
                group_list = overall.get(sorted_word)
                group_list.append(word)
            else:
                overall[sorted_word] = [word]

        final_list = []
        for k,v in overall.items():
            final_list.append(v)

        return final_list