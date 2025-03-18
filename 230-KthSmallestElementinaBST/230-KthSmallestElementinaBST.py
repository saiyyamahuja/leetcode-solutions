# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [[]];
        current = root
        count = 0
        
        while len(stack) > 0 or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            count += 1
            
            if count == k:
                return current.val
            
            current = current.right
            
        return -1        