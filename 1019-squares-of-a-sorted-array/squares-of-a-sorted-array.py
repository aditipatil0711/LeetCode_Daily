class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = []
        for num in nums:
            array.append(num**2)
        
        array.sort()
        return array
        