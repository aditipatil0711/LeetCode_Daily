class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l =0
        r=1
        pr =0
        maxp =-1

        while r<len(nums):
            if nums[r]>nums[l]:
                pr = nums[r]-nums[l]
                maxp = max(maxp,pr)
            else:
                l=r
            r+=1
        return maxp
