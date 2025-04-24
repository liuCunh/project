package exam.util;

public class Factorial {
    public static void main(String[] args) {
        System.out.println(factorial(4));
    }
    // 阶乘方法
    public static int factorial(int n){
        if (n < 2){
            return 1;
        }
        return factorial(n-1) * n;
    }
}
