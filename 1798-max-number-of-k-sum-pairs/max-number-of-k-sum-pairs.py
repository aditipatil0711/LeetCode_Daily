class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        operations = 0
        l = 0
        r = len(nums)-1
        nums.sort()
        while l<r:
            if(nums[l]+nums[r]<k):
                l+=1
            elif (nums[l]+nums[r]>k):
                r-=1
            else:
                l+=1
                r-=1
                operations+=1
        return operations    


        