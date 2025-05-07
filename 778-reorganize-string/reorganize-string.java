class Solution {
    public String reorganizeString(String s) {
        int n = s.length();
        Map<Character, Integer> map = new HashMap<>();

        for(int i = 0; i<n; i++){
            char c = s.charAt(i);
            map.put(c,map.getOrDefault(c,0)+1);
        }

        for(int f:map.values()){
            if (f>(n+1)/2){
                return "";
            }
        }
        
        PriorityQueue<Map.Entry<Character,Integer>> pq = new PriorityQueue<>(
            (a,b) -> b.getValue() - a.getValue()
        );

        pq.addAll(map.entrySet());
        StringBuilder sb = new StringBuilder();

        while(pq.size() > 1){
            Map.Entry<Character,Integer> first = pq.poll();
            Map.Entry<Character,Integer> second = pq.poll();

            sb.append(first.getKey());
            sb.append(second.getKey());

            if(first.getValue()-1 > 0){
                first.setValue(first.getValue()-1);
                pq.offer(first);
            }

            if(second.getValue()-1 > 0){
                second.setValue(second.getValue()-1);
                pq.offer(second);
            }

        }

        if(!pq.isEmpty()){
            Map.Entry<Character,Integer> last = pq.poll();
            if(last.getValue() > 1){
                return "";
            }
            sb.append(last.getKey());

        }
        return sb.toString();
        
    }
}