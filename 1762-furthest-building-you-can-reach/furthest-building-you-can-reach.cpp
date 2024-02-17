class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int size = heights.size();
        priority_queue<int, vector<int>, greater<int>> pq;
        set<int> bjump;
        
        int i=0;
        while(i<size-1) {
            if(heights[i+1] > heights[i]){
                if(ladders > 0) {   //use up ladder if available
                    ladders--;
                    pq.push(heights[i+1] - heights[i]);
                } else if( (!pq.empty() && bricks >= pq.top()) ||  bricks >= (heights[i+1] - heights[i])) { //check if we have enough bricks to make the jump
                    if(!pq.empty() && pq.top() < (heights[i+1] - heights[i])) { //if we used a ladder for a smaller jump
                        bricks -= pq.top();
                        pq.pop();
                        pq.push(heights[i+1] - heights[i]);
                    } else {
                        bricks -= heights[i+1] - heights[i]; //correct place to use bricks                        
                    }
                } else { //we are out of resources
                    return i;
                }
            }
            i++;
        }
        
        
        return size-1; // we reach the last building
    }
};


