class Solution(object):
    def jump(self, nums):
        # Initial conditions
        n = len(nums)
        if n <= 1:
            return 0  # No jumps needed if there's only one element
        
        jumps = 0
        current_end = 0
        farthest = 0
        # Loop through each index in the array except the last one
        for i in range(n):
            # Update the farthest point that can be reached
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the array, return the jumps
            if farthest >= n - 1:
                return jumps + 1
            
            # If we reach the end of the range we can currently jump to
            if i == current_end:
                # We need to make another jump
                jumps += 1
                # Move the end to the farthest point we can currently reach
                current_end = farthest

            # This condition happens when the current index is beyond the farthest reach
            # (it's an edge case that theoretically won't happen in this problem because
            # it's guaranteed that the end is always reachable)
            if i == farthest:
                break  # Can't go further; though, this line should never be executed due to problem constraints

        return jumps  # This return is theoretical and should not be needed
