class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        leftsum = 0
        for i in nums:
            sum += i

        for x in range(len(nums)):
            if(leftsum == sum - nums[x]-leftsum):
                return x
            leftsum += nums[x]
        
        return -1
        
        