package P2st;

public class Factorial {
    public static long factorial(int n){
        // 递归出口
        if (n <= 1){
            return 1;
        }else {
            // 递归方法调用
            return n * factorial(n - 1);
        }
    }
}
