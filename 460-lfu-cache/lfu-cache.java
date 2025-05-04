class LFUCache {
    private Map<Integer,Pair<Integer, Integer>> cache;
    private Map<Integer,LinkedHashSet<Integer>> freqs;
    private int minF;
    private int capacity;


    private void insert(int key, int freq, int value){
        cache.put(key, new Pair<>(freq, value));
        freqs.putIfAbsent(freq,new LinkedHashSet<>());
        freqs.get(freq).add(key);
    } 

    public LFUCache(int capacity) {
        cache = new HashMap<>();
        freqs = new HashMap<>();
        minF = 0;
        this.capacity = capacity;
    }
    
    public int get(int key) {
        Pair<Integer,Integer> freqandValue = cache.get(key);
        if(freqandValue == null){
            return -1;
        }
        int freq = freqandValue.getKey();
        Set<Integer> keys = freqs.get(freq);
        keys.remove(key);

        if(keys.isEmpty()){
            freqs.remove(freq);
            if(minF == freq){
                ++minF;
            }
        }

        int value = freqandValue.getValue();
        insert(key,freq+1,value);
        return value;
        
    }
    
    public void put(int key, int value) {
        Pair<Integer,Integer> freqandValue = cache.get(key);
        if(freqandValue != null){
            cache.put(key, new Pair<>(freqandValue.getKey(), value));
            get(key);
            return;
        }
        if (capacity == cache.size()) {
            final Set<Integer> keys = freqs.get(minF);
            final int keyToDelete = keys.iterator().next();
            cache.remove(keyToDelete);
            keys.remove(keyToDelete);
            if (keys.isEmpty()) {
                freqs.remove(minF);
            }
        }
        minF = 1;
        insert(key, 1, value);
        
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */