package P1st;

import java.util.Scanner;

public class NumberMax {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double maxValue = Double.MIN_VALUE;
        for(int i = 0; i<3; i++){
            System.out.print("Enter a number: ");
            int a = scanner.nextInt();
            if (a > maxValue){
                maxValue = a;
            }
        }
        System.out.println("您输入的三个值中最大值为："+maxValue);
    }
}
