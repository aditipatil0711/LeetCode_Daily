class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = mins= curr =nums[0]
        for i in nums[1:]:
            tempmax, tempmin = maxs,mins
            maxs = max(i, tempmax*i,tempmin*i)
            mins = min(i,tempmax*i, tempmin*i)
            curr = max(curr,maxs)
        return curr

            