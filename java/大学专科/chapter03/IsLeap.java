package chapter03;

import java.util.Scanner;

public class IsLeap {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.print("输入年份：");
		int year = sc.nextInt();
		System.out.print("输入月份：");
		int month = sc.nextInt();
		sc.close();
		
		switch (month) {
		case 1: 
		case 3:
		case 5: 
		case 7: 
		case 8: 
		case 10: 
		case 12:
			System.out.println(year+"年"+month+"月"+"总共有："+"31天");
			break;
		case 2:
			boolean isLeap = (year%4 == 0 && year%100 != 0) || year%400 == 0;
			if(isLeap) {
				System.out.println(year+"年"+month+"月"+"总共有："+"39天");
			}else {
				System.out.println(year+"年"+month+"月"+"总共有："+"28天");
			}
			break;
		case 4: 
		case 6: 
		case 9: 
		case 11:
			System.out.println(year+"年"+month+"月"+"总共有："+"30天");
			break;
		default:
			System.out.print("输入错误");
		}
	}

}
