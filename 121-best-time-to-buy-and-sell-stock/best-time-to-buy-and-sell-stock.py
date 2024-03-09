class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l= 0 
        r = 0
        maxp =0

        while r<len(prices):
            if prices[l]<prices[r]:
                pr = prices[r]-prices[l]
                maxp = max(pr,maxp)
            else:
                l=r
            r+=1

        return maxp
        



        
        