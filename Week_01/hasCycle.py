class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        l1,l2 = head,head #思路是设置两个指针，以不同的速率行走，如果会相遇则有环，如果步幅较大的先到终点（能走通），则无环
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
            if l1 == l2:
                return True
        return False