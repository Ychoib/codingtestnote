class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a,b) -> Integer.compare(b[1], a[1]));
        int maximumunits = 0;
        for(int i=0; i < boxTypes.length;i++){
            System.out.println(truckSize);
            System.out.println(boxTypes[i][0]);
            System.out.println(boxTypes[i][1]);
            if(truckSize - boxTypes[i][0] >= 0){
                truckSize -= boxTypes[i][0];
                maximumunits += boxTypes[i][1] * boxTypes[i][0];
            }else{
                maximumunits += boxTypes[i][1] * truckSize;
                break;
            }
        }
        return maximumunits;
    }
}