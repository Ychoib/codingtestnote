class Solution {
    public int climbStairs(int n) {
        // n = 3
        /* cost = [1,2]
        dp[i] : i 계단을 오를때 오르는 방법
           dp[0] = 0
           dp[1] = 1과 2로 1을 만들 수 있는 조합의 수 : 1
           dp[2] = 1과 2로 2을 만들 수 있는 조합의 수 : 2
           dp[3] = 1과 2로 3을 만들 수 있는 조합의 수 : dp[1] + dp[2]
           dp[4] = 1과 2로 4을 만들 수 있는 조합의 수 : dp[3] + dp[2]
           dp[i] = 1,2의 덧셈으로 조합가능한 모든 경우의 수
         */

        int[] dp = new int[n + 1];
        if(n == 1){
            return 1;
        }
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        for(int i=3;i < n + 1;i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
}