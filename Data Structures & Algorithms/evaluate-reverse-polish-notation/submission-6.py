class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(t, stack)
            if t in '+-*/':
                y = stack.pop()
                x = stack.pop()
                match t:
                    case '+':
                        stack.append(x + y)
                    case '-':
                        stack.append(x - y)
                    case '*':
                        stack.append(x * y)
                    case '/':
                        tmp = x / y
                        truncated = int(abs(tmp))
                        tmp = truncated if tmp >= 0 else -truncated
                        stack.append(tmp)
            else:
                stack.append(int(t))
            
        return stack[0]


        