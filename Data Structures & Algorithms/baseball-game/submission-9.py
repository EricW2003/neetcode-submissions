class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        ans = 0
        for operation in operations:
            if operation == "+":
                res = stack[-1]+stack[-2]
                ans += res
                stack.append(res)
            elif operation == "C":
                res =stack.pop()
                ans -= res
            elif operation == "D":
                res = 2*stack[-1]
                ans += res
                stack.append(res)
            else:
                res = int(operation)
                ans += res
                stack.append(res)
        return ans