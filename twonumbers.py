# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        st1 = ""
        st2 = ""
        curnode = l1
        while curnode != None:
            st1 += str(curnode.val)
            curnode = curnode.next
        curnode = l2
        while curnode != None:
            st2 += str(curnode.val)
            curnode = curnode.next
        st1 = st1[::-1]
        st2 = st2[::-1]
        ans = int(st1) + int(st2)
        ans = str(ans)
        ans = ans[::-1]
        l3 = ListNode(int(ans[0]))
        prevnode = l3
        for i in ans[1:]:
            curnode = ListNode(int(ans[i]))
            prevnode.next = curnode
            prevnode = curnode
        return l3
