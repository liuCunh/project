package P1st;

import java.util.Scanner;

public class InputAndPrint {
    public static void main(String[] args) {
        System.out.println("请输入您的姓名：");
        Scanner scanner = new Scanner(System.in); // 创建输入对象
        String name = scanner.nextLine();  //输入

        System.out.println("请输入您的性别：");
        String sex = scanner.next();  //继承输入

        System.out.println("请输入您的爱好：");
        String hobby = scanner.next();

        System.out.println("大家好，我叫"+name+",我是一名"+sex+"生,我的爱好是"+hobby+"，很高兴认识大家。");
    }
}
