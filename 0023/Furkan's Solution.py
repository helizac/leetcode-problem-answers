# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        l = []
        for i in lists:
            while i:
                l.append(i.val)
                i = i.next
        l.sort()
        
        if len(l) == 0:
            return ListNode().next
        
        
        head = ListNode(l[0])
        tail = head
        
        e = 1
        while e < len(l):
            tail.next = ListNode(l[e])
            tail = tail.next
            e+=1

        return(head)
