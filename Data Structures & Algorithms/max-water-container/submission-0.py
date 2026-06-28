class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i !=j : 
                    area = (j-i)*min(heights[i], heights[j])
                    maxArea = max(area, maxArea)

        return maxArea