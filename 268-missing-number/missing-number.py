class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = sum(nums)
        length = len(nums)
        total = length*(length+1)/2

        return total - sum1
        