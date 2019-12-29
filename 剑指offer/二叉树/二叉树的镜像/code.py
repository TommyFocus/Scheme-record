# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def mirror(self, root):
        if not root:
            return None
        tmp = self.mirror(root.right)
        root.right = self.mirror(root.left)
        root.left = tmp
        return root
