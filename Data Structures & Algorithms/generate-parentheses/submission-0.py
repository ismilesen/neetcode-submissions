class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def back(openCount, ClosedCount):
            if openCount == ClosedCount == n:
                res.append("".join(stack))
                return
            if openCount < n:
                stack.append("(")
                back(openCount + 1, ClosedCount)
                stack.pop()
            if ClosedCount < openCount:
                stack.append(")")
                back(openCount, ClosedCount + 1)
                stack.pop()
        back(0, 0)
        return res