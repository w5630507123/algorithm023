class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        temp = ListNode(0)
        temp.next = head
        dummy = temp
        while dummy.next and dummy.next.next:
            node_1 = dummy.next
            node_2 = dummy.next.next
            dummy.next = node_2
            node_1.next = node_2.next
            node_2.next = node_1
            dummy = node_1
        return temp.next