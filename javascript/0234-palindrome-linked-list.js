/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
    // Time: O(n)
    // Space: O(1)

    // find midpoint
    let fast = head;
    let slow = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // reverse one side
    let prev = null;
    while (slow) {
        let temp = slow.next;
        slow.next = prev;

        prev = slow;
        slow = temp;
    }

    // compare if palindrome
    while (prev) {
        if (prev.val != head.val) {
            return false;
        }

        prev = prev.next;
        head = head.next;
    }

    return true;
};
