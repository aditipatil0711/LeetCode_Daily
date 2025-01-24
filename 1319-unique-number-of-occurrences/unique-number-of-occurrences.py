class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        count = {}
        for num in arr:
            count[num] = count.get(num,0)+1
        
        counts = list(count.values())
        u_count = set(counts)

        return len(counts)==len(u_count)



        