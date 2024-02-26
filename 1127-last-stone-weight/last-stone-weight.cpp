class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq(stones.begin(), stones.end());
        // Makes it a maxheap

        while(pq.size()>1){
            int stone1 = pq.top();
            pq.pop();
            int stone2 = pq.top();
            pq.pop();

            if(stone1 != stone2){
                pq.push(abs(stone1-stone2));
            }

           

        }
         return pq.empty() ? 0 : pq.top();
    }
    
        
    
};