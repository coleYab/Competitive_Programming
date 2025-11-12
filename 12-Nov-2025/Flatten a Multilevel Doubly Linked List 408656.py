# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        root = Node(head.val, None, None, None)
        # root.val = head.val
        if head.child:
            print("the head is: ", head.val)
            nxt = self.flatten(head.child)
            nxt.prev = root
            root.next = nxt
        
        cur = root
        while cur.next:
            cur = cur.next
    
        if head.next:
            nxt = self.flatten(head.next)
            nxt.prev = cur
            cur.next = nxt

        return root