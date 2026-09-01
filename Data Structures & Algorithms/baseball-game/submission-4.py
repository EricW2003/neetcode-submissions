class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        for operation in operations:
            if operation == "+":
                stack.append(stack[-1]+stack[-2])
                print(stack)
            elif operation == "C":
                stack.pop()
                print(stack)
            elif operation == "D":
                stack.append(2*stack[-1])
                print(stack)
            else:
                stack.append(int(operation))
                print(stack)
        print(stack)
        return sum(stack)