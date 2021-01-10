class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #迭代
        if not root:
            return
        stack,res = [root],[]
        while stack:
            code = stack.pop()
            if code:
                res.append(code.val)
                if code.right:
                    stack.append(code.right)
                if code.left:
                    stack.append(code.left)
        return res