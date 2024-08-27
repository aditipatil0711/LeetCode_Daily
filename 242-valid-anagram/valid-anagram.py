class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list(sorted(s))
        l2 = list(sorted(t))
        return l1 == l2