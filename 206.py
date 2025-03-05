# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr != None:
            print(curr.val)
            if prev == None:
                cpy = curr.next
                prev = curr
                curr.next = None
                curr = cpy
            else:
                cpy = curr.next
                curr.next = prev
                prev = curr
                curr = cpy
        print("out of while")
        return prev

        
