class Solution(object):
    def countSubarrays(self, nums, mink, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        res = 0
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                bad_idx = i

            if num == mink:
                left_idx = i

            if num == maxK:
                right_idx = i

            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res