class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checkKeys = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in checkKeys:
                if stack and stack[-1] == checkKeys[c]:
                    stack.pop()
                else:
                    return False            
            else:
                stack.append(c)
        
        return True if not stack else False