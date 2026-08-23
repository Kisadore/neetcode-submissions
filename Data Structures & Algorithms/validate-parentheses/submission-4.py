class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            else:
                if not stack:
                    return False
                check = stack.pop()
                if char == ']' and check != '[':
                    return False
                if char == ')' and check != '(':
                    return False
                if char == '}' and check != '{':
                    return False
        return not stack