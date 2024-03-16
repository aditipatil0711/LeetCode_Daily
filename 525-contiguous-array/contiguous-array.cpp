class Solution {
public:
    int findMaxLength(vector<int>& arr) {
        int n = arr.size();
        for(int i = 0; i<n; i++){
            if(arr[i]==0)arr[i]=-1;
        }
        unordered_map<int,int>mp;
        int mx=0; 
        mp[0]=-1;
        int sum =0;
        for(int i = 0 ; i<n ; i++){
            sum += arr[i];
            if(mp.find(sum)!=mp.end()){
                int a= i-mp[sum];
                mx = max(mx ,a);
            }
            else mp[sum] = i;
        }
        return mx;        
    }
};