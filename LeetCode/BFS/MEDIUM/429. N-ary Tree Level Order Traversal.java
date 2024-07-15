/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> result = new ArrayList<>();
        if(root == null) return result;

        List<Integer> rootnum = new ArrayList<>();
        int depth = 1;
        rootnum.add(root.val);
        result.add(rootnum);
        getChildren(root, result, depth);
        return result;
    }

    public static void getChildren(Node root, List<List<Integer>> result, int depth){
        if(root.children.size() == 0 ) return;
        List<Integer> list = new ArrayList<>();

        System.out.println(depth);

        if(result.size() - 1 < depth){
            for(Node children : root.children){
                list.add(children.val);
            }
            result.add(list);
        }else{
            for(Node children : root.children){
                result.get(depth).add(children.val);
            }
        }
        System.out.println(result);


        for(int i=0; i < root.children.size(); i++){
            if(root.children.get(i) != null){
                //System.out.println(root.children.get(i).val);
                //System.out.println(depth);
                getChildren(root.children.get(i), result, depth + 1);
            }
        }

        return;
    }
}