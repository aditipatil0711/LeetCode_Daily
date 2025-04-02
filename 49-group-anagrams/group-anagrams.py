class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashtable = {}

        for i in strs:
            sortedword = ''.join(sorted(i))
            if sortedword not in hashtable:
                hashtable[sortedword] = []
            hashtable[sortedword].append(i)

        ans = list(hashtable.values())

        return ans

        
        