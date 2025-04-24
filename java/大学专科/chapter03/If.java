package chapter03;

import java.util.Scanner;

public class If {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// 输入四件套
//		Scanner sc = new Scanner(System.in);
//		System.out.print("输入你的成绩：");
//		int score = sc.nextInt();
//		sc.close();
//		
//		
//		if (score >= 60) {
//			System.out.println("合格！");
//		}else {
//			System.out.println("不合格！");
//		}
		Scanner sc = new Scanner(System.in);
		System.out.print("输入数字(1~7)");
		int day = sc.nextInt();
		sc.close();
		if(day == 1) 
			System.out.print("Mon");
		else if(day == 2) 
			System.out.print("Tues");
		else if(day == 3) 
			System.out.print("Wed");
		else if(day == 4) 
			System.out.print("Thur");
		else if(day == 5) 
			System.out.print("Fri");
		else if(day == 6) 
			System.out.print("Sat");
		else if(day == 7) 
			System.out.print("Sun");
		else 
			System.out.print("输入有误！");
	}

}
