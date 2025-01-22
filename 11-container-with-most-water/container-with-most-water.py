class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        l = 0
        r = len(height)-1

        while l<r:
            width = r-l
            maxArea = max(maxArea,min(height[l],height[r])*width)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return maxArea
        