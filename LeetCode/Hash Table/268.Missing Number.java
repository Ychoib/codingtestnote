class Solution {
    public int missingNumber(int[] nums) {
        int length = nums.length;
        Set<Integer> hash = new HashSet<>();
        for(int n : nums){
            hash.add(n);
        }
        for(int n=0;n<=length;n++){
            if(!hash.contains(n)){
                return n;
            }
        }
        return 0;
    }
}