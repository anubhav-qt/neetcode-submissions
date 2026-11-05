class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))
            res += "#"
            for char in string:
                res += char
        
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            temp = ""
            while i < len(s) and s[i] != '#':
                temp += s[i]
                i += 1
            i += 1
            tmp = ""
            for j in range(i, i + int(temp)):
                tmp += s[j]
            i += int(temp)
            res.append(tmp)
        
        return res
