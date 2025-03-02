class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """

        heap1 = []
        heap2 = []

        n = len(costs)

        l = 0
        r = n-1

        for i in range(min(candidates, n)):
            heapq.heappush(heap1, (costs[i], i))
            l +=1
        
        for i in range(max(l,n-candidates),n):
            heapq.heappush(heap2, (costs[i],i))
            r -= 1

        total_cost = 0

        for _ in range(k):
            if heap1 and heap2:
                if heap1[0] <= heap2[0]:
                    cost, index = heapq.heappop(heap1)
                    if l <= r:
                        heapq.heappush(heap1, (costs[l],l))
                        l += 1
                else:
                    cost, index = heapq.heappop(heap2)
                    if l <= r:
                        heapq.heappush(heap2, (costs[r],r))
                        r -= 1

            elif heap1:
                cost, index = heapq.heappop(heap1)
            else:
                cost, index = heapq.heappop(heap2)

            total_cost  += cost
        
        return total_cost


        