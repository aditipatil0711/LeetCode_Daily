class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_element = max(nums)
        indexes_of_max_elements = []
        ans = 0

        for i,e  in enumerate(nums):
            if e == max_element:
                indexes_of_max_elements.append(i)
            freq = len(indexes_of_max_elements)
            if freq >= k:
                ans += indexes_of_max_elements[-k] +1 
        return ans 