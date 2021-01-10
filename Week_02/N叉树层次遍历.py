class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #思路：广度优先遍历
        def bfs(root):
            if not root:
                return
            for child in root.children:
                s.append(child.val)
                bfs(child)
            ss.append(s)
            bfs(root.children)
        s,ss = [],[]
        bfs(root)
        return ss