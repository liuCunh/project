package exam.util;

import java.util.Scanner;

public class PrintAgeLevel {
    public static void main(String[] args) {
        // 用户输入
        Scanner sc = new Scanner(System.in);
        // 输入年龄
        int inAge = sc.nextInt();
        if(inAge > 60){
            System.out.println("老年");
        } else if (inAge >= 40) {
            System.out.println("中老年");
        } else if (inAge >=26) {
            System.out.println("壮年");
        } else if (inAge >= 18){
            System.out.println("青年");
        } else {
            System.out.println("少年");
        }
    }
}
