class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int, int> um;
        int i =0, j = 0, n = nums.size(), maxLen = 0;
        while(j<n){
            um[nums[j]]++;
            while(i<j && um[nums[j]]>k){
                um[nums[i]]--;
                i++;
            }
            maxLen = max(maxLen, j-i+1);
            j++;
        }
        return maxLen;
    }
};