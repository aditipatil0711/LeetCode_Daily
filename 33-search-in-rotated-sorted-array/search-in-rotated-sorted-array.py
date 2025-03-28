class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l,r = 0, n-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid -1 

        # mid = pivot index:
        def helper(left_boundary, right_boundary,target):
            l,r = left_boundary, right_boundary
            while l <= r:
                mid = (l+r) //2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        answer = helper(0, l - 1, target)
        if answer != -1:
            return answer

        # Binary search over elements on the pivot element's right
        return helper(l, n - 1, target)


        