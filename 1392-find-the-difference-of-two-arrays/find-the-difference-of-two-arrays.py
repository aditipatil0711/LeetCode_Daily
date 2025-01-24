class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ans1 =[]
        ans2 = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                ans1.append(nums1[i])
            
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                ans2.append(nums2[i])
        
        return [ans1,ans2]

        