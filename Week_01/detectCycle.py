class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        a = set() #思路是直接定义一个指针，如果有环则该指针第一个重复的点即为入环点
        l1 = head
        while l1:
            if l1 in a:
                return l1
            a.add(l1)
            l1 = l1.next
        return None