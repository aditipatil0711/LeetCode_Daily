class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        # start at City 0
        # recursively check neighbors
        # count outgoing edges

        edges = {(a, b) for a, b in connections}  # Stores direct edges (directed)
        neighbors = {city: [] for city in range(n)}  # Adjacency list
        visit = set()  # Keeps track of visited nodes
        changes = 0  # Count of roads to be reversed

        for a, b in connections:
            neighbors[a].append(b)  # Forward connection
            neighbors[b].append(a)  # Backward connection for traversal

        def dfs(city):
            nonlocal changes

            for n in neighbors[city]:  # Iterate over neighboring cities
                if n in visit:  # If already visited, skip
                    continue
                if (n, city) not in edges:  # If the edge does not exist in the original direction, it needs reversal
                    changes += 1
                visit.add(n)
                dfs(n)

        visit.add(0)  # Start from city 0
        dfs(0)
        return changes
