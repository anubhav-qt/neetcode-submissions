class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open_brackets: int, close_brackets: int) -> None:
            if close_brackets == n:
                res.append("".join(stack))
                return

            if open_brackets < n:
                stack.append('(')
                backtrack(open_brackets + 1, close_brackets)
                stack.pop()

            if close_brackets < open_brackets:
                stack.append(')')
                backtrack(open_brackets, close_brackets + 1)
                stack.pop()

        backtrack(0, 0)
        return res
