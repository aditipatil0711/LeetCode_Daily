class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x,y = 0,0
        xi,yi = 0,0

        for i in moves:
            if i == "U":
                x,y = x,y+1
            elif i == "D":
                x,y = x,y-1
            elif i == "L":
                x,y = x-1,y
            elif i=="R":
                x,y = x+1,y

        return (x==xi and y==yi)