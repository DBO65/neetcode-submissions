class Solution:
    def isValid(self, s: str) -> bool:
        check = {')': '(', ']' : '[', '}' : '{'}
        stack = []

        for b in s:
            if b in check.keys():
                if check[b] not in stack:
                    return False
                elif stack[-1] != check[b]:
                    return False
                else:
                    stack.pop()
                    continue

            stack.append(b)

        if stack:
            return False

        return True 
