class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr_string: str, open_brackets: int, close_brackets: int, n: int) -> None:
            if close_brackets == n:
                res.append(curr_string)
                return

            if open_brackets < n:
                backtrack(curr_string + '(', open_brackets + 1, close_brackets, n)

            if close_brackets < open_brackets:
                backtrack(curr_string + ')', open_brackets, close_brackets + 1, n)

        backtrack("", 0, 0, n)
        return res
