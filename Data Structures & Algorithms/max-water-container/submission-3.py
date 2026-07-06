class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0 
        j = len(heights)-1
        max_water =0

        while(i<j):
            water_stored = min(heights[i], heights[j])*(j-i)

            if heights[i]<heights[j]:
                i+=1
            elif heights[i]>=heights[j]:
                j-=1

            max_water = max(max_water, water_stored)

        return max_water