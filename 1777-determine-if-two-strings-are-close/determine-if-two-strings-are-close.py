class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # if the len
        if (len(word1) != len(word2)):
            return False
        wordMap1 = {}
        wordMap2 = {}

        for c in word1:
            wordMap1[c] = wordMap1.get(c, 0) + 1

        for c in word2:
            wordMap2[c] = wordMap2.get(c,0) + 1

        if set(wordMap1.keys()) != set(wordMap2.keys()):
            return False
        
        word1_frequency_list = sorted(wordMap1.values())
        word2_frequency_list = sorted(wordMap2.values())
        
        return word1_frequency_list == word2_frequency_list


        
