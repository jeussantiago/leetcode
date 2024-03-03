/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
    /**
     * Time: O(n)
     * Space: O(1)
     */

    let dummy_head = new ListNode(0, head);
    let prev = dummy_head;
    let forw = head;

    while (forw) {
        forw = forw.next;
        if (n != 0) {
            n -= 1;
        } else {
            prev = prev.next;
        }
    }

    prev.next = prev.next.next;
    return dummy_head.next;
};
