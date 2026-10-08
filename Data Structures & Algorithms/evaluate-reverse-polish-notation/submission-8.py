class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())

            elif c == "-":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)

            elif c == "*":
                stack.append(stack.pop() * stack.pop())

            elif c == "/":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 / num2))

            else:
                stack.append(int(c))
        
        return stack[0]
        
        
        
            
        
        
        
        
        # brute force TN n2 sc n
        # while len(tokens) > 1:
        #     for i in range(len(tokens)):
                
        #         if tokens[i] in "+-*/":
        #             num1 = int(tokens[i-2])
        #             num2 = int(tokens[i-1])
        #             if tokens[i] == "+":
        #                 result = num1 + num2
        #             elif tokens[i] == "-":
        #                 result = num1 - num2
        #             elif tokens[i] == "*":
        #                 result = num1 * num2
        #             elif tokens[i] == "/":
        #                 result = int(num1 / num2)
                    
        #             tokens = tokens[ : i - 2] + [str(result)] + tokens[i + 1 : ]

        #             break
        
        # return int(tokens[0])
                

        
        