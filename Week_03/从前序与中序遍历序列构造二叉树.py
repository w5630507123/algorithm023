# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pOrder, iOrder):
            if not pOrder: return None
            root = TreeNode(pOrder[0])  # 前序第一个节点做为根
            rootInx = iOrder.index(root.val)  # 在中序中找到前序第一个节点的位置
            root.left = helper(pOrder[1:rootInx + 1], iOrder[0:rootInx])
            root.right = helper(pOrder[rootInx + 1:], iOrder[rootInx + 1:])
            return root
        return helper(preorder,inorder)

