class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        Job[] jobs = new Job[n];
        int[] memo = new int[n];

        for(int i = 0; i < startTime.length; i++){
            jobs[i] = new Job(startTime[i], endTime[i],profit[i]);
        }
        Arrays.sort(jobs,(a,b) -> a.startTime - b.startTime);
        
        //Uncomputed
        for(int i = 0; i < n; i++){
            memo[i] = -1;
        }

        return DFS(0,jobs, memo);
    }

    private class Job{
        int startTime;
        int endTime;
        int profit;

        public Job(int startTime, int endTime, int profit){
            this.profit = profit;
            this.startTime = startTime;
            this.endTime = endTime;
        }
    }

    private int DFS(int index, Job[] jobs, int[] memo){
        if(index>=jobs.length){
            return 0;
        }
        if(memo[index]!=-1){
            return memo[index];
        }
        int profitSkip = DFS(index+1, jobs, memo);
        int nextIndex = findNext(jobs, jobs[index].endTime);
        int profitTake = jobs[index].profit + DFS(nextIndex,jobs,memo);

        memo[index] = Math.max(profitSkip,profitTake);

        return memo[index];

    }

    private int findNext(Job[] jobs, int target){
        int low = 0; 
        int high = jobs.length;
        while(low < high){
            int mid = (low+high)/2;
            if(jobs[mid].startTime < target){
                low = mid+1;
            }
            else{
                high = mid;
            }
        }
        return low;
    
    }
}