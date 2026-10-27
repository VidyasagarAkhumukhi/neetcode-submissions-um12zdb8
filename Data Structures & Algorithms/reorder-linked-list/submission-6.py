# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head:
            return 

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        first, second = head, prev
        
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        
        
        # brute force
        # if not head:
        #     return 

        # node = []
        # cur = head

        # while cur:
        #     node.append(cur)
        #     cur = cur.next

        # l, r = 0, len(node) - 1

        # while l < r:
        #     node[l].next = node[r]
        #     l += 1

        #     if l >= r:
        #         break
            
        #     node[r].next = node[l]
        #     r -= 1
        # node[l].next = None

        


        