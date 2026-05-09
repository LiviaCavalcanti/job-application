
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    queue = [root] if root else []
    while queue:
        level = []
        l = []
        for _ in range(len(queue)):
            elem = queue.pop(0)
            l.append(elem.val)
            if elem.left:
                level.append(elem.left)
            if elem.right:
                level.append(elem.right)
        result.append(l)
        queue = level
    return result
    
from same_tree import get_tree
print(levelOrder(get_tree([3,9,20,None,None,15,7])))