package chapter02;

import java.util.Scanner;

public class Circle {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Scanner a = new Scanner(System.in);
//		System.out.print("r: ");
//		double r = a.nextDouble();
//		a.close();
//		int tmp = (int)(r* 2 * 3.14);
//		System.out.print("周长=" + tmp);
		
		
		double r, perimeter, area;
		final double PI = 3.1415926;  // 圆周率Π
		Scanner scan = new Scanner(System.in);
		System.out.print("圆的半径：");
		r = scan.nextDouble();
		scan.close();
		
		perimeter = 2 * PI * r;
		int perimeter1 = (int)perimeter;
		System.out.println("圆的周长=" + perimeter1);
		
		area = PI * r * r;
		System.out.printf("圆的面积=%.2f\n", area);
		
		// Math.round(nums)函数，将nums小数点后的数给去除
		System.out.print("圆的面积=" + (double)Math.round(area*100)/100);
		
		

		
	}

}
