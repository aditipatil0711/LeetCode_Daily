class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        maxp=0

        while r<len(prices):
            if prices[l]>prices[r]:
               l+=1
            else:
                pr = prices[r]-prices[l]
                if maxp<pr:
                    maxp = max(pr,maxp)
                r+=1
        return maxp
        