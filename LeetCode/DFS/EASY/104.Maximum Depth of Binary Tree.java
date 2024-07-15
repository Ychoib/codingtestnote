/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        int res = maxDepthHelp(root, 0);
        return res
    }
    public static int maxDepthHelp(TreeNode root, int result){
        System.out.println(root.val);
        System.out.println(result);

        if(root == null){
            return result
        }
        return Math.max(maxDepthHelp(root.left, result + 1), maxDepthHelp(root.right, result + 1));
    }
}