class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = sum(nums[::2])
        s2 = sum(nums[1::2])

        count = 0
        t1 = 0
        t2 = 0

        for i, v in enumerate(nums):
            if i%2 == 0:
                is_fair = (t2 + s1 - t1 - v == t1 +s2 - t2)
                count += is_fair
            else:
                is_fair = (t1 + s2 - t2 - v== t2 + s1 - t1)
                count += is_fair
        
            if i%2 == 0:
                t1 += v
            else:
                t2 += v
        return count

