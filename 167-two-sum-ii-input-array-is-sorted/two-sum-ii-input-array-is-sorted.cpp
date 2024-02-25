class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> ans;
        int i = 0;
        int j = numbers.size()-1;
        int sum = 0;
        
        while (i<j){
            int sum = numbers.at(i) +numbers.at(j);

            if (sum > target){
                j--;
            }
            else if ( sum < target){
                i++;
            }
            else {
                return {i+1,j+1};
            }
        }
        return {-1,-1};

    }
};