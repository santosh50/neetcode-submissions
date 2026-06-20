class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
            else:
                if not stk:
                    return False
                opening = stk.pop()
                if opening == '(' and c != ')':
                    return False
                if opening == '[' and c != ']':
                    return False
                if opening == '{' and c != '}':
                    return False
        
        return not stk
        