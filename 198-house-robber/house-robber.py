class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}  # Memoization dictionary

        def dfs(i):
            if i >= len(nums):
                return 0  # Base case
            
            if i in memo:
                return memo[i]  # Use stored result if available
            
            # Recurrence relation
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))  # Correct way to store in memo
            
            return memo[i]  # Return the computed value

        return dfs(0)  # Start from the first house
            