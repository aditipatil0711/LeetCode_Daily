class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer =[1]*length
        for i in range(1,length):
            answer[i] = nums[i-1]*answer[i-1]
        
        R =1
        for i in reversed(range(length)):
            answer[i] = answer[i]*R
            R*=nums[i]
        return answer        
        