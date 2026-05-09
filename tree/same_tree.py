"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        current = queue.pop(0)
        
        if arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    
    return root

p = [1,2,3]
q = [1,2, -3]

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    isSame = True
    if p and q:
        p_val = p.val if p else None
        q_val = q.val if q else None
        if p_val != q_val:
            isSame = False
        else:
            isSame = isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    elif p or q:
        isSame = False
    return isSame

isSameTree(get_tree(p), get_tree(q))