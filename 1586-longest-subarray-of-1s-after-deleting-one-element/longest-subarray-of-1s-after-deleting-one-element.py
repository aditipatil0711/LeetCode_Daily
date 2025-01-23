class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        zero_count = 0
        max_length = 0
        for end in range(len(nums)):
            if nums[end]==0:
                zero_count+=1
            while zero_count>1:
                if nums[start] == 0:
                    zero_count-=1
                start+=1
            max_length = max(max_length,end-start)
        return max_length
        