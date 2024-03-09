class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        pt1=0
        pt2=0
        min_num = 0

        while pt1<len(nums1) and pt2<len(nums2):
            if nums1[pt1]<nums2[pt2]:
                pt1+=1
            elif nums1[pt1]>nums2[pt2]:
                pt2+=1
            else:
                return nums1[pt1]
        
        return -1