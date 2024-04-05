class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx=1
        n = len(nums)
        i=0

        for i in range(1,n):
            if (nums[i]!=nums[i-1]):
                nums[idx]=nums[i]
                idx+=1

        return idx
        