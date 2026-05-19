class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paren_stack = []
        sol = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                sol.append("".join(paren_stack))
                return

            if openN < n:
                paren_stack.append("(")
                backtrack(openN + 1, closedN)
                paren_stack.pop()

            if closedN < openN:
                paren_stack.append(")")
                backtrack(openN, closedN + 1)
                paren_stack.pop()

        backtrack(0, 0)
        return sol