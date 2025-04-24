package P2st;

import java.util.Scanner;

public class Recursion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        System.out.printf("%d! = %d", n, factorial(n));
    }
    // 斐波那契数列
    public static long factorial(long n){
        if (n<2){
            // 程序出口
            return 1;
        }else {
            return n * factorial(n - 1);
        }
    }
}
