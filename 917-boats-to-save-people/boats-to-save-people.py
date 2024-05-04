class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        ans = 0
        l,r = 0,len(people)-1
        people.sort()

        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
            ans+=1

        return ans
