class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dirX, dirY = 0,1 # facing north
        x,y = 0,0 # initial position

        for direction in instructions:
            if direction =="G":
                x,y = x+dirX, y+dirY
            elif direction == "L":
                dirX,dirY = -1*dirY, dirX # -ve scale of plane X
            else:
                dirX,dirY = dirY, -1*dirX
        return (x,y) == (0,0) or (dirX,dirY) !=(0,1)

        # return if you make a circle or direction changed atleast by 1
                                       


                                                                                                                                                                 