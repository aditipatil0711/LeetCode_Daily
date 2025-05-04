class LRUCache {

    class Node{
        int key;
        int value;
        Node next;
        Node prev;

        public Node(int key, int value){
            this.key = key;
            this.value = value;
            next = null;
            prev = null;
        }
    }

    private Map<Integer, Node> map;
    private int capacity;
    private int key;
    private int value;
    private Node head;
    private Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<>();
        head = new  Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
         
    }
    private void remove(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void add(Node node){
    Node temp = tail.prev;
    temp.next = node;
    node.prev = temp;
    node.next = tail;
    tail.prev = node;
    }
    
    public int get(int key) {
        if (!map.containsKey(key)){
            return -1;
        }
        Node node = map.get(key);
        remove(node);
        add(node);
        return node.value;
        
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            Node old = map.get(key);
            remove(old);
        }

        Node newNode = new Node(key, value);
        map.put(key, newNode);
        add(newNode);

        if(map.size() > capacity){
            Node x = head.next;
            remove(x);
            map.remove(x.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */