class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> hash = new HashSet<>();
        for(int n : nums){
            if(hash.add(n)){
                return true;
            }
        }
        return false;
    }
}