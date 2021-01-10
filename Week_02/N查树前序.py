class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #使用递归
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                dfs(child)

        res = []
        dfs(root)
        return res