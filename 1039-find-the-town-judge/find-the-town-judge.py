class Solution(object):
    def findJudge(self, n, trust):
        
        if n == 1:
            return 1 if not trust else -1

        trustCounts = [0] * (n + 1)
        trustedByCounts = [0] * (n + 1)

        for a, b in trust:
            trustCounts[a] += 1
            trustedByCounts[b] += 1

        for i in range(1, n + 1):
            if trustCounts[i] == 0 and trustedByCounts[i] == n - 1:
                return i

        return -1
