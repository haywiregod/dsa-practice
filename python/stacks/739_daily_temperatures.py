# https://leetcode.com/problems/daily-temperatures/description/
from typing import List

"""
Problem Context:

Typically, the problem asks you to find, for each day in an array of temperatures, how many days you have to wait until a warmer temperature occurs. If there's no future day with a warmer temperature, you return 0 for that day.
Time Complexity Analysis:

The reason the solution is O(n)O(n) (linear time complexity) involves the use of a stack to keep track of indices of the temperature array.

    Single Pass: You traverse the list of temperatures only once. For each temperature, you:
        Compare it with the temperatures at the indices stored in the stack.
        Pop the stack until you find a previous day where the current temperature is warmer or the stack is empty.
        Push the current day onto the stack.

    Push and Pop Operations: Each index is pushed and popped from the stack at most once, resulting in O(1)O(1) operations per index.

Detailed Breakdown:

    Stack Operations: In the worst case, every element of the array is pushed onto the stack and then popped. This gives a total of O(n)O(n) operations for an array of size nn.
    Final Complexity: Since you process each temperature once and each temperature is pushed and popped from the stack at most once, the overall time complexity is O(n)O(n).

Thus, the algorithm efficiently computes the number of days until a warmer temperature for each day in linear time, making it O(n)O(n).

"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for index in range(length):
            temp = temperatures[index]
            while stack and temp > temperatures[stack[-1]]:
                i = stack.pop()
                ans[i] = index - i
            stack.append(index)
        return ans

    def bruteForce(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        for i in range(length):
            for j in range(i + 1, length):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
        return ans


sol = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(sol.bruteForce(temperatures=temperatures))
print(sol.dailyTemperatures(temperatures=temperatures))
