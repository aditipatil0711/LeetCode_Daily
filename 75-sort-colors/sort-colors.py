class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        curr = p0 =0
        p1 = len(nums)-1

        while curr<= p1:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr],nums[p0]
                curr+=1
                p0 +=1
            elif nums[curr] ==2:
                nums[p1], nums[curr] = nums[curr],nums[p1]
                p1-=1
            else:
                curr +=1
