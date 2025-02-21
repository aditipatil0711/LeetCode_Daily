class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
       
        def buildAGraph(equations, values, graph):
            
            for eq, val in zip(equations, values):
                a,b  = eq

                if a not in graph:
                    graph[a] = {}
                if b not in graph:
                    graph[b] = {}

                graph[a][b] = val
                graph[b][a] = 1/val
            return graph

        def dfs(start, end, graph, visited ):
            print(start , end ,visited)
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for n in graph[start]:
                if n not in visited:
                    res = dfs(n,end, graph,visited)
                    if res != -1.0:
                        return res*graph[start][n]
                
            return -1.0

        graph = {}
        graph  = buildAGraph(equations, values, graph)
        print(graph)
        res = []
        for q in queries:
            start, end = q
            # calculate values from hashset by for
            res.append(dfs(start, end, graph, set())) 
        return res



