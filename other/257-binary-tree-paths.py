# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, path, arr):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                arr.append(path)
            else:
                dfs(root.left, path + '->', arr)
                dfs(root.right, path + '->', arr)
        res = []
        dfs(root, '', res)
        return res 

        