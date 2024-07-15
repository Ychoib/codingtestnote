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
    public boolean findTarget(TreeNode root, int k) {
        List<Integer> arr = new ArrayList<>();
        if(root.left == null && root.right == null){
            return false;
        }
        addArr(root,arr);
        System.out.println(arr);

        int i = 0;
        int j = arr.size() - 1;
        while(i < j){
            int sum = arr.get(i) + arr.get(j);
            System.out.println(arr.get(i));
            System.out.println(arr.get(j));

            if(i == j) return false;
            if( sum > k){
                j--;
            }else if(sum < k){
                i++;
            }else{
                return true;
            }
        }
        return false;
    }

    public static void addArr(TreeNode root, List arr){
        if(root.left != null) addArr(root.left,arr);
        if(root != null) arr.add(root.val);
        if(root.right != null) addArr(root.right,arr);
        return;
    }
}