class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
    
        pq = [(-count, char) for char,count in Counter(s).items()]
        heapify(pq)

        while pq:
            count1, char1 = heappop(pq)
            if not ans or char1 != ans[-1]:
                ans.append(char1)
                if count1 + 1 != 0:
                    heappush(pq, (count1+1, char1))
            else:
                if not pq: return ''
                count2, char2 = heappop(pq)
                ans.append(char2)
                if count2 + 1 != 0:
                    heappush(pq, (count2+1,char2))
                heappush(pq, (count1, char1))
        return ''.join(ans)
                




        