class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ans1 =[]
        ans2 = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans1 = list(nums1-nums2)
        ans2 = list(nums2-nums1)
    
        
        return [ans1,ans2]

        