class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump=0
        end = 0
        far = 0
        for i in range(len(nums)-1):
            far = max(far,i+nums[i])
            if i==end:
                jump +=1
                end = far
                if end>=(len(nums)-1):
                    break
        return jump
