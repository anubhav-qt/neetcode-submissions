class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pattern = {'}': '{', ']': '[', ')': '('}
        
        for c in s:
            if c in pattern:
                if stack and stack[-1] == pattern[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
