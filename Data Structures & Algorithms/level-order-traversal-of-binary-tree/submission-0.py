# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        def bfs(root):
            if not root:
                return result

            queue = deque()

            queue.append(root)
            while len(queue) > 0:
                list = []
                for i in range(len(queue)):
                    curr = queue.popleft()
                    list.append(curr.val)
                    if curr.left: 
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                result.append(list)
        
        bfs(root)
        return result

