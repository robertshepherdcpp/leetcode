# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_arr = []
        l2_arr = []
        while l1 or l2:
            if not l1:
                while l2:
                    l2_arr.append(l2.val)
                    l2 = l2.next
            elif not l2:
                while l1:
                    l1_arr.append(l1.val)
                    l1 = l1.next
            else:
                l1_arr.append(l1.val)
                l1 = l1.next
                l2_arr.append(l2.val)
                l2 = l2.next
        l1_arr = l1_arr[::-1]
        l2_arr = l2_arr[::-1]

        l1_str = ''.join(str(i) for i in l1_arr)
        l2_str = ''.join(str(i) for i in l2_arr)

        val = int(l1_str) + int(l2_str)
        res = []
        for i in str(val):
            res.append(int(i))
        res = res[::-1]
        # convert to list.
        head = ListNode(res[0])
        dummy_head = head
        for i in range(1, len(res)):
            dummy_head.next = ListNode(res[i])
            dummy_head = dummy_head.next
        return head            
            

        
