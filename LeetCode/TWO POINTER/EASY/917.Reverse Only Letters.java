class Solution {
    public String reverseOnlyLetters(String s) {
        char[] arrays = s.toCharArray();
        Stack<String> stack = new Stack<>();
        for(int i=0;i<arrays.length;i++){
            if(isEnglish(arrays[i])){
                stack.push(String.valueOf(arrays[i]));
            }
        }
        String news = "";
        for(int i=0;i<arrays.length;i++){
            if(Character.isLetter(arrays[i])){
                news += stack.pop();
            }else{
                news += String.valueOf(arrays[i]);
            }
        }
        return news;
    }

}