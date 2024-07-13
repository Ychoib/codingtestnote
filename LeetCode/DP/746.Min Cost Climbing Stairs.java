class Solution {
    public int minCostClimbingStairs(int[] cost) {
        // cost = [1,100,1,1,1,100,1,1,100,1]
        /* dp[0] = cost[0] 1
         dp[1] = cost[1] 100
        dp[2] = cost[2] + Min(dp[1], dp[0]) 2
        dp[3] = cost[3] + Min(dp[2], dp[1]) 3
        */
        int[] dp = new int[cost.length];   //dp[i] : i계단이 마지막일때, top으로 가는데 비용
        dp[0] = cost[0];
        dp[1] = cost[1];
        int i = 2;
        while(i < cost.length){
            dp[i] = cost[i] + Math.min(dp[i-1], dp[i-2]);
            System.out.println( dp[i]);
            i++;
        }
        return Math.Min(dp[cost.length-1],dp[cost.length-2]);
    }
}