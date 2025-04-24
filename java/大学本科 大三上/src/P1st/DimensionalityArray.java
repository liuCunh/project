package P1st;

public class DimensionalityArray {
    public static void main(String[] args) {
        int[][] arr = {{1,2,3},{2,3,4},{3,4,5}};
        for(int i = 0; i<arr.length; i++){
            int res = 0;
            for (int j = 0; j<arr[i].length; j++){
                res += arr[i][j];
            }
            System.out.print(res+"\t");
        }
    }
}
