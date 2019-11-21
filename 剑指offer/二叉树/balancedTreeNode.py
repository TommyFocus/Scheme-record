class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Solution_01
# O(N**2)
def getDeep(x):
	if x is None:
		return 0
	return 1 + max(getDeep(x.left), getDeep(x.right))

class Solution:
	def ISbalanced_Solution(self, pRoot):
		if not pRoot:
			return 1
		return abs(getDeep(pRoot.left) - getDeep(pRoot.right)) <= 1
			and self.ISbalanced_Solution(pRoot.left)
			and self.ISbalanced_Solution(pRoot.right)

# Sloution_02
# O(N)
def getDeep(x):
	if x is None:
		return 0
	left = getDeep(x.left)
	if left == -1:
		return -1
	right = getDeep(x.right)
	if right == -1:
		return -1
	return -1 if abs(getDeep(x.left) - getDeep(x.right)) > 1 else 1 + max(getDeep(x.left), getDeep(x.right))

class Sloution:
	def IsBalanced_Solution(self, pRoot):
		return getDeep(pRoot) != -1

		