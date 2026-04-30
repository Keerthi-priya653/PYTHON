using System;

class Solution
{
    public bool isPalindrome(Node head)
    {
        if (head == null || head.next == null)
            return true;

        Node slow = head;
        Node fast = head;

        // Step 1: Find middle
        while (fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse second half
        Node prev = null;
        Node curr = slow;

        while (curr != null)
        {
            Node next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // Step 3: Compare both halves
        Node first = head;
        Node second = prev;

        while (second != null)
        {
            if (first.data != second.data)
                return false;

            first = first.next;
            second = second.next;
        }

        return true;
    }
}
