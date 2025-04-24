package P1st;

import java.util.Scanner;

public class IsLuck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Place enter a number: ");
        int num = scanner.nextInt();
        if (num > 0 && num % 3 == 0 && num % 5== 0){
            System.out.printf("%d是一个幸运数字", num);
        }else {
            System.out.printf("%d不是一个幸运数字", num);
        }
    }
}
