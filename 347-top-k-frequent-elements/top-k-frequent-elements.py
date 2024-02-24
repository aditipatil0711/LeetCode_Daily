class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map1= {}
        ans = []
        for i in nums:
            if i in map1:
                map1[i] +=1
            else:
                map1[i]=1
        
        sorted_map = sorted(map1.items(),key=lambda x:x[1],reverse=True)
        for i in range(k):
            ans.append(sorted_map[i][0])
        return ans
