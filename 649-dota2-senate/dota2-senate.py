class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate = list(senate)
        D, R = deque(), deque()
        for i,c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)

        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if rTurn < dTurn:
                R.append(rTurn + len(senate))
            else:
                D.append(dTurn + len(senate))


        return "Radiant" if R else "Dire"
        