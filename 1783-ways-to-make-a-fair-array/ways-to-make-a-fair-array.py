class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_even = sum(nums[::2])
        sum_odd = sum(nums[1::2])

        count = 0
        t_even = 0
        t_odd = 0

        for i, value in enumerate(nums):
            if i%2 == 0:
                is_fair = t_odd + sum_even - t_even - value == t_even +sum_odd - t_odd
                count += is_fair
            else:
                is_fair = t_odd + sum_even - t_even == t_even +sum_odd - t_odd - value
                count += is_fair
        
            if i%2 == 0:
                t_even += value
            else:
                t_odd+= value
        return count

