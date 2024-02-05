class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = defaultdict(int)
        n = len(s)

        for j,v in enumerate(s):
            map[v] += 1

        for i,v in enumerate(s):
            if map[v] == 1:
                return i
        return -1 
