/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {

        ListNode temp = new ListNode(0);
        ListNode current = temp;

        PriorityQueue<ListNode> pq = new PriorityQueue<>((ListNode a, ListNode b) -> a.val - b.val);

        for (ListNode head : lists){
            if (head != null){
                pq.add(head);
            }
        }

        while (!pq.isEmpty()){
            ListNode smallest = pq.poll();

            current.next = smallest;
            current = current.next; //Moving the current pointer

            if(smallest.next != null){
                pq.add(smallest.next);
            }
        }

        return temp.next;
        
    }
}