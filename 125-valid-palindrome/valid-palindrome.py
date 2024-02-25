class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        
        i = 0
        j = len(s)-1
        while i<j:
            #skip the characters
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum(): 
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1


        return True
        """
        s=s.lower()
        pattern =r'[^a-z0-9]+'
        a = re.sub(pattern,'',s)
        
        if(a[::-1]==a):
            return True
        else:
            return False
        