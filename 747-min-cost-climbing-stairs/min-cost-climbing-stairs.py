class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def min_cost(i):
            if i <= 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            one = cost[i-1] + min_cost(i-1)
            two = cost[i-2] + min_cost(i-2)
            memo[i] = min(one, two)
            return memo[i]

        memo = {}
        return min_cost(len(cost))
        