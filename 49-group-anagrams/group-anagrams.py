class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashtable = {}

        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word not in hashtable:
                hashtable[sorted_word] = []
            
            hashtable[sorted_word].append(i)
        return list(hashtable.values())
        

        