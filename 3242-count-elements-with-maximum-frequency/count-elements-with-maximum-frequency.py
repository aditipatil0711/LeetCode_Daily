class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] =1
        
        max_f =0
        for f in freq.values():
            max_f = max(max_f,f)

        result = 0
        for f in freq.values():
            if f == max_f:
                result +=f

        return result

        