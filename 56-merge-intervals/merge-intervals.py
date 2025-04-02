class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """


        intervals.sort(key=lambda x: x[0])

        mergedList = []

        for i in intervals:
            if not mergedList or i[0] > mergedList[-1][1]:
                mergedList.append(i)
            else:
                mergedList[-1][1] = max(mergedList[-1][1],i[1])
        
        return mergedList

        

        