class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        i=0
        for i,v in enumerate(nums):
            if v!=0:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1

        return nums        
            


        