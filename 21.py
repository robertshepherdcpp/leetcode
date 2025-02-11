# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy_head = curr = ListNode()
        while list1 or list2:
            if list1 == None:
                curr.next = list2
                list2, curr = list2.next, list2
            elif list2 == None:
                curr.next = list1
                list1, curr = list1.next, list1
            elif list1.val > list2.val:
                curr.next = list2
                list2, curr = list2.next, list2
            else:
                curr.next = list1
                list1, curr = list1.next, list1
        return dummy_head.next
