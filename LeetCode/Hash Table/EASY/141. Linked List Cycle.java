/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solutaion {
    public boolean hasCycle(ListNode head) {
        if(head == null) return false;

        Set<ListNode> data = new HashSet<>();
        while(true){
            if(head == null) return false;
            if(data.contains(head)){
                return true;
            }
            data.add(head);
            head = head.next;
        }
        return false;
    }

}