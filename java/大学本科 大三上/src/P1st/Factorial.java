package P1st;

import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        long res = 1;
        for (int i=1; i <=  n; i++){
            res = res * i;
        }
        System.out.println(n+"! = "+res);
    }
}
