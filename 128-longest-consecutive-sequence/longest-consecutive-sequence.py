class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()

        longest_streak = 1
        curr_streak = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    curr_streak +=1
                else:
                    longest_streak = max(longest_streak, curr_streak)
                    curr_streak =1
        return max(longest_streak, curr_streak)
        

        