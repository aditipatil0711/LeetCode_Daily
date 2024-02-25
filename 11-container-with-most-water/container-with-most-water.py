class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        maxarea = 0
        r = len(height)-1

        while l<r:
            width = r-l
            maxarea = max(maxarea,min(height[l],height[r])*width)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxarea
        