
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l=ListNode()
        L=l
        residual=0
        while l1 and l2:
            temp=l1.val+l2.val+residual
            if temp >=10:
                temp-=10
                residual=1
            else:
                residual=0
            l1=l1.next
            l2=l2.next
            l.next=ListNode(temp)
            l=l.next
        while l1:
            temp=l1.val+residual
            if temp >=10:
                temp-=10
                residual=1
            else:
                residual=0
            l1=l1.next
            l.next=ListNode(temp)
            l=l.next
        while l2:
            temp=l2.val+residual
            if temp >=10:
                temp-=10
                residual=1
            else:
                residual=0
            l2=l2.next
            l.next=ListNode(temp)
            l=l.next
        if residual==1:
            l.next=ListNode(1)
        return L.next
if __name__=='__main__':
    L=ListNode()
    s=L
    temp=ListNode(10)
    L.val=temp.val
    L.next=ListNode()
    temp=ListNode(20)
    L.val=temp.val
    L.next=ListNode()
    temp=ListNode(30)
    L.val=temp.val
    print(s.val)

        