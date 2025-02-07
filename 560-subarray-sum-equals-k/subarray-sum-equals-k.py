class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        curr = 0
        prefixSum = {0:1}

        for n in nums:
            curr += n
            diff = curr -k 
            res += prefixSum.get(diff,0)
            prefixSum[curr] = 1 + prefixSum.get(curr,0)

        return res

        