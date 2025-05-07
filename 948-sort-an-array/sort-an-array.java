class Solution {
    public int[] sortArray(int[] nums) { 
    int l = 0;
    int r = nums.length -1;   
    mergeSort(nums, l, r);
    return nums;
    }

    private void mergeSort(int[] nums, int l, int r){
        if(l>=r){
        return;
        }
        int m  = (l+r)/2;
        mergeSort(nums,l,m);
        mergeSort(nums,m+1,r);
        merge(nums, l, m, r);
        //merge
    }

    private void merge(int[] nums, int p, int q, int r){
        int n1 = q-p+1;
        int n2 = r-q;

        int L[] = new int[n1];
        int M[] = new int[n2];

        for(int i = 0; i < n1; i++)
        {L[i] = nums[p + i];}
        for(int j = 0; j < n2; j++){
            M[j] = nums[q+1+j];
        }

        int i, j, k;
        i = 0;
        j = 0;
        k = p;

        while(i<n1 && j<n2){
            if(L[i]<=M[j]){
                nums[k] = L[i];
                k++;
                i++;
            }
            else{
                nums[k] = M[j];
                j++;
                k++;
            }
        }

        while(i<n1){
            nums[k] = L[i];
            i++;
            k++;
        }

        while(j<n2){
        nums[k] = M[j];
        j++;
        k++;
        }
            

    }
    
}