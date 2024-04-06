class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        remove = set()
        stack =[]
        for i,c in enumerate(s):
            if c not in '()':
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                remove.add(i)
            else:
                stack.pop()
        
        remove = remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in remove:
                string_builder.append(c)
        return "".join(string_builder)
        