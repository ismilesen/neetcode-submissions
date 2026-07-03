class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #go through the list.
        #if an iteration to the right is smaller than current then i is popped. The calculated left width is added to the current
        #then we continue on the stack
        #example: 1, 2, 3, 4. Since 2,3,4 are greater than 1. We will return 1 x 4. 1 height iteration point,
        #4 for length but not height.
        #return max area
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
            