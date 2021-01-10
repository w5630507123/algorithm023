class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''迭代'''
        inorder = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmd = stack.pop()
                inorder.append(tmd.val)
                root = tmd.right
        return inorder

        '''普通递归
        a = []
        def inorder(tree):
            if not tree:
                return
            inorder(tree.left)
            a.append(tree.val)
            inorder(tree.right)
        inorder(root)
        return a
        '''