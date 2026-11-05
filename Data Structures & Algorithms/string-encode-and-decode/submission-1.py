class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            temp = ""
            while i < len(s) and s[i] != '#':
                temp += s[i]
                i += 1
            i += 1
            res.append(s[i:i + int(temp)])
            i += int(temp)

        return res
