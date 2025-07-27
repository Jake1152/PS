class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack = []
        for ch in s:
            print(f"{ch=}")
            if ch in [ '(', '[', '{']:
                parentheses_stack.append(ch)
            else:
                if len(parentheses_stack) == 0:
                    return False
                top = parentheses_stack.pop()
                if ch == ')' and top == '(':
                    continue
                elif ch == ']' and top == '[':
                    continue
                elif ch == '}' and top == '{':
                    continue
                else:
                    return False
        if len(parentheses_stack) > 0:
            return False
        return True
