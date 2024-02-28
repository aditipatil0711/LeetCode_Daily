class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_even_index, sum_odd_index = sum(nums[::2]), sum(nums[1::2])
      
        # Initialize counters for the number of ways to make the array fair,
        # the running sum of elements at even indices, and odd indices
        fair_ways_count = running_sum_even = running_sum_odd = 0
      
        # Enumerate over the list to consider removing each element in turn
        for index, value in enumerate(nums):
            # If the current index is even, check if removing the element makes the array fair
            if index % 2 == 0:
                # A fair array has equal sum of remaining elements at even and odd positions
                is_fair_after_removal = (running_sum_odd + sum_even_index - running_sum_even - value ==
                                         running_sum_even + sum_odd_index - running_sum_odd)
                # If fair, increment the fair ways count
                fair_ways_count += is_fair_after_removal
            else:
                # If the current index is odd, perform a similar check after removing the element
                is_fair_after_removal = (running_sum_odd + sum_even_index - running_sum_even ==
                                         running_sum_even + sum_odd_index - running_sum_odd - value)
                fair_ways_count += is_fair_after_removal
          
            # Update the running sums for even and odd indices after considering each element
            if index % 2 == 0:
                running_sum_even += value
            else:
                running_sum_odd += value
      
        # Return the total number of ways the array can be made fair
        return fair_ways_count