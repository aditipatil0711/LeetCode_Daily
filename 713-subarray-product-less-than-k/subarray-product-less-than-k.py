class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left,right = 0,0
        product,count = 1,0
        while right<len(nums):
            product*=nums[right]
            right+=1
            while left<right and product >=k:
                product/=nums[left]
                left+=1
            count+=(right-left)
        return count
        