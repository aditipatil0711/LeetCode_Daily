class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        step, seen = 0, 1 << amount
        while seen & 1 != 1:
            cur = seen
            for coin in coins:
                cur |= seen >> coin
            if cur == seen:
                return -1
            step, seen = step + 1, cur
        return step
