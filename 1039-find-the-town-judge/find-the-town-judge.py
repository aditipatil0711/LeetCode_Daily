class Solution(object):
    def findJudge(self, n, trust):
        
        if n == 1:
            return 1 if not trust else -1
    
        trusts = {}
        isTrustedBy = {}

        for a, b in trust:
            trusts[a] = trusts.get(a, 0) + 1
            isTrustedBy[b] = isTrustedBy.get(b, 0) + 1

        for person in range(1, n + 1):
            if trusts.get(person, 0) == 0 and isTrustedBy.get(person, 0) == n - 1:
                return person

        return -1
