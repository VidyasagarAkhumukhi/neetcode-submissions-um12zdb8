class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                firstPop, secondPop = stack.pop(), stack.pop()
                stack.append( secondPop - firstPop )
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                firstPop, secondPop = stack.pop(), stack.pop()
                stack.append( int(secondPop / firstPop) )
            else:
                stack.append(int(c))

        return stack[0]
            