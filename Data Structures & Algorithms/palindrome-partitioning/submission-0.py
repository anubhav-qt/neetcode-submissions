class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        def backtrack(start_index: int, palindromes: List[int]) -> None:
            if start_index >= len(s):
                self.res.append(palindromes.copy())
                return

            for i in range(start_index, len(s)):
                if check_palindrome(s[start_index: i + 1]):
                    palindromes.append(s[start_index: i + 1])
                    backtrack(i + 1, palindromes)
                    palindromes.pop()

        def check_palindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1 
                r -= 1
            return True

        backtrack(0, [])
        return self.res
