from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for index, string in enumerate(strs):
            count = [0] * 26
            for char in string:
                count[ord(char) - 97] += 1

            tuple_count = tuple(count)            
            if tuple_count in seen:
                seen[tuple_count].append(index)
            else:
                seen[tuple_count] = [index]
        
        res = []
        for value in seen.values():
            res.append([strs[i] for i in value])

        return res
