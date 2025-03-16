class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}

        def dfs(i):
            if i>= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]


        return dfs(0)
            