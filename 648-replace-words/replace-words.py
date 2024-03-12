class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        dictionary.sort(key = len)
        words = sentence.split(" ")

        for i, word in enumerate(words):
            for j in dictionary:
                if word.startswith(j) :
                    words[i] = j
                    break 
        return " ".join(words)