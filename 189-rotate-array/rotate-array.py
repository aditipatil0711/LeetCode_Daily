class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)
        
        nums[0:n] = reversed(nums[0:n])
        nums[0:k] = reversed(nums[0:k])
        nums[k:n] = reversed(nums[k:n])