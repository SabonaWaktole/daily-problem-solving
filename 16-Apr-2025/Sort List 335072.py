# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_middle(head):
            slow, fast = head, head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow

        def merge(list1, list2):
            dummy = ListNode()
            current = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next

            current.next = list1 if list1 else list2
            return dummy.next
        def mergeSort(head):
            if not head or not head.next:
                return head
            middle = find_middle(head)
            left = mergeSort(head)
            right = mergeSort(middle)
            return merge(left, right)

        return mergeSort(head)
            
            


        