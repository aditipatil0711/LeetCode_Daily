class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_num=0
        current_string =""

        for a in s:
            if a.isdigit():
                current_num = current_num *10 +int(a)
            elif a == '[':
                stack.append((current_string,current_num))
                current_string = ""
                current_num = 0
            elif a =="]":
                prev_string,num = stack.pop()
                current_string = prev_string + num*current_string
            else:
                current_string += a

        return current_string
            
            

            
        