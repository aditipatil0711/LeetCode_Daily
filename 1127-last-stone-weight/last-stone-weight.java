class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b)-> b-a);
        for(int s: stones){
            maxHeap.offer(s);
        }
        while(maxHeap.size()>1){
            int s1 = maxHeap.poll();
            int s2 = maxHeap.poll();
            if(s1!=s2){
                maxHeap.offer(s1-s2);
            }
        }
        return maxHeap.isEmpty()?0:maxHeap.peek();
    }
}