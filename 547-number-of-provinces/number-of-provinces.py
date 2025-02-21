class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(city):
            visited.add(city)
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        n = len(isConnected)
        visited = set()
        province_count = 0

        for city in range(n):
            if city not in visited:
                dfs(city)
                province_count +=1
        
        return province_count
        