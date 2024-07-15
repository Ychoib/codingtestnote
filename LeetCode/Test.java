class Solution {
    public int minNumberOfFrogs(String croakOfFrogs) {

       int numOfFrogs = 0;
       String[] array = croakOfFrogs.split("");

       checkfrog(array, 0, numOfFrogs);

//       for(int i=0; i< array.length;i++){
//           //c가 보일때마다 frog 확인
//           if(array[i].equals("c") && ){
//
//               if(checkfrog(array, i)){
//                   numOfFrogs += 1;
//               }
//           }
//       }
       return numOfFrogs;
    }
    public static void checkfrog(String[] array, int index, int numOfFrogs){
        boolean flag = false;

        for(int i=index; i < array.length; i++){

            System.out.println(array[i]);
            System.out.println(flag);

            if(array[i].equals("c") && flag == false){
                flag = true;
                continue;
            }else if (array[i].equals("c") && flag == true){
                //새로운 개구리 발견
                checkfrog(array, i, numOfFrogs);
            }

            if(array[i].equals("r") && flag == true){
                continue;
            }else{
                flag = false;
            }
            if(array[i].equals("o") && flag == true){
                continue;
            }else{
                flag = false;
            }
            if(array[i].equals("a") && flag == true){
                continue;
            }else{
                flag = false;
            }

            if(array[i].equals("k") && flag == true){
                numOfFrogs += 1;
                return;
            }else{
                flag = false;
            }

        }
        return;
    }
}