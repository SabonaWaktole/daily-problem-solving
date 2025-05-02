# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = ListNode()
        retnode = node
        candidates = []
        available = True
        while available:
            k = 0
            for i in range(len(lists)):
                head = lists[i]
                if head:
                    heappush(candidates, head.val)
                    head = head.next
                    lists[i] = head
                    k += 1

            if not k:
                available = False
            if candidates:
                tail = ListNode()
                tail.val = heappop(candidates)
                retnode.next = tail
                retnode = retnode.next

        while candidates:
            tail = ListNode()
            tail.val = heappop(candidates)
            retnode.next = tail
            retnode = retnode.next
        return node.next