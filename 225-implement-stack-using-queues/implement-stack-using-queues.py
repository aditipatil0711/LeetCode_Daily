class MyStack(object):

    def __init__(self):
        self.q = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        for _ in range(len(self.q)-1):
            val = self.q.popleft()
            self.q.append(val)

    def pop(self):
        """
        :rtype: int
        """
        return self.q.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()