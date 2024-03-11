class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        char_count = Counter(s)
        sorted_chars = []
        for c in order:
            sorted_chars.append(c * char_count[c])
            char_count[c] = 0

        for c,count in char_count.items():
            sorted_chars.append(c*count)
        
        return ''.join(sorted_chars) 


