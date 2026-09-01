class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        ans = 0
        for operation in operations:
            if operation == "+":
                ans += stack[-1]+stack[-2]
                stack.append(stack[-1]+stack[-2])
            elif operation == "C":
                ans -= stack.pop()
            elif operation == "D":
                ans += 2*stack[-1]
                stack.append(2*stack[-1])
            else:
                ans += int(operation)
                stack.append(int(operation))
        return ans