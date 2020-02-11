struct TreeNode {
	int val;
	struct TreeNode* left;
	struct TreeNode* rught;
	TreeNode(int x):
		val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	int TreeDepth(TreeNode* pRoot)
	{
		if (!pRoot) return 0;
		return max(TreeDepth(TreeNode->left)+1, TreeDepth(TreeNode->right)+1)
	}
};