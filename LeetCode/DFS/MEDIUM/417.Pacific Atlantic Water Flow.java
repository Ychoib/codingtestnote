class Solution {
    List<List<Integer>> result = new ArrayList<>();
    boolean Pacific = false;
    boolean Atlantic = false;
    public List<List<Integer>> pacificAtlantic(int[][] heights) {

        for(int i=0; i < heights.length; i++){
            for(int j=0; j < heights[0].length; j++){
                int[][] visit = new int[heights.length][heights[0].length];
                Pacific = false;
                Atlantic = false;
                touchOcean(heights,i,j,visit);
                if(Pacific && Atlantic || (heights.length == 1 && heights[0].length == 1)){
                    List<Integer> list = new ArrayList<>();
                    list.add(i);
                    list.add(j);
                    result.add(list);
                }
            }
        }
        return result;
    }


    public void touchOcean(int[][] heights, int i, int j, int[][] visit){
        if(Pacific && Atlantic) return;
        int height = heights[i][j];
        int up=0;
        int down=0;
        int left=0;
        int right=0;
        int x = heights.length - 1;
        int y = heights[0].length - 1;


        visit[i][j] = -1;


        if(i < heights.length && i > 0){

            up = heights[i-1][j];
            if(i == 0 || j == 0){
                Pacific = true;
            }
            if(i == x || j == y){
                Atlantic = true;
            }
            if(height >= up && visit[i-1][j] != -1){

                touchOcean(heights, i-1 , j,visit);
            }
        }
        if(i < heights.length - 1 && i >= 0){

            down = heights[i+1][j];

            if(i == 0 || j == 0){
                Pacific = true;
            }
            if(i == x || j == y){
                Atlantic = true;
            }
            if(height >= down && visit[i+1][j] != -1) {

                touchOcean(heights, i+1, j,visit);
            }
        }
        if(j < heights[0].length && j > 0){

            left = heights[i][j-1];
            if(i == 0 || j == 0){
                Pacific = true;
            }
            if(i == x || j == y){
                Atlantic = true;
            }
            if(height >= left && visit[i][j -1] != -1) {
                touchOcean(heights, i, j - 1,visit);
            }
        }
        if(j < heights[0].length - 1 && j >= 0){

            right = heights[i][j+1];
            if(i == 0 || j == 0){
                Pacific = true;
            }
            if(i == x || j == y){
                Atlantic = true;
            }
            if(height >= right && visit[i][j+1] != -1){
                touchOcean(heights, i , j+1,visit);
            }
        }

        return;
    }
}