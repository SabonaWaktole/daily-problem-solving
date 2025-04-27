# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 0
        que = deque([(root, level)])
        ans = []
        current = 0
        element = []
        while que:
            
            node, level = que.popleft()
            if not node:
                continue
            if current != level and element:
                ans.append(element)
                current += 1
                element = []
            que.append((node.left, level + 1))
            que.append((node.right, level + 1))
            element.append(node.val)
        if element:
            ans.append(element)
            
        return ans