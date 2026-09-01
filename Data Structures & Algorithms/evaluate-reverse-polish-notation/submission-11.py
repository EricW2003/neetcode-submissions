class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in ["+","-","/","*"]:
                stack.append(int(token))
            if token=="+":
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
            if token=="-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            if token=="*":
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
            if token=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(float(b)/a))
        return stack.pop()