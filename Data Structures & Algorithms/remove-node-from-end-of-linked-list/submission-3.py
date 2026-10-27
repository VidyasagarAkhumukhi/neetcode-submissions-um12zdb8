# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        right = head
        left = dummy

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
    



        # bruteforce
        # res = []
        # curr = head

        # while curr:
        #     res.append(curr)
        #     curr = curr.next

        # removeIndex = len(res) - n

        # if removeIndex == 0:
        #     return head.next
        
        # res[removeIndex - 1].next = res[removeIndex].next

        # return head