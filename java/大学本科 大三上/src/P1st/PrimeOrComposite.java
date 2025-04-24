package P1st;

import java.util.Scanner;

public class PrimeOrComposite {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("enter a number: ");
        int num = scanner.nextInt();
        if (num > 1){
            int i = 2;
            while (i < num){
                if (num % i == 0){
                    System.out.println("合数");
                }
                i++;
            }
            System.out.println("质数");
        }else {
            System.out.println("输入错误！");
        }
    }
}
