class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for string in strs:
            temp = [0] * 26
            for char in string:
                temp[ord(char) - ord('a')] += 1
            
            table[tuple(temp)].append(string)

        res = []
        for strings in table.values():
            temp = []
            for string in strings:
                temp.append(string)
            res.append(temp)

        return res
