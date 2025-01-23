class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max1s = 0
        num0s= 0
        n = len(nums)
        l =0
        for r in range(n):
            if nums[r] == 0:
                num0s += 1
            while num0s>k:
                if nums[l] == 0:
                    num0s -= 1
                l+=1
            w = r-l+1
            max1s = max(max1s,w)
        return max1s

        