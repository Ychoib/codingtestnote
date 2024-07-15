class Solution {
    public int islandPerimeter(int[][] grid) {
        if(grid == null) return 0;
        for(int i=0;i< grid.length;i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == 1){
                    return solve(grid, i,j);
                }
            }
        }
        return 0;
    }

    public static int solve(int[][] grid, int x, int y){

        if(x >= 0 && y >= 0 && y < grid[0].length && x < grid.length){
            int count = 0;
            if(grid[x][y] == 0) return 1;
            if(grid[x][y] == -1) return 0;
            grid[x][y] = -1;
            count += solve(grid, x - 1, y);
            count += solve(grid, x + 1, y);
            count += solve(grid, x, y - 1);
            count += solve(grid, x, y + 1);
            return count;
        }else{
            return 1;
        }


    }

}