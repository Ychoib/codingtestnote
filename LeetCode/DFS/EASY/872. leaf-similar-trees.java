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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> res1 = new ArrayList<>();
        List<Integer> res2 = new ArrayList<>();

        solve(root1,res1);
        solve(root2,res2);

        return res1.equals(res2);
    }
    public static void solve(TreeNode root, List res){
        if(root == null) return;
        if(root.left == null && root.right == null){
            res.add(root.val);
        }

        solve(root.left, res);
        solve(root.right, res);
    }
}