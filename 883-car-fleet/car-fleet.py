class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        no_of_cars = len(position)
        if no_of_cars <= 1:
            return no_of_cars

        stack = []
        position_speed = [[p, s] for p,s in zip(position, speed)]
        position_speed = sorted(position_speed, reverse=True)
        for p,s in position_speed:
            time = float(target-p)/s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
