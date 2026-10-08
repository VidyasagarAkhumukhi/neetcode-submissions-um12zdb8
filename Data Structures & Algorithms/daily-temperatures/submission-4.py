class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] #pair of values [temp, index of the temp]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()

                res[stackIndex] = i - stackIndex
            
            stack.append([temp, i])

        return res
               
                
               
        
        # brute force Tc n2 sc 1 or n
        # n = len(temperatures)

        # res = [0] * n

        # for i in range(n):
        #     for j in range( i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        # return res         


