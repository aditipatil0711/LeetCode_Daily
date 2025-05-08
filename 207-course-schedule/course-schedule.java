class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
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

        for(int i = 0; i< numCourses; i++){
            if(dfsHasCycle(i, graph, visited)){
                return false;
            }
        }
        
        return true;
        
    }

    private boolean dfsHasCycle(int i, List<List<Integer>> graph, int[] visited){
        if(visited[i] == 1) return true;
        if(visited[i] ==2 ) return false;

        visited[i] = 1;
        for(int neighbor: graph.get(i)){
            if(dfsHasCycle(neighbor, graph, visited)){
                return true;
            }
        }

        visited[i] =2 ;
        return false;
    }




}