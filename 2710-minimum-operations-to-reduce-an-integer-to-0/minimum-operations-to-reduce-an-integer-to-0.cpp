class Solution {
public:
    int minOperations(int n) {
        
        int carry = 0;
        int result = 0;
        while(n>0){
            if (n&1){
                carry++;
            }
            else if(carry >0){
                result++;
                carry = carry == 1 ? 0 :1;
            }
            n>>=1;
        }

        if(carry ==1){
            result++;
        }else if (carry > 1){
            result +=2;
        }
        return result;
    }
};