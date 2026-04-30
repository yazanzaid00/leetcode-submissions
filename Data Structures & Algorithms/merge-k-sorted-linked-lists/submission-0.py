# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        elif k == 1:
            return lists[0]
        elif k == 2:
            tail = dummy = ListNode(-1, None) # dummy.next is the head of our ready linked list
            cur_0 = lists[0]
            cur_1 = lists[1]
            while cur_0 and cur_1:
                if cur_0.val <= cur_1.val:
                    tail.next = cur_0
                    cur_0 = cur_0.next
                else:
                    tail.next = cur_1
                    cur_1 = cur_1.next
                tail = tail.next
            tail.next = cur_0 or cur_1
            return dummy.next
        else:
            k = len(lists)
            left = self.mergeKLists(lists[0:k//2])
            right = self.mergeKLists(lists[k//2: k])
            return self.mergeKLists([left, right])