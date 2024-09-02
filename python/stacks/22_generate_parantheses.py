# https://leetcode.com/problems/generate-parentheses/description/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(openCount, closedCount, parantheses=""):
            if openCount == closedCount == n:
                result.append(parantheses)
                return

            if openCount < n:
                backtrack(openCount + 1, closedCount, parantheses + "(")

            if closedCount < openCount:
                backtrack(openCount, closedCount + 1, parantheses + ")")

        backtrack(0, 0)
        return result
