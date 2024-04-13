class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = nums[0]
        i=0
        for i in range(1,len(nums)):
            if count==0:
                return False
            count -=1
            count = max(count,nums[i])
        return True