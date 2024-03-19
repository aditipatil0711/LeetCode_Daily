class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = Counter(tasks)
        
        # Since we want to avoid a situation where we have same tasks back to back
        # The most optimal way would be to try to do other tasks between two identical tasks
        # And so, the most optimal way is to try to do those tasks first that have the maximum frequency
        # Because in this way, we can avoid the case where at the end, we have all identical tasks left to do 
        # which would otherwise mean a lot of waiting time
        # We can use a Max Heap to pick the task with maximum frequency at any time
        maxHeap = []
        for task in freq: heappush(maxHeap, [-freq[task], task])
            
        # To keep track of the current time
        time = 0
        
        # Waiting Queue
        waitingQueue = deque()
            
        # While we have tasks to complete
        while maxHeap or waitingQueue:
            
            # If the maxHeap is empty
            # It means the task that can be taken up will be the one in front of the waitingQueue
            # And it can be taken up at time = waitingQueue[0][0]
            # So, update the time accordingly in this case
            if not maxHeap: time = waitingQueue[0][0]
            
            # If there are tasks in the waiting queue that can be taken up at this "time"
            # Put them back in the maxHeap
            while waitingQueue and waitingQueue[0][0] <= time: 
                task = waitingQueue.popleft()[1]
                heappush(maxHeap, [-freq[task], task])
                
            # What is the task on top of the maxHeap
            topTask = heappop(maxHeap)[1]
            
            # So, once we complete it, its frequency will reduce by 1
            freq[topTask] -= 1
            
            # If the frequency is not 0, it means there are still same tasks that we have to complete
            # But we cannot complete them unless we wait for "n" minutes
            # So, till then, let's put them in a waiting queue which has tasks placed by the least to most waiting time
            # The queue will have data about eack task and the time at which it can be taken up by the CPU
            if freq[topTask] > 0: waitingQueue.append([time + n + 1, topTask])
                
            # Update the time
            time += 1
            
        # Finally, return the time taken to complete all the tasks
        return time
        