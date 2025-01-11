package P1st;

import java.util.Scanner;

public class AgeLevel {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入你的你年龄：");
        int age = scanner.nextInt();
        if(age > 60){
            System.out.println("老年");
        } else if (age >=40) {
            System.out.println("中老年");
        } else if (age>=26) {
            System.out.println("壮年");
        } else if (age >= 18) {
            System.out.println("青年");
        } else if (age >= 0) {
            System.out.println("少年");
        }else{
            System.out.println("输入错误");
        }
    }
}
