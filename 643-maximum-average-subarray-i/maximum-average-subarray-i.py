class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = 0
        max_avg =0
        for i in range(k):
           sum += nums[i] 
        max_avg = sum
        for i in range (k,len(nums)):
            sum += nums[i] -nums[i-k]
            max_avg = max(sum,max_avg)
            
        return max_avg/float(k)