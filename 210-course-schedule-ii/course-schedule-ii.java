class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        
        List<List<Integer>> graph = new ArrayList<>();
        
        //Create space in the list
        for(int i = 0; i< numCourses; i++){
            graph.add(new ArrayList<>());
        }

        //Add values to create edges
        for(int[] pair: prerequisites){
            graph.get(pair[1]).add(pair[0]);
        }

        int[] visited = new int[numCourses];
        List<Integer> order = new ArrayList<>();


        for(int i = 0; i< numCourses; i++){
            if(dfsHasCycle(i, graph, visited, order)){
                return new int[0];
            }
        }

        Collections.reverse(order);

        int[] result = new int[numCourses];
        for(int i = 0; i < numCourses; i++) {
            result[i] = order.get(i);
        }

        return result;
        
    }

    private boolean dfsHasCycle(int i, List<List<Integer>> graph, int[] visited, List<Integer> order){
        if(visited[i] == 1) return true;
        if(visited[i] ==2 ) return false;

        visited[i] = 1;
        for(int neighbor: graph.get(i)){
            if(dfsHasCycle(neighbor, graph, visited, order)){
                return true;
            }
        }

        visited[i] =2 ;
        order.add(i);
        return false;
    }
}