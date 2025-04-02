class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        minScore = weights[0] + weights[-1]
        maxScore = weights[0] + weights[-1]

        n = len(weights)
        pairsum = [weights[i]+ weights[i+1] for i in range(n-1)]

        pairsum.sort()

        for i in range(k-1):
            minScore += pairsum[i]
            maxScore += pairsum[-1-i]

        return maxScore - minScore


        