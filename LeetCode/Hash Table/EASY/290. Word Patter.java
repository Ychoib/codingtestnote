class Solution {
    public boolean wordPattern(String pattern, String s) {


        String[] sarray = s.split(" ");
        String[] patternarray = pattern.split("");
        if(sarray.length != patternarray.length) return false;
        Map<String, String> hash = new HashMap<>();

        for(int i=0; i < patternarray.length; i++){
            if(hash.containsKey(patternarray[i])){
                if(!hash.get(patternarray[i]).equals(sarray[i])){
                    return false;
                }
            }else{
                if(!hash.containsValue(sarray[i])){
                    System.out.println(patternarray[i]);

                    System.out.println(sarray[i]);
                    hash.put(patternarray[i], sarray[i]);
                }else{
                    return false;
                }
            }

        }
        return true;
    }
}