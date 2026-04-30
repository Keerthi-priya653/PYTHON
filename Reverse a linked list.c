using System;

class Solution
{
    public Node reverseList(Node head)
    {
        Node prev = null;
        Node curr = head;

        while (curr != null)
        {
            Node next = curr.next; // store next
            curr.next = prev;      // reverse link
            prev = curr;           // move prev
            curr = next;           // move curr
        }

        return prev; // new head
    }
}
