class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            c =  target-nums[i]
            if c in dict1:
                return [i,dict1[c]]
            dict1[nums[i]] = i
        