// Return the root node of a binary search tree that matches the given preorder traversal.
//
// (Recall that a binary search tree is a binary tree where for every node,
// any descendant of node.left has a value < node.val, and any descendant of
//  node.right has a value > node.val.  Also recall that a preorder traversal
//  displays the value of the node first, then traverses node.left, then traverses node.right.)


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode bstFromPreorder(int[] preorder) {
		return constructBST(preorder, 0, preorder.length - 1);
    }

    public static TreeNode constructBST(int[] preorder, int start, int end)
	{
		// base case
		if (start > end) {
			return null;
		}

		TreeNode node = new TreeNode(preorder[start]);
    int i;
		for (i = start; i <= end; i++) {
			if (preorder[i] > node.val) {
				break;
			}
		}

		// recursively construct the left sub-tree
		node.left = constructBST(preorder, start + 1, i - 1);

		// recursively construct the right sub-tree
		node.right = constructBST(preorder, i, end);

		// return current node
		return node;
	}

}
