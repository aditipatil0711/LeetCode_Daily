class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(","[","{"]:
                stack.append(i)
            elif i == ')' and len(stack)!=0 and stack[-1]=="(" :
                stack.pop()
            elif i == ']' and len(stack)!=0 and stack[-1]=="[" :
                stack.pop()
            elif i == '}' and len(stack)!=0 and stack[-1]=="{" :
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        return False

        