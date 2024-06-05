class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_size = len(words)
        result = []

        common_character_counts = collections.Counter(words[0])

        for i in range(1,word_size):
            current_character_counts = collections.Counter(words[i])
            for letter in common_character_counts.keys():
                common_character_counts[letter] = min(
                    common_character_counts[letter],
                    current_character_counts[letter]
                )

        for letter, count in common_character_counts.items():
            for _ in range(count):
                result.append(letter)

        return result