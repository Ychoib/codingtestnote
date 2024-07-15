class Solution {
    public int maxProfit(int[] prices) {

        int[] result = minValue(prices);
        if(prices.length == 1){
            return 0;
        }
        int maxValue = 0;
        for(int j= result[1];j< prices.length;j++){
            if(maxValue < prices[j]) {
                maxValue= prices[j];
            }
        }
        System.out.println(maxValue);
        System.out.println(result[0]);
        System.out.println(result[1]);

        return maxValue - result[0];
    }
    private static int[] minValue(int[] array){
        int minValue = array[0];
        int minIndex = 0;
        int[] result = new int[2];
        for(int i=0;i<array.length;i++){
            if(minValue > array[i]){
                minValue = array[i];
                minIndex = i;
            }
        }
        result[0] = minValue;
        result[1] = minIndex;

        return result;
    }
}