class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        x,y = 0,0
        dirX,dirY = 0,1

        for d in instructions:
            if d == "G":
                x,y = x+dirX,y+dirY
            elif d == "L":
                dirX,dirY = -dirY,dirX
            else:
                dirX,dirY = dirY,-1*dirX
        return (x,y) == (0,0) or (dirX,dirY) !=(0,1)

