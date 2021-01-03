class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:#判断不是空链表
            return head
        nummy = None#设置一个尾节点为空
        while head:
            temp = head.next
            head.next = nummy
            nummy = head
            head = temp
        return nummy