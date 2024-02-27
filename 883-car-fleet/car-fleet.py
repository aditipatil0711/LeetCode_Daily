class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = []
        for pos, spe in zip(position, speed):
            pair.append((pos,spe))
        pair.sort(reverse=True)
        time = float(target - pair[0][0]) / pair[0][1]
        num = 1
        for p,s in pair:
            cur_time = float(target - p) / s
            if (float(target - p) / s) > time: 
                num+=1
                time = cur_time
        return num