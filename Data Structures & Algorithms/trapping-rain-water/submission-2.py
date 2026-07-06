class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l = 0
        r = len(height)-1
        res = 0
        maxLeft = height[l]
        maxRight = height[r]

        while (l<r):

            if height[l]<=height[r]:
                l+=1
                maxLeft = max(maxLeft, height[l])
                res+=maxLeft-height[l]

            elif height[l]>height[r]:
                r-=1
                maxRight = max(maxRight, height[r])
                res+=maxRight-height[r]

        return res
