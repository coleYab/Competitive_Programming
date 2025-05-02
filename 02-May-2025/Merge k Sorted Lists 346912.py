# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = ListNode()
        cur = head
        for node in lists:
            while cur.next:
                cur = cur.next 
            cur.next = node

        if not head.next:
            return None
        
        def mid_of(head):
            dummy = ListNode(0, head)
            fast, slow = dummy, dummy
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            return slow

        def merge(left, right):
            head = ListNode(0)
            cur = head
            while left or right:
                if left and ((not right ) or left.val <= right.val):
                    cur.next = ListNode(left.val)
                    left = left.next
                else:
                    cur.next =ListNode(right.val)
                    right = right.next
                cur = cur.next
            return head.next

        def divide(head):
            if not (head and head.next):
                return head

            mid = mid_of(head)
            right = mid.next
            mid.next = None
            left = head
            l_ans = divide(left)
            r_ans = divide(right)

            return merge(l_ans, r_ans)
        
        return divide(head.next)