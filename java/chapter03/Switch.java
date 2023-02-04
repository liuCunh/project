package chapter03;

import java.util.Scanner;

public class Switch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.print("输入数字(1~7):");
		int day = sc.nextInt();
		sc.close();
		switch (day) {
		case 1:
			System.out.print("Mon");
			break;
		case 2:
			System.out.print("Tue");
			break;
		case 3:
			System.out.print("Wednesday");
			break;
		case 4:
			System.out.print("Thursday");
			break;
		case 5:
			System.out.print("Friday");
			break;
		case 6:
			System.out.print("Saturday");
			break;
		case 7:
			System.out.print("Sunday");
			break;
		default:
			System.out.print("输入错误！");
			
		}
	}

}
