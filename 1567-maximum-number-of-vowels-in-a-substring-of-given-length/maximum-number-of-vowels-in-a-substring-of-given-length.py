class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        vowels = {'a','e','i','o','u'}
        #Create First Window
        for i in range(k):
            if s[i] in vowels:
                count +=1
        #Max Count found so far or in first window creation
        max_count = count

        # Now calculate in sliding manner
        for i in range(k,len(s)):
            #Add next element and check if it fits the count for vowels
            if s[i] in vowels:
                count +=1
            #Remove the last element and if it is a vowel you will end up missing, reduce the count
            if s[i-k] in vowels:
                count -=1
            max_count = max(max_count,count)
        return max_count
        