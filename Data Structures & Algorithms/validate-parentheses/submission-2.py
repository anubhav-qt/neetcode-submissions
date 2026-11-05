class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parenthesis = ('[', '{', '(')
        for c in s:
            if c in open_parenthesis:
                stack.append(c)
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(c)
            elif c == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack) == 0
