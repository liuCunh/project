package P2st;

public class ElongateParameter {
    public static void main(String[] args) {
        int[] num = {1, 2, 3, 4, 5, 6};
        System.out.printf("num的和为：%d", Elongate(num));
    }
    public static int Elongate(int... num){
        int res = 0;
        for(int i : num){
            res += i;
        }
        return res;
    }
}
