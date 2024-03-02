class Solution:
    def maximumOddBinaryNumber(self, s):
        string = sorted(s)
        res = ''
        for i in range(len(string)-2, -1, -1):
            res += string[i]
        res += string[-1]

        return res
        