# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        firstPointer = head
        secondPointer = head
        for i in xrange(0, n):
            secondPointer = secondPointer.next
            
        if secondPointer is None:
            temp = firstPointer.next
            del firstPointer
            return temp
            
        while secondPointer.next != None:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
            
        temp = firstPointer.next
        firstPointer.next = firstPointer.next.next
        del temp

        return head