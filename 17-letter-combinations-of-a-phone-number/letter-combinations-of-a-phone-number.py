class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic={
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        res=[]
        for i in range(len(digits)):
            if len(res)==0:
                res=''.join(dic[digits[i]])
            else:
                temp=[]
                for j in range(len(res)):
                    temp2=dic[digits[i]]
                    for k in range(len(temp2)):
                        # print(res[j],temp2[k])
                        temp.append(res[j]+temp2[k])
                res=temp
        return res