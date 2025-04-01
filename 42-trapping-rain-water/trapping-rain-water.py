class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        lh, rh = height[i], height[j]
        total = 0

        while i<j:
            if lh < rh:
                i += 1
                lh = max(lh, height[i])
                total += lh -height[i]
            else:
                j -= 1
                rh = max(rh, height[j])
                total += rh -height[j]
        
        return total


        
        

        