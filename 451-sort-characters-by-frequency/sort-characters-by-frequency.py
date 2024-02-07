class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        m=list(set(s))
        s=list(s)
        a=[]
        b=[]
        for i in m:
            n=s.count(i)
            a.append(n)
            b.append(i)
        c=list(zip(a,b))
        c.sort(reverse=True)
        d=""
        for i in c:
            for x in range(i[0]):
                    d+=i[1]
        return d