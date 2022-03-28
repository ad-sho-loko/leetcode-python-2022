class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                popped = stack.pop()
                if ch == ')' and popped != '(':
                    return False
                if ch == '}' and popped != '}':
                    return False
                if ch == ']' and popped != '[':
                    return False

        return len(stack) == 0
