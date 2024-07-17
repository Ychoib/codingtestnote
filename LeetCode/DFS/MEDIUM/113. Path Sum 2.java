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
    private List<List<Integer>> result = new ArrayList<List<Integer>>();
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if(root == null) return new ArrayList<>();
        Stack<Integer> stack = new Stack<Integer>();
        goPath(root, targetSum, stack);
        return result;
    }

    public void goPath(TreeNode root, int targetSum, Stack<Integer> stack){
        stack.add(root.val);
        if(root.left == null && root.right ==null)
            if(targetSum == root.val) result.add(new ArrayList<Integer>(stack));

        if(root.left != null) goPath(root.left, targetSum - root.val, stack);
        if(root.right != null) goPath(root.right, targetSum - root.val, stack);
        System.out.println(stack.pop());
    }

}