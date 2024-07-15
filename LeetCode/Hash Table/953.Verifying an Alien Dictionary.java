class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<String, Integer> map = new HashMap<>();

        if(words.length == 1) return true;

        for(int i=0;i<order.length();i++){
            map.put(order.split("")[i], i);
        }
        for(int j=0;j<words.length - 1;j++){
            String[] word = words[j].split("");
            String[] next_word = words[j+1].split("");
            if(words[j].equals(words[j+1])) continue;
            for(int z=0;z < Math.min(word.length, next_word.length);z++){
                if(word[z] == next_word[z]) continue;
                if(map.get(word[z]) < map.get(next_word[z])){
                    break;
                }else if(map.get(word[z]) == map.get(next_word[z])){

                    if(z == Math.min(word.length, next_word.length) - 1){
                        if(word.length > next_word.length){
                            return false;
                        }
                    }
                    continue;
                }else{
                    return false;
                }
            }

        }
        return true;
    }
}