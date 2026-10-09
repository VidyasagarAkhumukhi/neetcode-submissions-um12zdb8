class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        stack = [] #pair, index and the height from heights list

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                indexPop, heightPop = stack.pop()
                maxArea = max(maxArea, heightPop * (i - indexPop))
                start = indexPop
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
        

        # brute force Tc n2 sc 1
        # n = len(heights)
        # maxArea = 0

        # for i in range(n):
        #     height = heights[i]

        #     rightMost = i + 1
        #     while rightMost < n and heights[rightMost] >= height:
        #         rightMost += 1

        #     leftMost = i
        #     while leftMost > 0 and heights[leftMost] >= height:
        #         leftMost -= 1

            
        #     rightMost -= 1
        #     leftMost += 1

        #     maxArea = max(maxArea, height * (rightMost - leftMost + 1))

        # return maxArea
