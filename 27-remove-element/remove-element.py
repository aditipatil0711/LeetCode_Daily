class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        n = len(nums)

        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i