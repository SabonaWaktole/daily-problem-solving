# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        que = deque([root])
        while que:
            node = que.popleft()
            if node.left:
                que.append(node.left)
                if node.left.val != node.val:
                    return False
            if node.right:
                que.append(node.right)
                if node.right.val != node.val:
                    return False
        return True