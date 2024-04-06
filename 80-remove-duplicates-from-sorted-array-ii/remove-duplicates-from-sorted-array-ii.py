class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        i = 1


        while (i<len(nums)):
            if nums[i] == nums[i-1]:
                counter +=1
                if counter >2:
                    nums.pop(i)
                    i-=1
            else:
                counter = 1
            i+=1
        return i

