# Definition for singly-linked list.
from typing import Union
import json

class ListNode():
    def __init__(self, val=0, next=None):
        self.val:int = val
        self.next:Union[ListNode,None] = next
        
    def toJson(self):
        return json.dumps(self, default=lambda o:o.__dict__)
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = l1.val + l2.val
        remain = val // 10
        floor = val % 10
        lns = [ListNode(floor)]
        while l1.next or l2.next or remain:
            if not l1.next:
                l1.next = ListNode()
            if not l2.next:
                l2.next = ListNode()
            val = l1.next.val + l2.next.val + remain
            remain = val // 10
            floor = val % 10
            ln = ListNode(floor)
            lns[-1].next = ln
            lns.append(ln)
            l1 = l1.next
            l2 = l2.next
        return lns[0]
    
if __name__ == "__main__":
    l1 = ListNode(2,ListNode(4,ListNode(3)))
    l2 = ListNode(5,ListNode(6,ListNode(4)))
    solution = Solution()
    out = solution.addTwoNumbers(l1, l2)
    print (out.toJson())
    l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
    l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9))))
    out = solution.addTwoNumbers(l1, l2)
    print (out.toJson())
