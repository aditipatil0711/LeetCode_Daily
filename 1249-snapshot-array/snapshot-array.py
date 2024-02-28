

class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.array = [[[0,0]] for _ in range(length)]
        self.snap_count = 0

        

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.array[index].append([self.snap_count,val])

        

    def snap(self):
        """
        :rtype: int
        """
        self.snap_count +=1
        return self.snap_count-1
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        snap_index=  bisect.bisect_right(self.array[index], [snap_id, 10 ** 9])
        return self.array[index][snap_index - 1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)