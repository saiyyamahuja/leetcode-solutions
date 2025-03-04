"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        old_to_new = {}
        curr = head
        start = head
        # First pass: Create a new copy of each node and store in the hash map
        while curr:
            old_to_new[curr] = Node(x = curr.val, next = None, random = None)
            curr = curr.next
        
        # Second pass: Assign next and random pointers for each new node
        for old_node, new_node in old_to_new.items():
            if old_node.next:
                # Link the copied node to its corresponding next node
                next_node = old_to_new[old_node.next] 
                new_node.next = next_node
            if old_node.random:
                # Link the copied node to its corresponding random node
                random_node = old_to_new[old_node.random]
                new_node.random = random_node
        return old_to_new[start]