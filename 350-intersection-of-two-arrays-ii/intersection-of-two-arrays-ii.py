class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = Counter(nums1)

        intersection = []
        for i in nums2:
            if n[i]>0:
                intersection.append(i)
                n[i]-=1
        return intersection

        