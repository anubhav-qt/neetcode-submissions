class Solution:
    def numDecodings(self, s: str) -> int:
        self.res, mapping_set = 0, set()
        for i in range(1, 27):
            mapping_set.add(str(i))

        def backtrack(start_index: int) -> None:
            if start_index == len(s):
                self.res += 1
                return
            if start_index > len(s):
                return

            for end_index in range(start_index, len(s)):
                if end_index - start_index + 1 <= 2:
                    if s[start_index: end_index + 1] not in mapping_set:
                        continue
                    backtrack(end_index + 1)
            
        backtrack(0)
        return self.res
